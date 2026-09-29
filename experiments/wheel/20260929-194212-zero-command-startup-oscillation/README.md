# 0929-01 双轮零指令启动后前后摆动

- 原始 bag：`lw_real_20260929-194212`，4905 帧，98.080 秒。
- 实际记录：2026-09-29 19:42:22.691–19:44:00.771，Asia/Shanghai。目录名是录制启动时间。
- 用户确认：双轮完全落地承重，使用 0929-01，没有速度指令；本轮策略阶段未人工触碰。前后晃动后立即请求 GetDown，随后绳子拉住机身。
- 记录支持：全程 control.x/y/yaw 均为零；策略运行约 1.56 秒内，轮速反复换向，Pitch -15.77°至 +14.37°，右轮目标峰值约 30.01 rad/s。约 0.8 秒的往复没有快速收敛。双髋速度峰值约 0.40 rad/s，与此前高频髋振荡不同。
- 结果：`zero_command_startup_pitch_wheel_oscillation`；不能标记为稳定性验收通过，唯一根因未确定。

## 数据入口

1. [分析报告](analysis/analysis.md)、[启动曲线](analysis/startup.png)、[两轮对比曲线](analysis/two_trials.png)。
2. [全量 CSV](exports/joint_states.csv)、[字段说明](exports/README.md)、[逐值验证](exports/validation.json)。
3. [原始 bag 元数据](raw/lw_real_20260929-194212/metadata.yaml)、[来源与哈希](manifest.json)、[部署资源快照](context/README.md)。

约 bag 相对 41.000 秒策略接管，42.580 秒目标模式转入 GetDown；FSM 边界由轨迹推断，用户确认操作。GetDown 后有绳子介入，不混入策略运行峰值。前一轮有人工扶持和短暂前进指令，见 [前一轮说明](../20260929-193808-startup-oscillation-manual-support/README.md)，不能作为受控 A/B。

## 版本与证据限制

用户确认 `lw-release-20260929-01`，提交 `e959d64d0ae6fb27d736cf64c96552af15ab54a5`。对应部署资源与清单哈希一致；运行中二进制没有独立取证，硬件/固件版本及同步视频未知。

当前部署 base.yaml、Wheel config.yaml 与 0928-01 按字节相同，模型更新为无速度估计版本。输入、历史/reset、训练动作比例、实物轮端响应等契约仍需核对，不能因资源哈希一致推断闭环稳定。

报告、NPZ time_s 和 CSV time_s 均采用 bag 首帧相对时间，header 整数时间戳独立保留。50 Hz 调试记录不等于全部 200 Hz 控制/硬件采样；目标不等于实际反馈，target effort 为按 RL 增益重算的 PD 值。源文档中的 Jetson 绝对路径按原文保留，换机器请按 manifest.json 相对路径访问。
