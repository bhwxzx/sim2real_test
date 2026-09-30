# 全量 JointState CSV

`joint_states.csv` 逐条导出该场次原始 bag 的全部消息。CSV 为 UTF-8、逗号分隔、LF 换行，一条消息一行，85 列：7 列时间/元信息 + 26 个名称各自的 position、velocity、effort，共 78 个数值通道。名称顺序与原始消息一致，列名使用 `<name>.<field>`。

没有插值、重采样、滤波、裁剪或重复值去除；占位零值也保留。CSV 覆盖“已录制的全部消息和字段”，不代表设备或控制循环的每一周期都被记录。原 bag 是序列化层面的原始依据，CSV 是数值访问副本。

## 时间与元信息

| 列 | 含义与单位 |
|---|---|
| row_index | 从 0 开始的导出行号，不是 ROS 消息序号；按 bag timestamp、SQLite message id 排序 |
| bag_timestamp_ns | SQLite messages.timestamp 原始整数，单位 ns |
| header_stamp_sec | ROS header.stamp.sec 原值，单位 s |
| header_stamp_nanosec | ROS header.stamp.nanosec 原值，单位 ns |
| header_stamp_ns | 上面两项按整数计算的合并时间戳，单位 ns |
| time_s | 相对第一条 bag 时间戳的秒数；先做整数差，再输出 9 位小数 |
| frame_id | 原始 header.frame_id；本场全部为空字符串 |

bag 时间戳与消息 header 时间戳分别保留，不相互替代。header 时间是发布端消息时间，不能视为每个关节或 IMU 的硬件采样时间。数值信号使用可往返还原原 float64 数值的十进制表示；未按显示精度四舍五入。

Excel 导入时将纳秒时间戳列设为“文本”，避免其约 15 位有效数字限制导致末尾精度丢失。绘图使用 `time_s`；Python 读取纳秒列使用 `int`，不要先转成 `float`。

## LW 字段解释

这个话题借用 sensor_msgs/msg/JointState 封装辅助信号。必须按名称与字段共同解释，不能将所有 position 都当作角度、所有 effort 都当作力矩。

| 名称组 | position | velocity | effort |
|---|---|---|---|
| right/left_hip_now、thigh_now、shank_now、foot_now | 设备反馈位置，rad | 设备反馈角速度，rad/s | 设备报告力矩，Nm |
| right_wheel_now、left_wheel_now | 发布器占位 0，未记录轮位置 | 设备反馈角速度，rad/s | 设备报告力矩，Nm |
| right/left_hip_target、thigh_target、shank_target、foot_target | 下发参考位置，rad | 发布器占位 0 | 发布器按 RL Kp/Kd 和反馈计算的 PD 估算值，Nm |
| right_wheel_target、left_wheel_target | 发布器占位 0 | 下发参考角速度，rad/s | 发布器按 RL Kp/Kd 和反馈计算的 PD 估算值，Nm |
| imu_ang_vel | 陀螺仪 x，rad/s | 陀螺仪 y，rad/s | 陀螺仪 z，rad/s |
| imu_quat_w、imu_quat_x、imu_quat_y、imu_quat_z | 四元数对应分量，无量纲 | 发布器占位 0 | 发布器占位 0 |
| cmd_vel | control.x 原值 | control.y 原值 | control.yaw 原值 |

`foot` 对应现有分析中的踝关节命名。`cmd_vel` 是控制输入，不是实测机身速度；本导出未施加策略 commands_scale，不能把这些原值直接当作已校准的 m/s 或 rad/s。

`*_target.effort` 不是最终电机输出或实际饱和后的力矩，也没有包含全部补偿项；GetUp/GetDown/Passive 的实际增益可能不同。不要把这些字段解释为所有状态下的实际执行力矩。占位 0 不代表对应物理量为零。

语义核对依据：rl_sar `03104469746402c407e54c4142ad0a8c9d8710af` 的 `src/rl_sar/library/core/debug/lw_debug_publisher.cpp`（populateMessage）和 `src/rl_sar/src/rl_real_LW.cpp`（LWDebugSnapshot）。已核对本场实际消息的名称、数组长度与占位字段。用户确认本场使用对应部署包，资源哈希与其清单一致；未独立捕获运行中可执行文件哈希。

本场共 3508 条消息。分析报告、decoded.npz 的 time_s 和 CSV 的 time_s 均使用相对第一条消息的 bag 时间。header 整数时间戳独立保留，不能视为硬件采样时间；严格对齐请使用整数时间戳与 row_index。

## 无 ROS 2 读取

CSV 可直接导入 Excel、MATLAB 或 PlotJuggler；PlotJuggler 的时间列选择 `time_s`。Python 只用标准库即可读取：

```python
import csv

with open("joint_states.csv", encoding="utf-8", newline="") as stream:
    for row in csv.DictReader(stream):
        timestamp_ns = int(row["bag_timestamp_ns"])
        time_s = float(row["time_s"])
        right_hip_rad = float(row["right_hip_now.position"])
        gyro_z_rad_s = float(row["imu_ang_vel.effort"])
        # 在这里进行自己的分析
```

`analysis/decoded.npz` 保留完整解码与派生数组，键为 bag_ns、header_ns、time_s、names、position、velocity、effort、rpy_deg、command、gyro_rad_s。CSV 不附加派生角度，直接保留原始四元数；派生角度以 XYZ 欧拉角、度表示。

## 再生成与核验

导出脚本在仓库根目录的 `tools/export_joint_states_csv.py`，从原始 SQLite bag 解码，不依赖 NPZ。转换端需要 ROS 2 Humble 的 rclpy 和 sensor_msgs；CSV 使用端无需 ROS 2。脚本只读 bag，并拒绝覆盖已存在的输出。

在仓库根目录运行（将场次路径替换为对应目录，并选择新的输出路径）：

```bash
source /opt/ros/humble/setup.bash
python3 tools/export_joint_states_csv.py \
  experiments/<模式>/<场次>/raw/<bag目录>/<bag文件>_0.db3 \
  /tmp/joint_states-new.csv
```

本次验证包括：CSV 逐行往返读取，与原 bag 的时间戳、frame_id、全部 78 个数值通道比对；再与既有 decoded.npz 独立交叉核对，保留负零（本场核对 392 个负零数值）。结果、输入和输出哈希见 `validation.json`，来源登记见上级 `manifest.json`。校验整个仓库可在根目录运行 `sha256sum -c SHA256SUMS`。
