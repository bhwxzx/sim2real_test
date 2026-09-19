# sim2real_test

LW 机器人实机测试数据与离线分析归档。按模式和测试场次保存原始 ROS 2 bag、既有分析与证据，不替代控制代码仓库。

## 目录规划

```text
sim2real_test/
├── README.md
├── catalog.json                     # 场次索引、结果及限制
├── SHA256SUMS                       # 归档文件完整性校验
├── docs/
│   └── ARCHIVING_CN.md               # 命名、归档和新增场次规范
├── templates/
│   └── EXPERIMENT_README.md          # 新场次说明模板
└── experiments/
    ├── wheel/                       # 双轮模式
    │   └── YYYYMMDD-HHMMSS-<场景>/
    │       ├── README.md
    │       ├── manifest.json        # 原路径、大小和 SHA-256
    │       ├── raw/<原始bag目录>/    # metadata.yaml 与全部 db3 分片
    │       └── analysis/            # 既有报告、指标、图表、解码数据
    └── leg/                         # 双足模式，采用相同结构
```

场次名称取原始 bag 目录时间，时区为 Asia/Shanghai；准确采样起点以 metadata.yaml 为准。场次清单见 [catalog.json](catalog.json)。同场连续录制保留完整 bag，阶段范围记入说明，不为前进、后退复制两份相同数据。

## 使用

```bash
git clone https://github.com/bhwxzx/sim2real_test.git
cd sim2real_test
sha256sum -c SHA256SUMS
# 加载 ROS 2 Humble 后检查某场次的 raw/<bag目录>：
# ros2 bag info experiments/<模式>/<场次>/raw/<bag目录>
```

现有数据仅含 `/LW_joint_states`（sensor_msgs/msg/JointState）。FSM、实际机身位移/速度、硬件总线原始帧等未被直接录制；各分析报告的推断边界应一并阅读。

原始数据来自 Jetson 的 `/home/nvidia/debug_bags/`，分析来自 `/home/nvidia/rl_sar/build/lw_diagnostics/`。源文件保持原样，逐文件校验后复制。历史报告和 source.json 中的绝对路径按原文保留，换机器时使用 manifest.json 的仓库内相对路径。

归档时控制代码仓库 HEAD 为 `a6e330a55ac0aef001799a9b24d1fa85d7c79f1e`；这不是测试发生时版本的证明。本次未归档或验证实际运行的部署包、模型和配置快照，不能仅凭这些数据完整复现实机闭环。

## 本次归档

| 模式 | 场次 | 现场结果与范围 |
|---|---|---|
| 双轮 | [20260918-163736](experiments/wheel/20260918-163736-oscillation/README.md) | 接管后振荡，原因未确定 |
| 双足 | [20260918-113020](experiments/leg/20260918-113020-forward-backward/README.md) | 用户确认对应前进、后退完成测试；保留末尾反馈异常与失稳分析，不标为整场稳定性验收通过 |
