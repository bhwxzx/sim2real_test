# 版本与参考证据

当前源码HEAD及参考部署包为a5736756b397，但本轮没有完整模型加载stdout或测试进程文件捕获。实测source_commit保持null，不使用归档时HEAD替代。

两轮共用当前参考快照，包含base/Leg/LegToWheel/Wheel资源及动作CSV，用于说明参考轨迹与PD语义，不作为实测资源的独立证明。

- [当前参考资源](../../../../docs/reports/20261012-leg-to-wheel-no-rope/context-reference/README.md)
- [参考校验与证据限制](../../../../docs/reports/20261012-leg-to-wheel-no-rope/deployment-reference.json)

缺少接触、吊绳/外力时刻、机身位置/线速度及精确策略frame记录。现场条件来自用户确认，证据边界在总报告说明。
