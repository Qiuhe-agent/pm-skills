# 基于AI大模型的故障诊断与根因分析落地实现
发布时间：2025-12-05  
发布于：浙江  
来源：阿里云开发者  

## 简介
本项目基于Dify平台构建多智能体协作的AIOps故障诊断系统，融合指标、日志、链路等多源数据，通过ReAct模式实现自动化根因分析（RCA），结合MCP工具调用与分层工作流，在钉钉/企业微信中以交互式报告辅助运维，显著降低MTTD/MTTR。

## 一、项目背景概述
当前，企业数字化转型进入深水区，业务系统的复杂性呈指数级增长。微服务、容器化、云原生架构成为主流，这虽然带来了敏捷性和弹性，但也让系统内部的依赖关系变得空前复杂。一个简单的用户请求可能穿越几十个甚至上百个服务，产生的监控指标、日志、链路数据量浩如烟海。

在此背景下，AIOps从一种“锦上添花”的探索转变为“雪中送炭”的必需品。该项目是AIOps在故障智能诊断这一核心场景下的前沿实践。

### 项目核心目标
构建一个基于多智能体协作的AI系统，模拟人类专家团队的协作模式，对IT系统中发生的故障进行自动化、智能化的根因分析（RCA），并通过企业微信等日常办公协作平台将分析过程和结论以交互式、易于理解的形式推送给运维工程师，最终实现平均故障发现时间（MTTD）和平均故障修复时间（MTTR）的大幅降低。

### 系统工作原理简述
#### 1. 数据接入
系统实时或准实时地接入全方位的运维数据源，包括：
- 监控指标（Metrics）：从Prometheus、Zabbix、云监控等获取的系统指标（CPU、内存、磁盘IO）、应用指标（QPS、响应延迟、错误率）、业务指标（订单量、支付成功率）。
- 日志（Logs）：从ELK及SLS平台获取的应用日志、系统日志、中间件日志，包含关键的ERROR、WARN级别信息及上下文。
- 调用链（Traces）：从ARMS获取分布式追踪数据，清晰展示请求在微服务间的完整路径和耗时。

#### 2. 多智能体协作分析
系统内部由一个“运维团队”构成，每个智能体被赋予特定的角色和专长，各司其职、相互协作：
- 任务规划智能体：扮演“运维专家”，对故障进行自动化根因分析并生成步骤计划，将监控搜查任务指派给对应智能体。
- 指标分析智能体：擅长分析时序指标数据，发现异常波动和相关性。
- 日志分析智能体：精通NLP，快速从海量日志中提取错误模式、异常堆栈和关键事件。
- 拓扑感知智能体：理解系统架构和服务依赖关系，分析故障传播路径。
- 分析决策智能体：扮演“值班长”，通过结构化思维将监控查询结果显性化以进行根因分析，不获取新数据或改变状态，仅附加思维日志；当证据缺失、冲突或步骤无进展时进行判断。
- 最终输出智能体：扮演“运营专家”，对系统告警事件问题进行总结与结构化输出。

#### 3. 交互与反馈
整个分析过程和最终结论通过钉钉机器人以卡片消息、Markdown文本或交互式按钮的形式推送给运维人员。运维人员可在聊天窗口中与智能体进行自然语言交互（如“查看详细证据”“分析xxx应用在几点几分的故障根因”），将运维场景无缝嵌入日常工作流，极大提升响应效率。

## 二、当前要解决的核心问题
构建的系统旨在解决传统运维模式中普遍的痛点：

### 1. 告警风暴与信息过载
- 痛点：底层组件故障会触发上下游数百个服务的数千条关联告警，运维人员陷入“告警海洋”，难以分辨因果。
- 智能体解决思路：多智能体系统对告警进行聚类、降噪和关联，将上千条告警收敛为几个核心“故障事件”，直接指出根源，减轻认知负荷。

### 2. 故障定位效率低下，严重依赖个人经验
- 痛点：故障排查依赖资深工程师的专家经验，需在多个监控系统间反复横跳、手动查询，耗时耗力；专家离职或不在岗时，故障恢复时间不可控。
- 智能体解决思路：智能体7x24小时值守，集成顶尖专家分析模式，短时间内完成跨数据源关联分析，将人工数小时甚至数天的排查过程压缩到分钟级，降低对个人经验的过度依赖。

### 3. 数据孤岛与关联分析困难
- 痛点：监控指标、日志、调用链数据存储在不同系统，彼此割裂，人工关联操作繁琐、极易出错，难以发现深层次跨体系关联关系。
- 智能体解决思路：智能体系统天然具备全局视野，统一接入所有数据源，自动基于时间戳、服务名、TraceID等字段进行端到端关联，发现人类肉眼难以察觉的隐藏模式。

