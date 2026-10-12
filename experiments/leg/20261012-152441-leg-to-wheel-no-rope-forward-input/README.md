# 第二轮：无吊绳、含主动前进输入腿转轮

## 现场与效果

用户确认流程与前次相同，策略测试期间无吊绳干扰；切换后轮子着地、脚板离地；没有非预期前冲，最后主动GetDown并倾倒放置到地面。

本轮有两段主动前进输入，最大原始control.x约0.303，侧向/转向为零。LegToWheel约3.4秒/170组采样目标，Wheel约8.065611秒/403组不同采样目标。没有推理计数器，不能把采样数写成绝对精确策略步数。

转换末端右脚踝约+24.10°，接管目标跳变约31°/10°，仍有较大单侧瞬态；后段恢复到较小脚踝角站姿。

较大q_target−q_actual是PD产生力矩的控制误差，不能单凭该量判定运动跟踪差；统计值保留，但评估解释已修订。GetDown后的大俯仰按用户确认的退出/放地过程处理。

## 报告与数据

- [分轮评估（可浏览副本）](analysis/archive-view.md)；[分析原文](analysis/assessment.md)字节不变。
- [两轮对照与PD语义修订](../../../docs/reports/20261012-leg-to-wheel-no-rope/README.md)。
- 原bag：lw_real_20261012-152441，4443帧，88.870650秒；Asia/Shanghai时间2026-10-12T15:25:20.492625+08:00—2026-10-12T15:26:49.363275+08:00。
- 原始db3 SHA-256：65ad6d55595343ac5743e26b5910382a084a65d7f975bb728aab544464a549d3。
- 完整metadata.yaml、db3、NPZ、指标、三张图及启动/控制/IMU/录包日志均保留。日志不含完整终端stdout。
- [全量CSV](exports/joint_states.csv)：4443行、85列；与bag及NPZ逐值位模式一致，不重采样/滤波。[字段说明](exports/README.md)、[校验结果](exports/validation.json)。
- [版本证据](context/README.md)：当前参考包不冒充实测版本；实测source_commit未知。
- 源路径、副本大小和哈希见[manifest.json](manifest.json)。

原始记录和已有归档保持；短时成功不作为长期稳定性、跳高/冲击或运动速度跟踪的完整验收。
