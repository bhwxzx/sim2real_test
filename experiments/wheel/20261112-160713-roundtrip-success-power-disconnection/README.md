# 2026-11-12 160713：成功往返及电源线脱落倾倒

第一次轮切足、足切轮成功；随后第二次轮切足时倾倒，用户后续确认电机电源线脱落。右小腿三项反馈冻结先于明显侧倾，旧反馈持续传播机制仍待定位；该段归类为硬件电源连接故障条件下的事件，不直接计为策略自身失败。

- 原始 bag `lw_real_20261112-160713`：2182 帧，43.619708 秒。
- 阶段摘要：W2L 3.40 秒 → Leg 1.60 秒 → L2W 3.40 秒 → Wheel 4.24 秒 → 第二次 W2L 约 2.26 秒后进入 GetDown。
- 吊绳松弛、无人扶持（用户确认）；精确落地接触、实际位移和同步视频未独立记录。
- 版本依据和限制见 [context](context/README.md)。
- 原始 bag 全量保留，不裁剪、不去重；metadata.yaml 已存在并核验。
- 本次未重新解码数值载荷或重新评估；CSV 复用既有 NPZ，原始消息头另行读取校验。

优先阅读 [现场确认及修订说明](analysis/operator-confirmation.md)。

[最新完整报告](analysis/assessment-updated.md) · [分析时原始报告](analysis/assessment.md) · [今日三场总览](../../../docs/reports/20261112-1112-01-transitions/README.md)

[全量 CSV](exports/joint_states.csv) · [字段说明](exports/README.md) · [逐值校验](exports/validation.json) · [归档清单](manifest.json)

历史报告中的源绝对路径和“未归档/未提交”操作状态按原文保留；当前归档事实以本说明、修订报告和 Git 历史为准。此前昨日较早 bag 不归档的要求保持不变。
