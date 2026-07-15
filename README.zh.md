<div align="center">
  <h1>研究点子快速筛选</h1>
  <p><strong>快速评估早期研究点子——低成本、系统化、诚实透明。</strong></p>

  <p>
    <strong>中文</strong> &nbsp;|&nbsp;
    <a href="README.md">English</a>
  </p>

  <p>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
    <a href="https://python.org"><img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python 3.10+"></a>
    <a href="#"><img src="https://img.shields.io/badge/status-stable-brightgreen" alt="Status: Stable"></a>
  </p>
</div>

---

## 为什么要做研究点子筛选？

每个研究者都经历过这样的场景：你想到一个令人兴奋的研究点子，花了几周读文献、设计实验，结果发现别人已经发表过了，或者问题远比想象中复杂。

**Research Idea Screening** 是一个轻量级、有原则的工作流，帮助你**在投入大量时间、资金或精力之前**，判断哪些早期点子值得深入探索。

它的设计原则是：

- **低成本**：一次快速筛选约需 30 分钟，有明确的搜索预算限制。
- **诚实透明**：暴露不确定性而非掩盖它，绝不将"没快速找到"等同于"没人研究过"。
- **可操作**：每次筛选输出具体建议——推进、先探索、搁置或拒绝——以及解决剩余不确定性的最便宜路径。

---

## 核心功能

| 功能 | 说明 |
|---|---|
| **有界新颖性搜索** | 覆盖精确词、同义词、旧术语、相邻领域和反假设的六族查询 |
| **硬性门控过滤** | 四个门控（重要性、可回答性、资源路径、伦理/治理）——任一失败即拒绝 |
| **加权评分** | 六维度 1-5 分制，带置信区间和决策敏感性分析 |
| **事前分析** | 在投入前识别最大风险、最早预警信号、停止规则和挽救路径 |
| **批量比较** | 在同一研究画像和筛选预算下比较多个点子，带置信度感知排名 |
| **通俗易懂的输出** | 结论以日常语言呈现，不暴露内部评分机制 |

---

## 工作流程

```
输入点子
    │
    ▼
点子标准化 — 目标、机制、比较对象、预期结果、贡献类型
    │
    ▼
有界新颖性搜索 — 6 族查询，确定最相关工作
    │
    ▼
硬性门控 — 重要性、可回答性、资源路径、伦理/治理
    │
    ├── 任一"否" ──────────► 拒绝
    ├── 任一"未知" ────────► 先探索（设计最便宜的检验方案）
    │
    ▼
评分（仅通过门控的候选）
    │
    ├── 重要性（25%）
    ├── 差异化（20%）
    ├── 可行性（15%）
    ├── 验证清晰度（15%）
    ├── 成本效率（15%）
    └── 失败残值（10%）
    │
    ▼
事前分析 — 失败风险、预警信号、停止规则
    │
    ▼
决策 — 推进 / 先探索 / 搁置 / 拒绝
    │
    ▼
报告 — 通俗语言总结 + YAML 交接给 research-ideation
```

### 筛选模式

- **单个（single）** — 深入评估一个点子。
- **批量（batch）** — 在同一研究画像和筛选预算下比较多点子。
- **刷新（refresh）** — 新证据出现时重新评估之前的结果。

---

## 评分维度

所有维度按 1-5 分（0.5 递增）评分，必须附带置信度：

| 维度 | 权重 | 衡量什么 |
|---|---|---|
| **重要性** | 25% | 答案对可信的利益相关者、理论或决策能改变什么吗？ |
| **差异化** | 20% | 这个点子与最强的已有工作有多大区别？ |
| **可行性** | 15% | 是否存在可信的技术或资源路径来完成它？ |
| **验证清晰度** | 15% | 能否明确判断成功或失败？ |
| **成本效率** | 15% | 预期的洞见或影响是否值得投入？ |
| **失败残值** | 10% | 如果失败，是否有可复用的产出（数据、阴性结果、工具、基准）？ |

### 硬性门控（评分前必须检查）

| 门控 | 失败条件 |
|---|---|
| 重要性 | 没有可识别的受益者或影响 |
| 可回答性 | 没有可观测的结果能裁决该主张 |
| 资源路径 | 关键前提条件没有可信的替代方案 |
| 伦理/治理 | 风险不可接受或审批申请不现实 |

---

## 决策解读

| 筛选结果 | 含义 |
|---|---|
| **推进（Proceed）** | 值得深入评估，继续做更详细的可行性验证 |
| **先探索（Probe first）** | 还不够确定；先做个小型快速测试 |
| **搁置（Park）** | 当前不值得做；条件变化后可以重新考虑 |
| **拒绝（Reject）** | 存在根本性问题——建议放弃 |

