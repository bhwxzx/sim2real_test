# 0930-01 部分部署资源快照

用户确认使用 `lw-release-20260930-01`，标签指向提交 `03104469746402c407e54c4142ad0a8c9d8710af`。来源为 `/home/nvidia/rl_sar/build/lw_deployments/031044697464/share/rl_sar/deployment/LW`。

按字节附带 manifest.yaml、policy/LW/base.yaml、policy/LW/robot_lab/wheel_loco/config.yaml 和 policy.onnx。资源的 SHA-256 与清单一致，Wheel ONNX 为 `646bed9a1a67082f56681c704e40425d9ca3d4b70cd71042da35386eaf86ad22`。部署目录中的可执行文件哈希亦与 manifest 一致；可执行文件本身没有复制到本数据仓库。

相较 0929-01，本场 Wheel config.yaml 按字节相同，Wheel ONNX 不同。这里的文件仅是部分快照，不能直接启动机器人；bag 未捕获运行中进程的二进制身份，用户的版本说明和当前部署文件核验不能替代运行时独立取证。固件版本、同步视频未知。