### 4. 应急响应流程僵化，沟通成本高
- 痛点：发现故障后需拉群、打电话通知各方，群内信息碎片化，沟通效率低下。
- 智能体解决思路：通过钉钉/企业微信机器人，智能体直接成为“应急响应中心”，主动推送结构化分析报告，所有人基于同一份事实讨论决策；还可直接执行预案、触发止损操作，将沟通从“发生了什么”提升到“我们该怎么办”。

### 5. 知识沉淀与复用的挑战
- 痛点：故障处理经验多留在工程师脑中或私下聊天记录，难以有效沉淀，导致同类错误反复出现。
- 智能体解决思路：智能体的每次分析过程和处理结果自动记录归档，形成可检索的故障案例库；类似故障再次发生时，快速匹配历史案例，直接给出可能原因和解决方案，实现运维知识的持续积累和自动化复用。

## 三、整体技术实现架构
方案基于Dify平台构建分层智能体工作流，实现面向故障诊断与根因分析的AI大模型应用，整体架构分为三层：
- 任务规划层：对故障进行自动化根因分析，生成明确步骤计划，将监控搜查任务指派给对应智能体。
- 感知层：负责接入多源运维数据，包括日志（Log）、指标（Metric）、链路追踪（Trace）以及变更事件等。
- 分析决策层：通过大模型对多维数据进行关联推理，识别异常模式并定位潜在根因，结合业务上下文生成可执行的修复建议或自动化动作。

### 架构示意图相关说明
- 数据源：SLS、ARMS、Prometheus（云产品/ACK）、云安全中心日志、PaaS/IaaS配置审计日志、WAF日志、K8S日志、业务日志等。
- 数据组件：Redis、OSS、PGSQL、向量数据库、函数计算等。
- 接入方式：HTTPS、SSE、Remote write prometheus等。
- 交互入口：钉钉/企微、AppFlow、常见故障处理手册、webhook等。

### 设计原则
#### 1. 拆分模型职责，透明化工作流
- 核心思路：构建类比人类运维团队的多智能体协同系统，而非依赖单一AI模型。
- 具体实现：
  - 职责拆分：将诊断流程分解为多个专业化子任务，通过JSON进行多智能体间结构化信息传递。
  - 透明化：每个智能体的输入、输出及决策依据均显式记录，确保分析过程可追溯、可解释。
  - 标准化：统一输出模板和语义规范，实现诊断结论标准化，便于与下游运维系统集成或人工复核。

#### 2. 动态查询外部数据
- 核心思路：通过MCP服务封装监控工具，实现外部数据动态查询，避免静态上下文导致的信息滞后。
- 具体实现：
  - 将日志查询、指标检索、链路追踪等监控工具封装为MCP服务，部署于函数计算平台。
  - 大模型在推理过程中可按需调用MCP服务，实时获取最新监控数据。
  - 用户CMDB中的应用拓扑关系也封装为MCP服务，帮助大模型理解系统架构上下文，提升根因推断准确性。

#### 3. 自我迭代
- 核心思路：利用Dify工作流引擎编排MCP工具调用逻辑，通过ReAct模式对复杂问题自行拆解和迭代。
- 示例：检测到服务延迟异常时，工作流先调用Metric MCP获取关键性能指标；若发现CPU/内存异常，进一步调用Log MCP查询错误日志；同时通过CMDB MCP获取服务依赖的上下游组件，结合Trace MCP分析调用链瓶颈，最终由大模型综合多源信息输出根因假设与处置建议。

## 四、如何构建根因分析知识库
丰富的知识库能让大模型从“通用语言模型”转变为“专属领域运维专家”，需系统补充以下几类信息：

### 1. 系统静态知识（让模型了解业务系统）
- 系统架构与文档：
  - 拓扑关系：清晰的微服务/组件依赖关系图（如Service A依赖数据库B和缓存C）。
  - 组件说明：每个服务、中间件、数据库、网关的详细功能描述、技术栈和版本信息。
- 关键业务流与数据流：
  - 核心业务执行路径（如“用户下单”：API网关→订单服务→库存服务→支付服务→消息通知服务）。
  - 数据在不同服务间的流转和转换规则。
- 基础设施信息：集群信息、节点列表、网络分区（VPC/AZ）、负载均衡配置等。
- 配置信息：重要应用配置文件（超时时间、重试次数、线程池大小）、数据库连接池配置、缓存策略等。

### 2. 动态运行时数据（让模型了解系统正在发生什么）
- 监控指标（Metrics）：
  - 黄金指标：吞吐量（QPS）、错误率（Errors）、延迟（Latency）、容量。
  - 资源指标：CPU、内存、磁盘IO、网络带宽使用率。
  - 应用层指标：JVM GC次数、数据库连接数、消息队列堆积情况、慢查询数量。
  - 业务指标：订单创建成功率、支付成功率、登录PV/UV。