**决策语言规则**：所有结论必须用日常语言表达，不暴露内部评分概念（如"区间""阈值""灵敏度"）。

---

## 快速上手

### 环境要求

- Python 3.10+
- Git

### 获取工作流

```bash
git clone https://github.com/zhonxia/research-idea-screening.git
cd research-idea-screening
```

### 使用评分脚本

```bash
# 查看期望的输入格式
python scripts/score_screening.py --example

# 从 JSON 文件评分一个点子
python scripts/score_screening.py my_screen.json

# 批量评分
python scripts/score_screening.py batch_screens.json
```

### 输入格式

```json
{
  "title": "我的研究点子",
  "gates": {
    "significance": "yes",
    "answerability": "yes",
    "resource_path": "yes",
    "ethics_governance": "yes"
  },
  "dimensions": {
    "significance": {"score": 4.0, "confidence": "high"},
    "differentiation": {"score": 3.5, "confidence": "medium"},
    "feasibility": {"score": 3.0, "confidence": "medium"},
    "validation_clarity": {"score": 3.5, "confidence": "high"},
    "cost_efficiency": {"score": 3.0, "confidence": "low"},
    "failure_residual": {"score": 2.5, "confidence": "medium"}
  },
  "fatal_risk": false
}
```

脚本返回确定性推荐、加权分数、基于置信度的分数范围，以及 `decision_sensitive` 标记。

### 运行测试

```bash
python -m unittest tests/test_score_screening.py
```

---

## 项目结构

```
research-idea-screening/
├── SKILL.md                         # 完整筛选工作流规范（中文）
├── README.md                        # 英文文档
├── README.zh.md                     # 本文档
├── LICENSE                          # MIT 许可证
├── agents/
│   └── openai.yaml                  # AI Agent 接口定义
├── assets/
│   └── rapid-screen-report.md       # 筛选报告模板（YAML 头部 + Markdown）
├── references/
│   ├── screening-protocol.md        # 详细筛选协议（门控、评分、风险分析）
│   └── research-profiles.md         # 研究画像类型，确保公平评估
├── scripts/
│   └── score_screening.py           # 确定性评分脚本
└── tests/
    └── test_score_screening.py      # 评分脚本的单元测试
```

---

## 相关项目

本项目是研究构思生态的一部分：

- **[research-ideation](https://github.com/zhonxia/research-ideation)** — 研究点子的全生命周期管理：生成、正式评估、新颖性验证、组合追踪。这是**上游流程**——通过筛选的点子可以在此做深入评估。
- **[personal-literature-survey](https://github.com/zhonxia/personal-literature-survey)** — 系统化文献调研工作流，结合学术数据库和个人知识库。与点子筛选**并行运行**，为新颖性和可行性检查提供证据。

### 三者的关系

```
research-ideation（生成研究点子）
       │
       ▼
research-idea-screening（快速筛选 ← 你在这里）
       │
       ├── 推进 ──► research-ideation（正式评估）
       ├── 先探索 ──► 低成本实验，然后重新筛选
       ├── 搁置 ──► 回到点子池
       └── 拒绝 ──► 记录原因，继续前进
       
       │
       ▼
personal-literature-survey（证据收集——与筛选并行运行）
```

---

## 不可协商的规则

1. 永远不要将"没快速找到"等同于"没人研究过"。
2. 区分问题的重要性和论文的吸引力。
3. 在加权评分之前先应用门控。
4. 可行性评估必须包含时间、资金、访问权限、专业知识、许可和机会成本。
5. 定义拟贡献如何被证伪、有界化或实质性修正。
6. 与**最强相关的基线**比较，而非方便的弱基线。
7. 保留负面和反面证据。
8. 报告置信度和决策敏感性，而非仅仅一个点分数。
9. 仅在存在可信路径时，才将可复用的数据、代码、工具、负面发现、边界结果和文献图谱视为可能的失败残值。
10. 优先选择最能改变决策的最便宜探测方案。

---

## 使用建议

### 适合什么场景？

- 你有一个新的研究想法，想快速判断是否值得投入
- 你有多个备选方向，需要决定先做哪个
- 你有个积压的点子列表，需要系统性地梳理
- 你在写基金申请书或研究计划，需要排除明显不可行的方向
- 你是导师/团队领导，需要快速评估学生的提议方向

### 不适合什么场景？

- **需要完整新颖性证明**：本工作流只做有界搜索，不执行引用链饱和或系统性综述
- **需要正式的研究评估**：通过筛选后，应使用 `research-ideation` 进行完整评估
- **需要替代系统性文献综述**：应配合 `personal-literature-survey` 或专业文献数据库（Web of Science、Scopus）

---

## 许可

MIT © 2026 Wang Xu。详见 [LICENSE](LICENSE)。
