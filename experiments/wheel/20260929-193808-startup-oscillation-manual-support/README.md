# 0929-01 双轮启动后摆动（有人工扶持）

- 原始 bag：`lw_real_20260929-193808`，4538 帧，90.740 秒。
- 实际记录：2026-09-29 19:38:35.166–19:40:05.906，Asia/Shanghai。
- 用户确认与第二轮为同版 0929-01，测试期间手动扶住机身。扶持的精确时段没有录制。
- bag 记录短暂前进指令，control.x 最大约 0.476；不可标记为全程零指令。第一条非零指令约为 bag 相对 46.440 秒。最初约 1.32 秒零指令阶段已有轮速换向和俯仰变化。
- 结果：`startup_oscillation_with_manual_support_and_forward_input`。有人工干预，不作为稳定性验收或自由运动对照。

## 数据入口

1. [本轮分析摘要](analysis/analysis.md)、[未经人工触碰的下一轮分析](../20260929-194212-zero-command-startup-oscillation/analysis/analysis.md)。
2. [全量 CSV](exports/joint_states.csv)、[字段说明](exports/README.md)、[逐值验证](exports/validation.json)。
3. [原始 bag 元数据](raw/lw_real_20260929-193808/metadata.yaml)、[来源与哈希](manifest.json)、[部署资源快照](context/README.md)。

约 bag 相对 45.100 秒策略接管、55.200 秒进入疑似 GetDown 轨迹，FSM 状态没有直接录制。人工扶持影响运动响应，不能据本轮判断策略能否自行稳定；主要动力学结论见下一轮未人工触碰的数据。

## 版本与证据限制

用户确认 `lw-release-20260929-01`，提交 `e959d64d0ae6fb27d736cf64c96552af15ab54a5`。对应部署资源与清单哈希一致；运行中二进制没有独立取证，硬件/固件版本及同步视频未知。

当前部署 base.yaml、Wheel config.yaml 与 0928-01 按字节相同，模型更新为无速度估计版本。输入、历史/reset、训练动作比例、实物轮端响应等契约仍需核对，不能因资源哈希一致推断闭环稳定。

报告、NPZ time_s 和 CSV time_s 均采用 bag 首帧相对时间，header 整数时间戳独立保留。50 Hz 调试记录不等于全部 200 Hz 控制/硬件采样；目标不等于实际反馈，target effort 为按 RL 增益重算的 PD 值。源文档中的 Jetson 绝对路径按原文保留，换机器请按 manifest.json 相对路径访问。