- 日志（Logs）：
  - 错误日志：服务的异常堆栈信息（Stack Trace）、错误码（Error Code）。
  - 关键事件日志：服务启动/停止、重要业务流程节点（如“开始处理订单XXX”）。
  - 日志中的关键模式：如特定任务ID在多个服务间传递的追踪信息。
- 链路追踪（Trace）：分布式链路数据（如ARMS的Tracing），展示请求在不同服务上的耗时和状态，精准定位瓶颈和故障点。
- 事件（Event）：
  - 变更事件：最近的代码部署、配置变更、数据库变更、扩容/缩容操作（时间、内容、操作人）。
  - 告警事件：其他监控系统（如Prometheus/Zabbix）触发的告警信息、上下游系统故障通知。

### 3. 历史经验与解决方案（让模型学会如何诊断）
- 历史故障报告（RCA）：
  - 格式包含：故障现象、排查过程、根因、解决方案、预防措施。
- 常见问题库（Runbook）：针对特定告警或错误的标准化处理手册（如“CPU利用率>90%时，先检查Service A服务，执行top -Hp命令查看线程情况”）。
- 专家经验规则：将运维专家的经验转化为结构化知识（如“订单服务和支付服务同时报错，先检查数据库连接”“错误码502，优先排查上游服务和网络”）。

### 4. 流程与元信息（让模型遵循规范）
- 根因分析框架（SOP）：期望的排查流程（如“确认影响范围→检查近期变更→沿依赖链逐层下钻→...”）。
- 汇报格式模板：分析报告需包含的部分（如“【摘要】、【影响范围】、【可能根因】、【证据分析】、【建议行动】”）。
- 术语词典：统一系统内专有名词、服务名、指标名的叫法，避免歧义。

### 5. 有效地将信息沉淀到Dify知识库
- 非结构化数据及实时数据：
  - 非结构化：直接上传PDF、Word、Markdown格式的架构文档、故障报告、Runbook。
  - 实时数据：监控指标、变更事件等通过MCP查询外部接口（如Prometheus、CMDB），实时获取后作为上下文提供给LLM，保证信息时效性。
- 多知识库划分：按领域创建多个知识库（如“系统架构知识库”“历史故障案例库”“运维流程库”），根据问题类型选择性启用，提高检索精度。
- 数据预处理：
  - 清洗与脱敏：去除日志、文档中的敏感信息（IP、密码、个人信息等）。
  - 切片优化：对长文档调整分段策略，确保关键信息（错误码、解决方案）完整检索。

### 6. 基于专家经验强化训练模型定位根因能力
- 建立指标关联：如“应用RT升高→检查ECS的CPU/内存→检查数据库监控→检查缓存监控”“SLB后端服务器健康检查失败→关联检查ECS状态和应用日志”。
- 区分直接现象和根本原因：如“数据库CPU高”是现象，“大量慢SQL缺乏索引”是根因。
- 时序关联：关注指标异常的时间线，判断故障传播链起点（如先网络流量突增还是先应用CPU飙升）。
- 基线对比：异常表现为指标相对于历史基线的偏离（如夜间批量作业和白天在线业务的CPU使用率80%意义不同）。
- 配置信息关联：将监控指标与最近的变更事件（代码发布、配置修改）关联分析。

## 五、基于ReAct模式的AIOps根因分析技术实现
复杂故障问题无法通过单次工具调用或静态上下文直接求解，引入ReAct（Reasoning + Acting）模式，将大模型的推理能力与外部工具调用能力深度融合，实现动态拆解、迭代验证与逐步收敛。

### ReAct模式运行机制
核心是交替执行“推理（Thought）”与“行动（Action）”两个阶段：
1. 任务规划智能体基于告警信息生成初始假设（如“服务延迟可能由资源瓶颈或依赖服务异常引起”），制定首轮查询计划。
2. 工作流引擎调用Metric MCP获取目标服务的CPU、内存、请求延迟等时序指标；若指标显示资源使用率突增，触发第二轮推理（“高CPU是否由特定代码路径或外部调用引发？”），进而调用Log MCP检索对应时间段的错误日志或异常堆栈。
3. 拓扑感知智能体通过CMDB MCP获取服务上下游依赖拓扑，识别故障传播路径；若延迟集中在跨服务调用，进一步调用Trace MCP获取完整调用链数据，定位瓶颈节点（如数据库慢查询、第三方接口超时）。
4. 每一轮工具调用结果作为新证据输入分析决策智能体，评估证据链的完整性与一致性；若证据不足或冲突（如指标异常但日志无报错），系统自动重构问题表述（如“是否为非错误型性能退化？”），发起新一轮针对性工具调用。
5. 整个过程由Dify工作流引擎驱动，支持循环、条件分支与超时控制，确保有限步数内收敛至高置信度根因；最终由最终输出智能体生成包含根因假设、证据摘要与处置建议的标准化报告。

