# 0929-01 部分部署资源快照

用户确认使用 `lw-release-20260929-01`，对应提交 `e959d64d0ae6fb27d736cf64c96552af15ab54a5`。来源为 `/home/nvidia/rl_sar/build/lw_deployments/e959d64d0ae6/share/rl_sar/deployment/LW`。

按字节附带 manifest.yaml、policy/LW/base.yaml、policy/LW/robot_lab/wheel_loco/config.yaml 和 policy.onnx。三个资源的 SHA256 与清单一致，Wheel ONNX 为 `752b0895fed28f6816be509828810ea6d306e5ee5d1734d7125a71030379f255`。

此前分析还核对当前部署目录可执行文件及全部策略资源与清单一致，见 ../analysis/deployment_context.json。本目录不含完整可执行程序、其它全部策略或依赖，不能直接启动机器人。bag 未捕获实际运行进程身份，当前文件核验不能代替运行时二进制独立取证。固件版本、同步视频未知。
