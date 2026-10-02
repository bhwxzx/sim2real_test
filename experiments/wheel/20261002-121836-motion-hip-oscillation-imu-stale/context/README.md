# 部署包参考快照：测试时使用情况未确认

这些文件逐字节复制自现有 /home/nvidia/rl_sar/build/lw_deployments/2e74c528fb86/share/rl_sar/deployment/LW/，仅作为本次分析所用的参考版本背景。

- 包清单 source_commit：2e74c528fb8639ecdb1695160cefa7105f8b2a1e。
- Wheel模型 SHA-256：1bf82546c08e2f7e3eb28df9ab6f54244e7d8b72aa6bbf11cf6a02a4209a482a。
- Wheel配置 SHA-256：22e753d7199ca4deed79570ba116e2fec5e32e79355f7b589063c39d7fb15e92。
- 已核对 base.yaml、Wheel config.yaml、Wheel policy.onnx 与该包manifest记录的哈希一致。
- 用户没有明确确认本次所加载的部署标识；bag也不包含运行中的二进制/模型路径或哈希。因此 test_time_use_verified=false，不把参考包提交号写作已确认测试版本。
- 此目录只是manifest、基础配置、Wheel配置和模型的部分快照，不是完整可运行部署包，也没有进行新的构建或硬件验收。
