# 1002 双轮短时运动记录（覆盖不足）

- 场次 ID：20261002-120757-short-motion-recording。
- 原始 bag：lw_real_20261002-120757，共 2490 帧；实际消息范围 2026-10-02 12:08:44.104—12:09:33.883，Asia/Shanghai，约 49.779 秒。
- 用户确认当天两次测试为双轮模式、完全落地，抖动发生在运动过程中；人工扶持和吊绳是否受力未单独确认。
- 约相对 46.759 秒开始出现非零轮速目标，已保存的策略相关运动仅约 3.02 秒。该片段未出现第二次那样的强烈双髋振荡，但不能推断此后运动表现。
- 结果：short_motion_recording_insufficient_coverage；不作稳定性验收结论。

## 数据入口

- [全量 CSV](exports/joint_states.csv)、[字段说明](exports/README.md)、[逐值校验](exports/validation.json)。
- [短运动段曲线](analysis/120757-motion.png)、[解码数据](analysis/decoded.npz)、[来源](analysis/source.json)。
- [原始 SQLite](raw/lw_real_20261002-120757/lw_real_20261002-120757_0.db3)、[文件清单与哈希](manifest.json)、[启动日志](analysis/logs/launch.log)。
- [两次记录的联合分析](../20261002-121836-motion-hip-oscillation-imu-stale/analysis/analysis.txt)。

## 原始录制与版本限制

原目录没有 metadata.yaml，本归档原样保留，没有重建元数据或裁剪数据库。SQLite quick_check=ok，CSV直接读取全部已保存消息；不能由数据库可读推断原录制正常结束。使用本仓库现有导出工具可直接读取 db3；普通 ros2 bag info 可能因缺少元数据不可用。

启动日志仅包含进程启动，节点与录包日志为空，无法判明此场如何结束。后续 IMU 过期故障由用户明确归属第二次运行，不能迁移到本场。

实际加载的部署版本、模型与固件未独立记录；第二场保留的[部署包参考快照](../20261002-121836-motion-hip-oscillation-imu-stale/context/README.md)不是本场测试版本证明。
