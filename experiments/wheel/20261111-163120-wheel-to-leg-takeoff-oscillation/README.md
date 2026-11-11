# 2026-11-11 Wheel-to-Leg 起跳抖动

最新 bag 163120：轮转腿在起跳阶段双髋快速振荡，过渡运动明显失稳；操作者随后用吊绳拉住，再主动 GetDown。未完成轮转腿转换，不能作为双足接管或站立验收通过。

- 原始消息 1410 帧，28.187821 秒，Asia/Shanghai 16:31:33.873379–16:32:02.061199；50 Hz /LW_joint_states。
- 推断 Wheel-to-Leg 从 16:31:54.979 开始，16:31:57.160 进入 GetDown，约 2.180728 秒、109 条遥测目标样本。没有内部 FSM/推理计数，不能称精确 109 次推理。
- 早期双髋目标、实际运动及力矩反馈出现约 9–10 Hz 振荡。与旧 Wheel 的 8–9 Hz 现象存在共同闭环机制线索，具体根因尚未唯一确定。
- 用户报告全程零运动指令；转换段 x/y/yaw 确实为零，但之前 Wheel 阶段有两段短 yaw 输入。两种证据均保留，未擅自认定输入原因。
- 吊绳受力的精确时刻、足端接触、实际机身平移、完整策略观测和实际下发增益未记录；后段可能含保护拉绳外力。
- 当前包仅作参考；测试时版本/二进制未独立验证，详见 context。
- 同日较早 161746 准备记录按用户要求不归档。历史 L2W/Wheel 数据直接引用已有场次，不重复复制。
- PD 目标差用于产生力矩；本报告依据交变输出和真实振荡评价异常，不把目标差大小本身判为故障。

[完整评估与 L2W 对照](../../../docs/reports/20261111-wheel-to-leg-takeoff-oscillation/README.md) · [历史双轮抖动共同机制](../../../docs/reports/20261111-wheel-to-leg-takeoff-oscillation/shared-hip-oscillation-review-archive.md)

原始 bag：raw/lw_real_20261111-163120/。全量 [CSV](exports/joint_states.csv)、[字段说明](exports/README.md)、[逐值校验](exports/validation.json)。现存日志和完整解码保存在 analysis/；[源数据清单](manifest.json)。
