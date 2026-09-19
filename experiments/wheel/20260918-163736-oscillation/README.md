# 双轮模式接管后振荡

- 原始 bag：`lw_real_20260918-163736`。
- 数据：3613 条 `/LW_joint_states` 消息，约 72.244 秒。
- 现场观察：进入 wheel_loco 后立即抖动；轮子落地承重、吊绳松弛（既有分析记录的用户确认）。
- 结果：双轮闭环振荡，根因未确定。
- 约 64.003 秒策略接管，约 64.583 秒进入推断的 getdown；相对第一条消息计时，FSM 边界为离线推断。

## 阅读顺序

1. [事件分析](analysis/wheel_loco_incident_review.md)
2. [振荡起点复核](analysis/oscillation_onset_review.md)
3. [摩擦补偿重构](analysis/friction_reconstruction_review.md)
4. [文件来源与哈希](manifest.json)

原始 bag 位于 `raw/lw_real_20260918-163736/`。分析中的绝对路径与旧代码描述是当时记录，保留原文；例如其对策略入口保护的描述不代表后续 LW-080 修改后的当前实现。

离线模型输出重现不等于训练部署契约完全一致，也不等于确定唯一振荡原因。重构的力矩需求与设备报告力矩应区分。实际测试所用部署包、配置与模型快照未在本次核验或归档。

## 全量 CSV

[exports/joint_states.csv](exports/joint_states.csv) 提供本场全部消息和数值字段，无需 ROS 2 即可读取。列含义和单位见 [exports/README.md](exports/README.md)，与原始 bag、既有 NPZ 的逐值比对结果见 [exports/validation.json](exports/validation.json)。
