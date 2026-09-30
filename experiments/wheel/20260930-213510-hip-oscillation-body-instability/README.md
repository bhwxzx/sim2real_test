# 0930-01 双轮前进减速后髋部剧烈振荡与机身失稳

- 原始 bag：`lw_real_20260930-213510`，3508 帧、70.144 秒。实际调试消息时间为 2026-09-30 21:35:36.562–21:36:46.706，Asia/Shanghai；目录名是开始录制时间，不是第一条消息时间。
- 用户确认：双轮模式，使用 0930-01；机身完全落地承重，吊绳松弛，没有人扶；测试中有运动指令，失稳后按了 GetDown。用户观察到机身失稳且腿部剧烈甩动。
- 记录支持：策略阶段有前进指令、无转向指令。前进指令在 bag 相对 69.003 s 回零；左髋反馈速度约 69.543 s 开始明显增长，双髋目标约 69.703 s 开始快速放大并反向。策略窗口内双髋目标绝对峰值约 3.21 rad、髋反馈速度约 18.93 rad/s；末帧横滚约 −29.5°。这些是不同通道的峰值，不一定同帧发生。
- 结果：`forward_deceleration_hip_oscillation_body_instability`。记录呈现双髋目标与反馈的快速闭环放大，但无法由该 topic 确定最初扰动的唯一原因；不能标记为稳定性验收通过，也不能把前进回零直接判为唯一根因。

## 数据入口

1. [分析报告](analysis/analysis.md)、[末段曲线](analysis/event_window.png)、[左右髋起点跨场比较](analysis/hip_onset_comparison.md)及[比较明细](analysis/comparison.json)。跨场比较原文中的绝对路径指向 Jetson 的原始报告；早期场次也可从本仓库的 [catalog.json](../../../catalog.json) 查找。
2. [全量 CSV](exports/joint_states.csv)、[字段说明](exports/README.md)、[逐值校验](exports/validation.json)。CSV 一条 bag 消息一行，全部 85 列，无需 ROS 2 即可读取。
3. [原始 bag 元数据](raw/lw_real_20260930-213510/metadata.yaml)、[来源与哈希](manifest.json)、[部署资源快照](context/README.md)、[启动日志](analysis/logs/launch.log)。

bag 末帧仍有非零轮速目标，没有记录到 GetDown 收腿轨迹；不能据此否定用户在记录结束后按键。launch 日志显示 rl_real_LW 在 21:36:47.079 结束，整个 launch 于 21:36:57.376 才收到 Ctrl+C；节点日志为空，退出原因无法从保存日志判明。用户确认的失稳现象与程序退出时序应区分。

## 版本与证据限制

`lw-release-20260930-01` 标签和当前部署 manifest 指向 `03104469746402c407e54c4142ad0a8c9d8710af`，对应资源哈希均匹配。版本归属依据用户说明及现有文件，bag 没有捕获运行中的可执行文件和模型哈希；固件版本、同步视频未知。

原始数据只录制 `/LW_joint_states`，调试频率约 50 Hz，不能替代 200 Hz 控制循环、原始 IMU、FSM/安全事件、策略原始动作或电机总线报文。`*_target` 为已下发参考；`*_now` 为设备反馈。target effort 是按 RL 增益重算的 PD 估计，不是实际测得或最终下发的力矩。分析文件中的本机绝对路径按原文保留，换机器时以 manifest.json 的仓库内路径定位文件。