### ReAct的性能问题与解决方案
| 性能痛点 | 优化措施 |
| --- | --- |
| 工作流运行时间较久，端到端延迟高 | 减少不必要的循环限制次数，通过提示词或自定义函数前置处理数据减少无效思考循环；在工作流中添加多个过程输出模块，提升响应速度与用户体验 |
| 上下文信息易丢失，token消耗高 | 对历史信息进行摘要或关键片段提取，仅传递必要上下文给后续步骤，降低token消耗并保留核心证据 |
| 上下文过长引发推理性能下降 | 同上，通过上下文压缩与精准引用优化 |
| 循环终止判断不合理（过早结束或陷入无效循环） | 通过规划MCP服务持续监督任务进展，结合“证据充分性”与“步骤收敛性”动态决定是否终止循环 |
| 最终输出质量不稳定（中间结论、思考发散） | 判定任务完成后，显式调用总结工具触发大模型生成结构化、详尽的根因报告，确保输出专业且稳定 |

## 六、Dify工作流实现
### ReAct模式多智能体交互流程
#### 1. 核心参与角色
| 类别 | 子Agent/工具 | 用途 |
| --- | --- | --- |
| 数据Agent | 日志分析Agent | 生成候选日志查询语句、日志查询代码检索、调用链路追踪定位底层报错 |
| 数据Agent | 指标分析Agent | 应用指标分析、变更运维事件获取 |
| 数据Agent | 链路分析Agent | 基础告警分析、调用链详情查询 |
| 通用工具 | 思考工具-草稿纸 | 辅助推理过程记录 |
| 通用工具 | 时间处理 | 时间格式转换、时间区间计算 |
| 通用工具 | 数值计算 | 指标数据计算与分析 |

#### 2. 工作流步骤说明
1. **用户触发**：用户通过告警卡片提供告警信息，触发工作流。
2. **工作流初始化**：判断是否初次循环，将用户query、memory等赋值到工作流变量，从知识库检索对应信息。
3. **问题拆解及任务规划**：“运维专家”Agent生成根因分析步骤计划，将监控搜查任务指派给对应智能体。
4. **监控metric查询**：Metric Agent分析时序指标数据，发现异常波动和相关性。
5. **日志查询**：Log Agent利用NLP从海量日志中提取错误模式、异常堆栈和关键事件。
6. **链路调用查询**：Trace Agent查询系统架构和服务依赖关系，分析故障传播路径。
7. **分析决策**：“值班长”Agent对监控查询结果进行结构化根因分析，附加思维日志；证据缺失、冲突或步骤无进展时进行判断。
8. **循环**：若未满足停止条件，“运维专家”Agent根据“值班长”输出调整下一轮计划，继续调用数据Agent，直至满足停止条件。
9. **输出报告**：“运营专家”Agent总结所有事件问题，结构化输出“事件分析报告”。

### 用到的工具接口清单
#### 1. 阿里云openapi MCP服务接口
https://api.aliyun.com/mcp

| 工具类别 | API名称 | 用途 | 关键参数 |
| --- | --- | --- | --- |
| 资源查询 | DescribeInstancesFullStatus | 获取ECS实例列表及状态（如运行中、停止） | regionId（区域ID）、instanceId（实例ID，可选）、status（实例状态）、pageSize（分页大小，默认50） |
| 监控数据 | DescribeMetricList/DescribeMetricData | 查询指定监控项的最新监控数据（CPU使用率、内存使用率等） | namespace（命名空间）、metricName（指标名称）、dimensions（实例维度，JSON格式） |
| 日志查询 | alibabacloud-observability-mcp-server | 查询SLS中的日志（应用错误日志、Nginx访问日志等） | project（项目名称）、logstore（日志库名称）、query（查询语句） |
| 网络探测（测试验证） | CreateInstantSiteMonitor | 创建一次性站点监控任务，探测网络服务质量（HTTP、TCP、Ping） | address（探测地址）、taskName（任务名称）、interval（监控频率，分钟）、protocol（协议） |
| 应用监控 | QueryMetricByPage | 分页查询应用监控或前端监控的相关指标 | StartTime（起始时间）、EndTime（结束时间）、Metric（指标名称）、dimensions（实例维度） |
| 调用链查询 | GetMultipleTrace | 查询应用调用链详情，用于性能瓶颈定位和依赖分析 | traceID（调用链唯一标识）、regionId（区域ID）、startTime（开始时间） |
| 事件查询 | DescribeSystemEventAttribute | 查询系统事件（实例重启、磁盘扩容、故障迁移等） | product（产品名，如ECS）、eventType（事件类型）、regionId（区域ID）、startTime（开始时间） |

#### 2. 可观测MCP服务接口
https://github.com/aliyun/alibabacloud-observability-mcp-server

