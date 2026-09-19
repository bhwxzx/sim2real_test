#!/usr/bin/env python3
"""Export the archived LW JointState SQLite bag to an unresampled CSV.

Conversion requires ROS 2 sensor_msgs/rclpy; reading the CSV does not.
Run from a ROS 2 terminal, passing one .db3 file and a new CSV path.
"""
import argparse
import csv
from pathlib import Path
import sqlite3

TIME_COLUMNS = [
    "row_index", "bag_timestamp_ns", "header_stamp_sec",
    "header_stamp_nanosec", "header_stamp_ns", "time_s", "frame_id",
]
ARRAY_FIELDS = ("position", "velocity", "effort")
JOINTS = (
    "right_hip", "left_hip", "right_thigh", "left_thigh",
    "right_shank", "left_shank", "right_foot", "left_foot",
    "right_wheel", "left_wheel",
)
EXPECTED_NAMES = (
    tuple(name + "_now" for name in JOINTS)
    + tuple(name + "_target" for name in JOINTS)
    + ("imu_ang_vel", "imu_quat_w", "imu_quat_x", "imu_quat_y", "imu_quat_z", "cmd_vel")
)


def export(db_path, output):
    from rclpy.serialization import deserialize_message
    from sensor_msgs.msg import JointState

    db_path = db_path.resolve(strict=True)
    if output.exists():
        raise FileExistsError("Output already exists: " + str(output))
    with sqlite3.connect(db_path.as_uri() + "?mode=ro", uri=True) as db:
        topics = db.execute("SELECT id,name,type,serialization_format FROM topics").fetchall()
        if len(topics) != 1 or topics[0][1:] != (
            "/LW_joint_states", "sensor_msgs/msg/JointState", "cdr"
        ):
            raise ValueError("Expected exactly one CDR /LW_joint_states topic")
        topic_id = topics[0][0]
        expected_count = db.execute("SELECT count(*) FROM messages").fetchone()[0]
        if not expected_count:
            raise ValueError("Bag is empty")
        header = TIME_COLUMNS + [
            name + "." + field for name in EXPECTED_NAMES for field in ARRAY_FIELDS
        ]
        output.parent.mkdir(parents=True, exist_ok=True)
        count = 0
        first_ns = None
        created = False
        try:
            with output.open("x", encoding="utf-8", newline="") as stream:
                created = True
                writer = csv.writer(stream, lineterminator="\n")
                writer.writerow(header)
                for bag_ns, payload in db.execute(
                    "SELECT timestamp,data FROM messages WHERE topic_id=? ORDER BY timestamp,id",
                    (topic_id,),
                ):
                    msg = deserialize_message(payload, JointState)
                    if tuple(msg.name) != EXPECTED_NAMES:
                        raise ValueError("Unexpected or changing message.name layout")
                    if any(len(getattr(msg, field)) != 26 for field in ARRAY_FIELDS):
                        raise ValueError("Unexpected array length")
                    if first_ns is None:
                        first_ns = bag_ns
                    sec, nano = msg.header.stamp.sec, msg.header.stamp.nanosec
                    if not 0 <= nano < 1_000_000_000:
                        raise ValueError("Invalid header nanosecond component")
                    elapsed_sec, elapsed_ns = divmod(bag_ns - first_ns, 1_000_000_000)
                    row = [
                        str(count), str(bag_ns), str(sec), str(nano),
                        str(sec * 1_000_000_000 + nano),
                        f"{elapsed_sec}.{elapsed_ns:09d}", msg.header.frame_id,
                    ]
                    row.extend(
                        repr(float(getattr(msg, field)[index]))
                        for index in range(26) for field in ARRAY_FIELDS
                    )
                    writer.writerow(row)
                    count += 1
                if count != expected_count:
                    raise ValueError("Exported row count differs from bag message count")
        except Exception:
            # Only remove the incomplete file this invocation created.
            # An existing destination is rejected before opening.
            if created:
                output.unlink(missing_ok=True)
            raise
    return count, len(header)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bag_file", type=Path)
    parser.add_argument("output_csv", type=Path)
    args = parser.parse_args()
    if args.bag_file.resolve() == args.output_csv.resolve():
        parser.error("Input and output must differ")
    count, columns = export(args.bag_file, args.output_csv)
    print(f"{args.output_csv}: {count} rows, {columns} columns")


if __name__ == "__main__":
    main()
