# 2026-11-12：1112-01 三场实测归档

本次仅归档已完成分析的三份完整 bag，合计 **6226 帧**。原 bag、既有分析、图表、解码数据与日志逐文件核对 SHA-256 后复制；没有重复解码数值载荷或重做评估。三场均有原始 metadata.yaml；16:27 的元数据是用户关闭录制后实际生成，数据库哈希未变。

| bag 时间标识 | 消息数 | 结果及范围 | 最新报告 |
|---|---:|---|---|
| [154546](../../../experiments/wheel/20261112-154546-wheel-to-leg-success-zero-command/README.md) | 1946 | 全程零指令，轮切足约 3.40 秒完成，双足运行约 11.18 秒；接管初期约 1 秒调整后收敛。接管 2 秒后约 9.16 秒较安静站立。 | [报告](../../../experiments/wheel/20261112-154546-wheel-to-leg-success-zero-command/analysis/assessment-updated.md) |
| [160713](../../../experiments/wheel/20261112-160713-roundtrip-success-power-disconnection/README.md) | 2182 | 第一次轮切足、足切轮成功；随后第二次轮切足时倾倒，用户后续确认电机电源线脱落。右小腿三项反馈冻结先于明显侧倾，旧反馈持续传播机制仍待定位；该段归类为硬件电源连接故障条件下的事件，不直接计为策略自身失败。 | [报告](../../../experiments/wheel/20261112-160713-roundtrip-success-power-disconnection/analysis/assessment-updated.md) |
| [162712](../../../experiments/wheel/20261112-162712-bidirectional-transition-success/README.md) | 2098 | 轮切足、足切轮均成功，返回双轮后继续运行约 5.14 秒；双足阶段仅约 1.04 秒。录制程序关闭后 metadata.yaml 已实际生成并核对，数据库哈希未变。 | [报告](../../../experiments/wheel/20261112-162712-bidirectional-transition-success/analysis/assessment-updated.md) |

## 16:08 后续现场确认

用户明确补充“是电机电源线掉了”。该 bag 包含一次成功往返，以及随后电源连接故障条件下的第二次轮切足倾倒。原始报告保留；更新版报告、场次索引和 operator-confirmation.json 采用这一现场事实。右小腿三项反馈在明显侧倾前冻结的证据仍保留，旧反馈持续传播的具体层级及保护行为尚未定位。用户未进一步指定具体电机/接头身份。

所选三份记录共 3 次 W2L 成功、2 次 L2W 成功，以及 1 次电源线脱落条件下的 W2L 倾倒；这不是当天全量试验或严格重复试验，不据此估计策略成功率。

## 复用与版本边界

[共享部署资源快照](context-reference/README.md) 仅保存一份 1112-01 配置、模型、参考轨迹和 manifest。16:08 launch 日志记录包内可执行路径；另两场由用户确认版本。所有场次均缺少测试进程模型哈希的独立捕获。当前资源核验不等于完整闭环复现。

15:46 全程零指令、双足运行约 11.18 秒；16:08 与 16:27 包含双轮速度操作。PD 位置误差或力矩大小本身不是故障判据。此前 11 月 11 日分析和历史试验直接引用原归档，不再复制较早 bag。

## 导出与校验

每场 CSV 为 85 列，覆盖全部 78 个数值通道及消息头/时间。数值来自已分析 NPZ，逐值按 float64 位模式校验，保留负零；仅读取 bag 时间与 CDR Header 核对元信息，没有重复数值解码、滤波、插值或去重。各场 validation.json 明确区分 NPZ 数值核对和原 bag 头部核对。原 bag 仍为原始依据。

根目录 SHA256SUMS 覆盖全部归档文件；旧报告保留当时的绝对路径、版本限制和操作状态，最新补充以各场更新版报告为准。
