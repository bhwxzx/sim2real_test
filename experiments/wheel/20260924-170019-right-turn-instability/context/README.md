# 部署资源快照

用户确认本次运行 `/home/nvidia/rl_sar/build/lw_deployments/a70e25bbbad0`，对应提交 `a70e25bbbad014621a9ad1b4e7f15dfa45555f6d`。

本目录按字节保存该部署的 `manifest.yaml`，以及：

- `policy/LW/base.yaml`
- `policy/LW/robot_lab/wheel_loco/config.yaml`
- `policy/LW/robot_lab/wheel_loco/policy.onnx`

三个资源的 SHA-256 均与部署清单匹配。Wheel ONNX SHA-256 为 `33de9e0f5b6fc6ec8365cd323265bd3ea363330b5a867f8c37579455faefb75a`；核对记录也见 `../analysis/deployment_context.json`。

这是部分资源快照，不是完整可执行部署包。清单还列出了本目录未附带的可执行文件、依赖库及其它策略，不能直接对本目录执行完整部署验收或启动实机。实际运行二进制没有独立取证；部署身份来自用户确认，资源完整性来自清单核对。固件版本和同步视频未取得。