| 可观测产品 | 工具名称 | 用途 | 关键参数 | 最佳实践 |
| --- | --- | --- | --- | --- |
| SLS | sls_list_projects | 列出SLS项目，支持模糊搜索和分页 | projectName（可选，模糊搜索）、limit（默认50）、regionId（阿里云区域ID） | 不确定可用项目时优先使用；合理设置limit避免返回过多结果 |
| SLS | sls_list_logstores | 列出项目内的日志存储，支持名称模糊搜索 | project（必需）、logStore（可选，模糊搜索）、limit（默认10）、isMetricStore（是否筛选指标存储）、logStoreType（日志存储类型）、regionId | 确定项目后查找相关日志存储；通过logStoreType筛选特定类型 |
| SLS | sls_describe_logstore_index | 查看日志存储的索引信息 | project（必需）、logStore（必需）、regionId | 了解可用字段及类型；检查所需字段是否启用索引 |
| SLS | sls_execute_sql_query | 在指定时间范围内对日志存储执行SQL查询 | project（必需）、logStore（必需）、query（必需）、fromTimestampInSeconds（必需）、toTimestampInSeconds（必需）、limit（默认10）、regionId | 优化时间范围提升查询性能；限制返回结果数量 |
| SLS | sls_translate_text_to_sql_query | 将自然语言描述转换为SLS SQL查询语句 | text（必需）、project（必需）、logStore（必需）、regionId | 适用于不熟悉SQL语法的用户；复杂查询需优化生成的SQL |
| SLS | sls_diagnose_query | 诊断SLS查询问题，提供失败原因分析 | query（必需）、errorMessage（必需）、project（必需）、logStore（必需）、regionId | 查询失败时使用；根据诊断建议修改查询语句 |
| ARMS | arms_search_apps | 根据应用名称搜索ARMS应用 | appNameQuery（必需）、regionId（必需）、pageSize（默认20）、pageNumber（默认1） | 查找特定名称应用；获取其他ARMS操作所需的应用PID；合理设置分页参数 |
| ARMS | arms_generate_trace_query | 根据自然语言问题生成ARMS追踪数据的SLS查询 | user_id（必需）、pid（必需）、region_id（必需）、question（必需） | 查询应用追踪信息；分析性能问题和服务调用关系；集成自动重试机制处理瞬态错误 |
| ARMS | arms_get_application_info | 获取特定ARMS应用的详细信息 | pid（必需）、regionId（必需） | 用户明确请求应用信息时使用；确定应用开发语言；执行其他操作前获取基本信息 |
| ARMS | arms_profile_flame_analysis | 分析ARMS应用火焰图性能热点 | pid（必需）、startMs（必需）、endMs（必需）、profileType（默认cpu）、ip（可选）、thread（可选）、threadGroup（可选）、regionId（必需） | 分析应用性能热点；支持CPU和内存类型分析；适用于Java和Go应用 |
| ARMS | arms_diff_profile_flame_analysis | 对比不同时间段的火焰图性能变化 | pid（必需）、currentStartMs（必需）、currentEndMs（必需）、referenceStartMs（必需）、referenceEndMs（必需）、profileType（默认cpu）、ip（可选）、thread（可选）、threadGroup（可选）、regionId（必需） | 发布前后性能对比；分析性能优化效果；识别性能退化点 |
| CMS | cms_translate_text_to_promql | 将自然语言描述转换为PromQL查询语句 | text（必需）、project（必需）、metricStore（必需）、regionId（必需） | 提供清晰具体的指标描述；提及特定指标名称、标签或操作；优化生成的查询以提升准确性和性能 |

### 各Agent输出标准及提示词设计
#### 1. 运维专家Agent
- 用途：根据告警信息生成分析计划，协调下游Agent执行，根据结果反思和调整计划。
- 核心职责：解析告警输入、生成结构化排查计划、调度专业智能体、关联业务上下文。
- 工作流程规范：
  1. 输入信息校验：检查是否包含项目、应用、环境、时间等信息，缺失则要求用户补充（提供示例）。
  2. 明确具体时间：统一转换为UTC+8时区，格式为`YYYY-MM-DD HH:MM:SS`（缺秒补`:00`）。
  3. 拓扑定位：含域名调用`lookup_domain_topology`、含资源ID调用`lookup_resource_by_id`、已知项目/应用调用`list_resources_by_project_app`。
  4. 指派分析任务：指标查询→指标分析智能体、日志检索→日志分析智能体、调用链分析→调用链分析模块。
