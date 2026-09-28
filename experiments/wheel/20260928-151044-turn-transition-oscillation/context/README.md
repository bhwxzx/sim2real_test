# 部署资源快照

用户确认测试使用 `lw-release-20260928-01`，对应提交 `b3b20b9bdc56d1b62b16fddc393c3abac74ca1b6`。快照来源为 `/home/nvidia/rl_sar/build/lw_deployments/b3b20b9bdc56/share/rl_sar/deployment/LW`。

按原字节保存 manifest.yaml、policy/LW/base.yaml、policy/LW/robot_lab/wheel_loco/config.yaml 和 policy.onnx。三个资源均匹配部署清单；Wheel ONNX SHA256 为 `33aea9901317a597c72688a233a3c8c22516295ea87966e61bb7701762a9d7c3`。

分析时还核对了当前部署目录的可执行文件和全部策略资源，其哈希均匹配清单，见 ../analysis/deployment_context.json；本归档仅保存上述部分资源。bag 没有捕获运行中的程序身份或二进制哈希，不能把当前文件核验视为运行时独立取证。

这是部分资源快照，不是完整可执行部署包。清单所列其它策略、可执行文件和依赖并未全部附带，不能直接启动实机或执行完整部署验收。硬件/固件版本及同步视频未知。
