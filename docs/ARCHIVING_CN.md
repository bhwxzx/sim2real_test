# 归档规范

1. 模式使用 `wheel` 或 `leg`，场次使用 `YYYYMMDD-HHMMSS-<场景>`。一次原始录制对应一个场次，日期使用 Asia/Shanghai。
2. `raw/` 保存完整 bag 目录，保留原目录名、metadata.yaml 和全部 db3 分片；不重写、不裁剪、不对原始数据做清洗。新实验单独建目录，不覆盖旧实验。
3. `analysis/` 保存与本场次对应的已有分析。报告发生修订时保留修订说明；早期结论被后续报告修正时，在场次 README 中指出权威补充。
4. `README.md` 记录现场观察、测试目的、阶段、结果和证据限制。前进/后退有完成表现不等于整场稳定性验收通过。
5. `manifest.json` 记录归档源路径、仓库内相对路径、字节数、SHA-256 和消息数量；`catalog.json` 提供场次总索引。
6. 新增场次时尽量记录实测部署 commit、部署包标识、模型和配置哈希、硬件/固件版本、吊绳与接触状态、操作者观察、同步视频。不能核实的字段写明未知，不用归档时 HEAD 代替测试时版本。
7. 如后续确有视频，放在该场次 `media/`；有可靠配置快照则放 `context/`。仅有实际文件时建立目录，避免把当前配置冒充测试配置。
8. 当前归档采用普通 Git。未来大体积视频或长时间 bag 应先选择 Git LFS 或外部对象存储，并在仓库保留下载定位、大小和哈希；避免反复修改同一大型二进制文件。
9. 在仓库根目录更新 SHA256SUMS（不纳入 .git 和校验文件自身），运行 `sha256sum -c SHA256SUMS` 及 `git diff --check`，检查本次暂存文件后提交。
10. 读取 metadata.yaml / SQLite 或 `ros2 bag info` 即可检查归档。数据回放与硬件运行是独立任务，归档不表示已做新的实机验收。

11. 每场提供一份 `exports/joint_states.csv`，覆盖全部已录制消息与数值通道。保留时间戳和原始数值，不插值、重采样、滤波或手工编辑。字段说明放 `exports/README.md`，逐值校验结果放 `exports/validation.json`，并在 manifest.json 的 derived_exports 登记派生文件哈希。
12. 原 bag 为原始依据，CSV 为通用读取入口，NPZ 为可选的 Python 分析副本；现有 NPZ 和专题 CSV 保留。再导出使用 `tools/export_joint_states_csv.py` 并选择新的输出路径，核验后再决定是否替换旧导出。
