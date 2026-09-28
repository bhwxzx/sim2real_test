# 归档检查与报告修复记录（2026-09-28）

原分析报告因 Windows PowerShell 向 SSH 传递文本时的编码问题，中文被替换为字面问号：正文中文字符数为 0，问号共 2389 个。原文件没有覆盖，按字节归档为 original-report-encoding-error.md；来源、大小和 SHA256 登记在 manifest.json。

当前 analysis.md 使用 UTF-8 重建，恢复了此前分析的关键证据和限制。进一步明确 control.x/y/yaw 是控制输入而非实测速度，事件时间定位受约 20 ms 调试采样限制。报告采用重新检查的指标，没有改写原 bag、NPZ、metrics.json 或图表。

已核对原 bag SHA256、SQLite 完整性、metadata 与数据库/NPZ 的 3930 帧及起止时间；重算核对 12 个窗口的髋目标角、反馈角、速度、上报 effort 和重算 PD 峰值。派生欧拉角与四元数重算一致。

导出使用仓库既有 tools/export_joint_states_csv.py。CSV 的每条消息、时间戳、frame_id 和 78 个数值通道与原 bag、decoded.npz 逐值复核，保留 float64 位模式与负零；详细结果见 ../exports/validation.json。原始 bag 和全部来源副本逐文件哈希一致。

未修改控制源码、配置、模型或现有实验，未启动机器人。本记录是离线检查证据，不是新的稳定性或硬件验收。