- 禁止行为：自行解析原始数据、跳过拓扑定位猜测根因、连续调用同一CMDB工具超2次、输出模糊指令。
- 输出格式：JSON格式，包含`agent_type`（固定为master）、`data`（含plan、reflection）、`error_message`。
- 输出示例：
  ```json
  {
    "agent_type": "master",
    "data": {
      "plan": [
        {
          "step_id": 1,
          "agent": "metric",
          "date": "2025-09-20 10:00:00到2025-09-20 12:00:00",
          "query_backgroud": "2025年9月18日22点到23点 dreamone-customer-system请求耗时上升，请分析一下根因",
          "query": "app dreamone-order-system所关联的ECS实例列表为xxx，数据库为RDS实例xxx，请分析这些实例在最近7天（2025-09-20至2025-09-27）的CPU使用率、内存使用率、网络流量及RDS的CPU使用率、连接数等监控指标数据是否有异常，并生成趋势图。",
          "reason": "接口调用成功率下降可能由底层资源瓶颈导致，需优先验证ECS节点资源水位和RDS数据库性能是否正常，排除基础设施层问题。"
        },
        {
          "step_id": 2,
          "agent": "trace",
          "date": "2025-09-20 10:00:00到2025-09-20 12:00:00",
          "query_backgroud": "2025年9月18日22点到23点 dreamone-customer-system请求耗时上升，请分析一下根因",
          "query": "应用 dreamone-order-system 的接口调用成功率下降，请使用ARMS查询最近7天内该应用的调用链数据，重点分析失败请求的调用链，识别异常服务（如dreamone-customer-system/dreamone-item-system）、慢调用节点或HTTP状态码5xx错误，并整理关键链路数据。",
          "reason": "若基础设施指标正常，需通过调用链分析定位具体异常环节，确认是否由下游服务依赖故障或代码逻辑缺陷导致请求失败。"
        },
        {
          "step_id": 3,
          "agent": "log",
          "date": "2025-09-20 10:00:00到2025-09-20 12:00:00",
          "query_backgroud": "2025年9月18日22点到23点 dreamone-customer-system请求耗时上升，请分析一下根因",
          "query": "调用阿里云SLS日志MCP接口查询dreamone-order-system对应的Logstore order-system-business-log中最近7天ERROR级别日志，重点检索'ConnectionTimeout'、'SQLTimeout'、'ServiceUnavailable'等关键词，分析异常堆栈和错误频率分布。",
          "reason": "结合业务日志验证监控和链路分析结果，确认具体错误类型（如数据库连接池耗尽、第三方服务超时等），为根因提供直接证据。"
        }
      ],
      "reflection": "当前计划优先验证基础设施资源（Metric）、调用链路（Trace）、业务日志（Log）三层数据：1) 排除ECS/RDS资源瓶颈；2) 定位调用链异常节点；3) 通过日志确认具体错误类型。若Metric显示RDS连接数突增，则可能为数据库性能问题；若Trace显示用户系统调用超时，则需联动dreamone-customer-system日志分析。下一步将根据智能体返回数据交叉验证，逐步收敛根因范围。"
    },
    "error_message": null
  }
  ```

#### 2. Metric Agent
- 用途：调用监控MCP接口查询监控指标数据（CPU使用率、内存使用率等）。
- 角色：Metric监控数据获取智能体，从Metric时序库中获取时序数据并按指定格式输出。
- 工作流程：
  1. 获取查询指标的命名空间（Namespace）和监控项名称（MetricName）。
  2. 调用时间工具，确定起始和结束时间段（格式为YYYY-MM-DDThh:mm:ssZ）。
  3. 根据时间跨度选择统计周期（Period）：≤3分钟→15秒、3-10分钟→60秒、10-60分钟→900秒、>60分钟→3600秒。
  4. 根据实例ID生成监控维度（Dimensions）。
  5. 执行`DescribeMetricList`工具获取数据，按输出格式采样输出。
- 限制：指标为空时检查参数正确性、不查询无关信息、不编造数据、仅查询上海地域。
- 输出格式：JSON格式，包含`agent_type`（固定为metric）、`status`（success/failure）、`summary`、`data`（含metrics）、`error_message`。
- 输出示例：
  ```json
  {
    "agent_type": "metric",
    "status": "success",
    "summary": "我已经成功获取了应用xxx生产ECS实例`i-xxxmu3v`的CPU使用率数据。经分析该ECS的利用率相对较低，建议结合其他指标进行关联分析",
    "data": {
      "metrics": [
        {
          "namespace": "acs_ecs_dashboard",
          "metricName": "AliyunEcs_CPUUtilization",
          "unit": "%",
          "tag": {
            "instanceId": "i-bxxxmu3v",
            "regionId": "cn-shanghai"
          },
          "values": [
            {
              "timestamp": 1758023820,
              "value": 63.7
            }
          ]
        }
      ]
    },
    "error_message": null
  }
  ```

#### 3. Trace Agent
- 用途：调用链路监控MCP接口查询链路监控及APM数据（如调用链详情）。
- 角色：资深Trace诊断专家，为用户提供详尽且未经删改的错误Trace信息。
- 核心原则：工具是唯一入口、数据完整性第一（不截断/改写原始信息）、杜绝心算、控制数据规模、仅查询上海地域。
- 工作流程：
  1. 分析与准备：解析用户意图提取项目名、应用名、时间信息，调用`ListTraceApps`工具获取应用PID。
  2. 定位少量代表性错误Trace：调用`SearchTracesByPage`工具（isError=true、PageSize=3），提取最多3个唯一TraceID。
  3. 获取完整链路详情：调用`GetMultipleTrace`工具，传入TraceID列表和相同时间戳。
  4. 数据处理与格式化：按TraceID分组Spans，生成标准化Span对象（含错误信息字段）。
  5. 错误归因与最终输出：找到最深错误Span标记`[根因]`，上层传播错误标记`[传播]`，聚合后返回。
