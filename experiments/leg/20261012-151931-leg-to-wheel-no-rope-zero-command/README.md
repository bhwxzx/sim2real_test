# 第一轮：无吊绳、零指令腿转轮

## 现场与效果

用户确认流程与前次相同，策略测试期间无吊绳干扰；切换后轮子着地、脚板离地；没有非预期前冲，最后主动GetDown并倾倒放置到地面。

本轮全程x/y/yaw严格为零。LegToWheel约3.4秒/170组采样目标，Wheel约4.919967秒/246组不同采样目标。没有推理计数器，不能把采样数写成绝对精确策略步数。

转换末端脚踝约+4.78°/+3.92°，轮速近零，接管目标跳变约6°/6°，衔接较好。

较大q_target−q_actual是PD产生力矩的控制误差，不能单凭该量判定运动跟踪差；统计值保留，但评估解释已修订。GetDown后的大俯仰按用户确认的退出/放地过程处理。

## 报告与数据

- [分轮评估（可浏览副本）](analysis/archive-view.md)；[分析原文](analysis/assessment.md)字节不变。
- [两轮对照与PD语义修订](../../../docs/reports/20261012-leg-to-wheel-no-rope/README.md)。
- 原bag：lw_real_20261012-151931，8195帧，163.862752秒；Asia/Shanghai时间2026-10-12T15:19:46.176662+08:00—2026-10-12T15:22:30.039415+08:00。
- 原始db3 SHA-256：6d4f88a3cb7831fbfa8af70620df1c6fdeb914eca0039d6a43d96e701e5f0bc2。
- 完整metadata.yaml、db3、NPZ、指标、三张图及启动/控制/IMU/录包日志均保留。日志不含完整终端stdout。
- [全量CSV](exports/joint_states.csv)：8195行、85列；与bag及NPZ逐值位模式一致，不重采样/滤波。[字段说明](exports/README.md)、[校验结果](exports/validation.json)。
- [版本证据](context/README.md)：当前参考包不冒充实测版本；实测source_commit未知。
- 源路径、副本大小和哈希见[manifest.json](manifest.json)。

原始记录和已有归档保持；短时成功不作为长期稳定性、跳高/冲击或运动速度跟踪的完整验收。
