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
    │       ├── exports/             # 全量 CSV、字段说明与逐值校验
    │       ├── context/             # 有可靠来源时保存配置、模型及部署清单快照
    │       └── analysis/            # 既有报告、指标、图表、解码数据
    └── leg/                         # 双足模式，采用相同结构
```

场次名称取原始 bag 目录时间，时区为 Asia/Shanghai；准确采样起点以 metadata.yaml 为准；原始录制缺少该文件时，以 SQLite 消息时间为准并在场次说明中注明。场次清单见 [catalog.json](catalog.json)。同场连续录制保留完整 bag，阶段范围记入说明，不为前进、后退复制两份相同数据。

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

2026-09-19 首批归档时控制代码仓库 HEAD 为 `a6e330a55ac0aef001799a9b24d1fa85d7c79f1e`；这不是那两场测试发生时版本的证明。首批未归档实际部署资源。2026-09-24、2026-09-28、2026-09-29 和 2026-09-30 场次另附用户确认的部署标识及与清单匹配的配置、模型快照；各场版本证据和限制以场次 README、manifest.json 为准。部分资源快照不能替代完整实机部署包或证明闭环可复现。

2026-10-02 两场归档另含短运动记录与运动中反复髋部振荡记录。实际加载版本未确认；第二场 context 明确标为现有部署包参考快照。第一场原始录制缺少 metadata.yaml，保留原状，未重建元数据。

2026-10-03 场次归档1003-01双轮运动改善与持续髋部偏斜记录，并附启动前人工扶稳条件、启动前后髋角度对比和长腿刚性几何估算。测试时进程文件哈希与支撑释放时刻未独立记录；本场不作为机械对齐或一般稳定性验收通过的证据。

2026-10-09 场次归档1009-01在吊绳松弛、启动后松手的自主双轮运动与双髋逐渐外偏记录。精确松手时刻和测试进程哈希未录制，短时平稳运动不等于髋姿态/受力问题解决。

2026-10-09 双足场次归档1009-01无辅助零指令站立，包含纯PD与策略接管对照、关节静差、IMU航向慢变和悬空轮响应。短时姿态平稳不代表传感器标定、姿态跟踪或步行验收通过。

## 本次归档

| 模式 | 场次 | 现场结果与范围 |
|---|---|---|
| 双轮 | [20260918-163736](experiments/wheel/20260918-163736-oscillation/README.md) | 接管后振荡，原因未确定 |
| 双轮 | [20260924-170019](experiments/wheel/20260924-170019-right-turn-instability/README.md) | 右转时左髋先振荡、随后双髋放大及机身失稳；用户主动 GetDown 后 Ctrl+C，原因未确定 |
| 双轮 | [20260928-151044](experiments/wheel/20260928-151044-turn-transition-oscillation/README.md) | 0928-01 左转后恢复前进阶段出现双髋振荡，幅度减轻但仍未稳定；后段右转前已起振，GetDown 后绳子介入 |
| 双轮 | [20260929-193808](experiments/wheel/20260929-193808-startup-oscillation-manual-support/README.md) | 0929-01 同版测试，期间人工扶持且有短暂前进指令；不作为自由运动对照 |
| 双轮 | [20260929-194212](experiments/wheel/20260929-194212-zero-command-startup-oscillation/README.md) | 0929-01 无手动触碰、全程零指令，接管后轮速与俯仰往复，GetDown 后绳子介入 |
| 双轮 | [20260930-213510](experiments/wheel/20260930-213510-hip-oscillation-body-instability/README.md) | 0930-01 前进指令回零后双髋目标快速放大、机身失稳；GetDown 未进入已保存的记录，原因尚未唯一确定 |
| 双轮 | [20261002-120757](experiments/wheel/20261002-120757-short-motion-recording/README.md) | 仅覆盖约3秒策略运动，原录制缺少metadata.yaml；不足以判断整场表现 |
| 双轮 | [20261002-121836](experiments/wheel/20261002-121836-motion-hip-oscillation-imu-stale/README.md) | 运动中两组明显双髋振荡及末段短振荡；GetDown后另发生IMU过期停机，根因未定 |
| 双轮 | [20261003-155617](experiments/wheel/20261003-155617-stable-motion-hip-bias/README.md) | 1003-01运动中未出现此前机身抖动崩溃，持续髋偏斜尤其左侧；启动前人工扶稳，机械形状与承载变形贡献待核实 |
| 双轮 | [20261009-163704](experiments/wheel/20261009-163704-autonomous-motion-hip-outward-drift/README.md) | 1009-01启动后松手自主运动，短时未复现剧烈髋抖动；双髋缓慢外偏、目标跟踪误差与报告力矩增大 |
| 双足 | [20260918-113020](experiments/leg/20260918-113020-forward-backward/README.md) | 用户确认对应前进、后退完成测试；保留末尾反馈异常与失稳分析，不标为整场稳定性验收通过 |
| 双足 | [20261009-194732](experiments/leg/20261009-194732-zero-command-standing-pd-policy/README.md) | 1009-01无辅助零指令站立平稳；膝踝承载静差、IMU航向慢变、悬空轮非零目标仍待核查 |
| 双足→双轮 | [20261010-203035](experiments/leg/20261010-203035-leg-to-wheel-jump-forward-surge/README.md) | a5736756腿转轮跳跃，落地前冲后吊绳拽住并GetDown；转换大轮速、末端姿态偏差及约8步Wheel接管，原因未唯一确定 |

## 无 ROS 2 读取全量数据

每场的 `exports/joint_states.csv` 一条消息一行，包含全部 78 个数值通道以及时间、行号和 frame_id，共 85 列。Excel、MATLAB、Python 或 PlotJuggler 可直接读取，无需 ROS 2。绘图选择 `time_s`；Excel 导入纳秒时间戳列时请选择文本类型以保留精度。

| 场次 | 全量 CSV | 行数 | 字段说明与校验 |
|---|---|---:|---|
| 双足前进、后退 | [joint_states.csv](experiments/leg/20260918-113020-forward-backward/exports/joint_states.csv) | 5491 | [字段说明](experiments/leg/20260918-113020-forward-backward/exports/README.md)、[验证结果](experiments/leg/20260918-113020-forward-backward/exports/validation.json) |
| 双轮振荡 | [joint_states.csv](experiments/wheel/20260918-163736-oscillation/exports/joint_states.csv) | 3613 | [字段说明](experiments/wheel/20260918-163736-oscillation/exports/README.md)、[验证结果](experiments/wheel/20260918-163736-oscillation/exports/validation.json) |
| 双轮右转后失稳 | [joint_states.csv](experiments/wheel/20260924-170019-right-turn-instability/exports/joint_states.csv) | 3235 | [字段说明](experiments/wheel/20260924-170019-right-turn-instability/exports/README.md)、[验证结果](experiments/wheel/20260924-170019-right-turn-instability/exports/validation.json) |
| 双轮转向后前进振荡 | [joint_states.csv](experiments/wheel/20260928-151044-turn-transition-oscillation/exports/joint_states.csv) | 3930 | [字段说明](experiments/wheel/20260928-151044-turn-transition-oscillation/exports/README.md)、[验证结果](experiments/wheel/20260928-151044-turn-transition-oscillation/exports/validation.json) |
| 双轮启动摆动（人工扶持） | [joint_states.csv](experiments/wheel/20260929-193808-startup-oscillation-manual-support/exports/joint_states.csv) | 4538 | [字段说明](experiments/wheel/20260929-193808-startup-oscillation-manual-support/exports/README.md)、[验证结果](experiments/wheel/20260929-193808-startup-oscillation-manual-support/exports/validation.json) |
| 双轮零指令启动摆动 | [joint_states.csv](experiments/wheel/20260929-194212-zero-command-startup-oscillation/exports/joint_states.csv) | 4905 | [字段说明](experiments/wheel/20260929-194212-zero-command-startup-oscillation/exports/README.md)、[验证结果](experiments/wheel/20260929-194212-zero-command-startup-oscillation/exports/validation.json) |
| 双轮前进减速后髋部失稳 | [joint_states.csv](experiments/wheel/20260930-213510-hip-oscillation-body-instability/exports/joint_states.csv) | 3508 | [字段说明](experiments/wheel/20260930-213510-hip-oscillation-body-instability/exports/README.md)、[验证结果](experiments/wheel/20260930-213510-hip-oscillation-body-instability/exports/validation.json) |
| 1002双轮短运动记录 | [joint_states.csv](experiments/wheel/20261002-120757-short-motion-recording/exports/joint_states.csv) | 2490 | [字段说明](experiments/wheel/20261002-120757-short-motion-recording/exports/README.md)、[验证结果](experiments/wheel/20261002-120757-short-motion-recording/exports/validation.json) |
| 1002双轮运动髋部振荡 | [joint_states.csv](experiments/wheel/20261002-121836-motion-hip-oscillation-imu-stale/exports/joint_states.csv) | 3533 | [字段说明](experiments/wheel/20261002-121836-motion-hip-oscillation-imu-stale/exports/README.md)、[验证结果](experiments/wheel/20261002-121836-motion-hip-oscillation-imu-stale/exports/validation.json) |
| 1003-01双轮运动与髋偏斜 | [joint_states.csv](experiments/wheel/20261003-155617-stable-motion-hip-bias/exports/joint_states.csv) | 8892 | [字段说明](experiments/wheel/20261003-155617-stable-motion-hip-bias/exports/README.md)、[验证结果](experiments/wheel/20261003-155617-stable-motion-hip-bias/exports/validation.json) |
| 1009-01自主双轮运动与髋外偏 | [joint_states.csv](experiments/wheel/20261009-163704-autonomous-motion-hip-outward-drift/exports/joint_states.csv) | 5179 | [字段说明](experiments/wheel/20261009-163704-autonomous-motion-hip-outward-drift/exports/README.md)、[验证结果](experiments/wheel/20261009-163704-autonomous-motion-hip-outward-drift/exports/validation.json) |
| 1009-01双足零指令站立 | [joint_states.csv](experiments/leg/20261009-194732-zero-command-standing-pd-policy/exports/joint_states.csv) | 4277 | [字段说明](experiments/leg/20261009-194732-zero-command-standing-pd-policy/exports/README.md)、[验证结果](experiments/leg/20261009-194732-zero-command-standing-pd-policy/exports/validation.json) |
| 腿转轮跳跃与落地前冲 | [joint_states.csv](experiments/leg/20261010-203035-leg-to-wheel-jump-forward-surge/exports/joint_states.csv) | 4055 | [字段说明](experiments/leg/20261010-203035-leg-to-wheel-jump-forward-surge/exports/README.md)、[验证结果](experiments/leg/20261010-203035-leg-to-wheel-jump-forward-surge/exports/validation.json) |

CSV 从原 bag 直接解码生成，已逐行与 bag 及既有 NPZ 交叉核对；不重采样、不插值、不滤波。bag、NPZ 和既有专题 CSV 均保留。[导出脚本](tools/export_joint_states_csv.py)的转换端需要 ROS 2，读取已导出的 CSV 不需要。