- 输出格式：JSON格式，包含`agent_type`（固定为trace）、`status`（success/failure）、`summary`、`data`（含traces）、`error_message`。

#### 4. Log Agent
- 用途：调用阿里云SLS日志MCP接口查询应用日志、访问日志和系统运行日志。
- 角色：SLS日志分析专家，采样获取SLS Logstore中的数据，为故障排查提供采样日志。
- 上下文：预设不同类型日志对应的SLS project和logstore。
- 工作流程：
  1. 提取用户输入中的日志库、时间范围、日志特征。
  2. 通过`sls_translate_text_to_sql_query`工具将自然语言转化为SLS查询语句。
  3. 调用`sls_execute_sql_query`工具执行语句，失败则用`sls_diagnose_query`工具排查重试。
  4. 对结果采样（去重、最多10条）并输出。
- 限制：输出为空时检查参数、单次查询时间范围≤1天、日志条数≤10条、仅查询上海地域、不编造数据。
- 输出格式：JSON格式，包含`agent_type`（固定为log）、`status`（success/failure）、`data`（含logs）、`survey_summary`、`error_message`。
- 输出示例：
  ```json
  {
    "agent_type": "log",
    "status": "success",
    "data": {
      "logs": [
        {
          "timestamp": "1758027375",
          "level": "ERROR",
          "message": "1 --- [   scheduling-1] o.s.s.s.TaskUtils$LoggingErrorHandler    : Unexpected error occurred in scheduled task\n\njava.lang.RuntimeException: null\n\tat org.example.task.ExceptionTask.scheduleThrowException(ExceptionTask.java:23)\n\tat jdk.internal.reflect.GeneratedMethodAccessor75.invoke(Unknown Source)\n\tat java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)\n\tat java.base/java.lang.reflect.Method.invoke(Method.java:566)\n\tat org.springframework.scheduling.support.ScheduledMethodRunnable.run(ScheduledMethodRunnable.java:84)\n\tat org.springframework.scheduling.support.DelegatingErrorHandlingRunnable.run(DelegatingErrorHandlingRunnable.java:54)\n\tat java.base/java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:515)\n\tat java.base/java.util.concurrent.FutureTask.runAndReset(FutureTask.java:305)\n\tat java.base/java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:305)\n\tat java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1128)\n\tat java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:628)\n\tat java.base/java.lang.Thread.run(Thread.java:834)",
          "source": {
            "__hostname__": "xxx",
            "_pod_name_": "dreamone-order-system-deployment-5cbxxx"
          },
          "fields": {}
        }
      ]
    },
    "survey_summary": "我在日志发现存在xxx报错异常，可能线程池存在满了，建议查询数据库线程指标以进一步确认。",
    "error_message": null
  }
  ```

#### 5. 值班长Agent
- 用途：将结构化思维显性化，评估当前证据，检查规则/模式，提出假设和下一步步骤，决定停止条件；不获取新数据，仅附加思维日志。
- 角色：资深SRE值班长，负责关键判断与决策仲裁。
- 核心职责：证据整合、逻辑校验、决策干预、关联业务上下文。
- 决策触发条件（满足任一即介入）：
  - 指标、日志、调用链结论相互冲突；
  - 根因假设缺乏关键支撑证据；
  - 连续两个分析步骤未缩小根因范围；
  - CMDB信息未被有效利用。
- 推理原则：优先业务影响、依赖拓扑优先、奥卡姆剃刀（优先单一原因）、显性化思维（结论需附推理依据）。
- 禁止行为：发起新数据查询、忽略CMDB上下文、输出模糊结论、重复已有分析步骤、连续调用同一CMDB工具超2次。
- 输出格式：结构化Markdown，包含决策结论、推理依据、后续建议。

#### 6. 运营专家Agent
- 用途：对所有事件问题进行总结并结构化输出“事件分析报告”。
- 角色：专业AIOps根因分析运营专家。
- 要求：
  1. 时间格式统一为“YYYY-MM-DD HH:mm:ss”；
  2. 结合当前时间及问题发生时间输出；
  3. 关键信息准确无误；
  4. 监控发现部分以表格形式呈现，附趋势描述；
  5. 日志示例真实反映异常特征；
  6. 原因分类从基础设施、网络、中间件、应用、配置、第三方依赖等维度归类；
  7. 优化建议具体可落地（优先自动化、容灾、监控覆盖）；
  8. 不捏造信息。
