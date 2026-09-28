# 双轮转向后前进阶段振荡（0928-01）

- 场次：`20260928-151044-turn-transition-oscillation`。
- 原始 bag：`lw_real_20260928-151044`，3930 帧，约 78.584 秒，2026-09-28 15:11:10.141–15:12:28.725（Asia/Shanghai）。
- 用户观察：最新策略下左右转仍有抖动，程度较此前减轻；双轮模式，策略运行期间完全落地、无吊绳，部署版本 0928-01。随后主动 GetDown，绳子拽住机身。
- 记录支持：明显双髋振荡先在左转后的前进阶段增长，早于后段右转约 0.66 秒；振荡持续至 GetDown 前。第一段右转和左转没有同量级的双髋振荡，不能用当前记录否定现场轻微抖动。
- 结果标签：`turn_transition_hip_oscillation_reduced_amplitude`。幅度减轻不等于稳定性验收通过，唯一根因未知。
- 用户确认部署 tag `lw-release-20260928-01`，提交 `b3b20b9bdc56d1b62b16fddc393c3abac74ca1b6`。资源快照匹配其清单；运行中二进制没有独立取证，硬件/固件版本和同步视频未知。

## 阅读入口

1. [已复核分析报告](analysis/analysis.md)、[全程曲线](analysis/overview.png)、[起振曲线](analysis/onset.png)、[归档检查和报告修复说明](analysis/archive-review.md)。
2. [全量 CSV](exports/joint_states.csv)、[字段说明](exports/README.md)、[逐值校验](exports/validation.json)。
3. [原始 bag 元数据](raw/lw_real_20260928-151044/metadata.yaml)、[文件来源与哈希](manifest.json)。
4. [部署资源快照说明](context/README.md)。

## 阶段与限制

约 61.063–62.403 秒左转；62.983 秒恢复前进；63.263 秒右髋振荡增长，随后左髋参与；63.543 秒指令回零后仍振荡；63.923 秒才出现后段右转；65.403 秒目标模式符合 GetDown。FSM 边界由轨迹推断，用户确认主动 GetDown，之后绳子介入。

报告、NPZ time_s 与 CSV time_s 均以 bag 首帧为基准；header 整数时间戳另行保留。记录约 50 Hz，不能代替 200 Hz 控制和硬件原始采样。目标角不等于反馈角，重算 PD effort 不等于实际电机输出。

09-24 对比数据已在本仓库 [上一场次](../20260924-170019-right-turn-instability/README.md) 归档。本场源 source.json 等文件的 Jetson 绝对路径按原文保留，换机器时按 manifest.json 相对路径访问。旧中文报告编码损坏的原字节副本仅作修复追溯，当前阅读以 analysis/analysis.md 为准。
