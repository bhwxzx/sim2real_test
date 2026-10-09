# 1009-01 资源与几何快照

用户确认本场使用 1009-01。标签 lw-release-20261009-01 与现存部署 manifest 均对应 8cd9a7cef928e29c534cc459552bd5a5590102ae。bundle_snapshot 保存 manifest、基础配置、Wheel 配置与 ONNX，已逐项核对清单哈希；现存程序哈希也已核对。详细证据见 ../analysis/deployment-provenance.json。

本场 bag 没有独立记录测试时进程路径、程序或模型哈希。此处为部分资源快照，不含完整程序、运行库、其他模式模型或硬件固件，不能替代完整部署包或证明闭环可复现。

geometry/LW.urdf 为本次分析使用的代码仓库几何文件，用于刚性模型估算。它不证明实物机械零位、承载形变或训练 USD 与模型一致。来源与哈希见 ../manifest.json。
