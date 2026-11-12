# 全量 JointState CSV

本场 2098 行、85 列：7 列时间/元信息 + 26 个名称各自的 position、velocity、effort，共 78 个数值通道。列名为 `<name>.<field>`。

本次从已有 `analysis/decoded.npz` 原值导出；只读取原 bag 的 SQLite 时间和 CDR 消息头以恢复 sec/nanosec/frame_id，没有重复解码数值载荷。CSV 逐行回读，与 NPZ 进行 float64 位模式比较（包括负零），时间与 frame_id 核对原 bag；详见 validation.json。没有插值、滤波、重采样、删帧或去重。原 bag 仍是原始依据。

## 时间字段

`row_index` 为零起始行号；`bag_timestamp_ns` 为 SQLite 时间；`header_stamp_sec`、`header_stamp_nanosec`、`header_stamp_ns` 为原消息头时间；`time_s` 为相对首条 bag 消息时间，整数差后输出 9 位小数；`frame_id` 保留原文。Excel 导入纳秒列应设为文本，Python 使用 int。它们不是单电机硬件采样时间。

## 数值含义

| 名称 | position | velocity | effort |
|---|---|---|---|
| hip/thigh/shank/foot_now | 反馈位置 rad | 反馈速度 rad/s | 驱动估计力矩 Nm |
| wheel_now | 占位 0 | 反馈轮速 rad/s | 驱动估计力矩 Nm |
| hip/thigh/shank/foot_target | 目标位置 rad | 占位 0 | 发布器使用 RL 增益计算的 PD 估算值 |
| wheel_target | 占位 0 | 目标轮速 rad/s | 发布器 PD 估算值 |
| imu_ang_vel | 陀螺仪 x rad/s | y rad/s | z rad/s |
| imu_quat_w/x/y/z | 对应四元数分量 | 占位 0 | 占位 0 |
| cmd_vel | 前进输入 | 侧移输入 | 转向输入 |

`foot` 对应踝关节；cmd_vel 是记录的操作输入，不是实测机身速度。target effort 不是所有状态的最终实际下发力矩，不能忽略 GetUp/GetDown/Passive 增益差异。占位零不代表物理量为零。语义依据当前 1112-01 参考发布器，版本证据和限制见场次 context。

16:08 场次含电源线脱落及右小腿旧反馈重复；CSV 原样保留，不将冻结值视为可信真实运动。数值有限或消息更新不保证单关节反馈新鲜。

可用 Excel、MATLAB、Python、PlotJuggler 直接读取，绘图时间列选 time_s。若未来需要独立重新解码，仓库现有 tools/export_joint_states_csv.py 支持从 bag 导出到新的文件；本次未运行该解码流程。