- 输出格式样例：
  ```markdown
  ### 一、问题简述
  2025-09-15 10:30:45 xxx反馈业务域名访问超时，业务耗时增长严重，客户下线DDoS和WAF后恢复正常。原因是waf一台服务节点异常，摘除异常节点后风险消除。共有两个业务受到影响，分别是电商中台和客服系统。

  ### 二、影响概述
  9.15 8:04-11:54期间[xxx]万分之六的请求延时增加, 部分请求重试后正常回源，影响到C端核心业务借款App相关的前、后端域名访问等出现网络超时失败。以及B端核心业务催收、电销、客服等业务系统，大面积反馈网络超时报错。
  【故障影响时间】2025-09-15 10:30 ～ 2025-09-15 11:54 共计84分钟
  【风险评估】暂无

  ### 三、问题原因
  【原因分类】
  阿里云产品硬件问题。
  【原因概述】
  WAF北京集群中一台机器管理口板卡故障, 导致DNS解析时延增加, 周期概率性影响在WAF侧配置了域名回源的业务流量。

  ### 四、问题分析及优化建议
  【故障根因】
  WAF集群中一台机器管理口板卡故障, 导致所有管理口通信的链路异常。
  【监控发现】（输出内容请以表格方式并添加监控趋势图）
  1. 连接数监控显示活跃连接数达到最大值100，且持续超过5分钟。
  2. 日志出现大量499，且都集中在同一个ip。（补充其中一条日志）
  【暴露问题】
  DNS解析链路依赖管理口，监控日志基于管理口上报失败，无法做到自动摘除
  【优化建议】
  1. 告警优化: 优化主机探活告警, 单机10%丢包电话告警
  2. 监控优化: 增加告警, 采集异常后电话告警
  3. DNS解析异常的容灾优化
  ```

## 七、ClaudeCode与Dify对比与选型
### ClaudeCode核心逻辑代码
```python
import os
import asyncio
from claude_code import ClaudeCodeOptions, ConversationSession, HookMatcher
from hooks import pre_tool_logger, post_tool_logger
from mcps import aliyun_sls_mcp, aliyun_arms_ecs_mcp, time_mcp

async def main():
    # 获取当前目录的MCP配置文件路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    mcp_config_path = os.path.join(current_dir, "mcp_config.json")
    
    # 读取当前文件下的intro.md文件内容
    with open(os.path.join(current_dir, "intro.md"), "r", encoding="utf-8") as f:
        system_prompt = f.read().strip()
    
    # 配置远程MCP流HTTP协议工具
    options = ClaudeCodeOptions(
        hooks={
            'PreToolUse': [
                HookMatcher(hooks=[pre_tool_logger])
            ],
            'PostToolUse': [
                HookMatcher(hooks=[post_tool_logger])
            ]
        },
        allowed_tools=["Read", "Write", "Bash", "mcp__time__time"],
        permission_mode="acceptEdits",
        # 使用MCP配置文件路径
        mcp_servers={
            "aliyun-mcp": aliyun_sls_mcp,
            "aliyun-arms-ecs": aliyun_arms_ecs_mcp,
            "time": time_mcp
        },
        system_prompt=system_prompt
    )
    
    session = ConversationSession(options)
    await session.start()

asyncio.run(main())
```

### 对比与选型建议
| 维度 | Claude Code方案 | Dify方案 |
| --- | --- | --- |
| 开发效率 | 需编写核心逻辑代码（部分由Claude生成） | 可视化编排，快速搭建原型 |
| 灵活性 | 可深度定制算法/模型 | 依赖LLM能力，复杂逻辑需结合自定义函数 |
| 准确性 | 确定性算法+AI模型，内置多种优化算法 | LLM可能产生幻觉，需自行通过提示词参数等优化 |
| 实时性 | 微秒级响应（模型推理） | 秒级延迟（LLM API调用） |
| 运维成本 | 需维护训练管道/部署环境 | 无基础设施管理，SaaS化运维 |
| 可观测支持 | 需额外开发日志/追踪分析模块 | 原生支持文本/日志分析及调用量统计 |
| 知识沉淀 | 需独立构建知识库 | 内置知识库自动学习 |
| 典型场景 | 金融互联网等低延迟算法控制场景 | 零售电商企业快速上线场景 |

### 选型建议
- 需求简单/快速上线：优先使用Dify。
- 需控制算法/超低延迟：推荐ClaudeCode。
- 复杂场景：80%标准场景+20%定制，可结合使用。

## 八、总结
目前该AIOps项目已推进一个多月，仍在持续优化迭代功能，包括：
- 开发集成IDC的CMDB服务；
- 拆分知识库；
- 动态注入上下文；
- 时间通过中心化函数统一；
- 重写提示词结构；
- 加入缓存机制等。

部分场景的根因定位成功率从20%优化到70%左右，仍有提升空间。当前在工程层面优化工作流，后续将在模型层面进行更深入的挖掘。