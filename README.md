<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=180&section=header&text=Samarth%20Annigeri&fontSize=42&fontColor=fff&animation=twinkling&fontAlignY=32&desc=Machine%20Learning%20%E2%80%A2%20AI%20Systems%20%E2%80%A2%20Data%20Architecture%20%E2%80%A2%20Product&descAlignY=55&descSize=16" width="100%"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&pause=1000&color=00D9FF&center=true&vCenter=true&multiline=false&width=860&lines=ML+pipelines+%E2%86%92+AI+agents+%E2%86%92+production+systems.;LangChain+%C2%B7+LangGraph+%C2%B7+CrewAI+%C2%B7+AutoGen+%C2%B7+n8n.;RAG+%C2%B7+vector+stores+%C2%B7+fine-tuning+%C2%B7+MLOps+%C2%B7+evals.;LSTM+%C2%B7+LightGBM+%C2%B7+Transformers+%C2%B7+causal+inference.;From+probability+theory+to+deployed+agentic+systems." alt="Typing SVG" />

<br/><br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/samarth-annigeri-14326a178/)
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=notion&logoColor=white)](https://theindianmagenta.notion.site/Product-Portfolio-f56b69796af74829a005df99d3cadf4b)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:samarth.annigeri@mail.mcgill.ca)

<br/>

![Open to Work](https://img.shields.io/badge/%F0%9F%9F%A2%20Open%20to%20Work-ML%20Engineer%20%7C%20AI%20Engineer%20%7C%20Data%20Architect%20%7C%20PM-brightgreen?style=flat-square&labelColor=0d1117)

</div>

---

<img align="right" width="340" src="https://github-readme-stats.vercel.app/api?username=Agent007repo&show_icons=true&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true&rank_icon=github" />

## Who I Am

I design and ship **production AI systems** across the full stack: from mathematical foundations and classical ML through deep learning, LLM architecture, agentic workflows, and cloud deployment. My work spans credit risk (ARIMA pipelines in Azure), supply chain intelligence (LSTM + LightGBM multi-horizon forecasting), quantitative investment (alpha generation on 147 stock characteristics), and AI agent systems (multi-step reasoning pipelines, RAG, n8n automation).

I don't just use frameworks. I understand why each layer of the stack exists, where it breaks, and how to instrument it for production. Whether the problem needs a Bayesian prior, a fine-tuned LLM, a LangGraph multi-agent loop, or a LightGBM ensemble, I reach for the right tool and I know the tradeoffs of each choice.

**Current role:** Data Architect @ BNP Paribas Montreal  
**Education:** MMA, McGill University | BS Information Systems, SFSU  
**Authorization:** Canadian PGWP - open to all of Canada + remote  
**Outside of work:** Badminton, strength training, Vedic philosophy

<br clear="right"/>

---

## Impact by the Numbers

<div align="center">

| Domain | System | Key Result |
|:---|:---|:---|
| Supply Chain Risk | LSTM AE + LightGBM | >80% recall on 6 major global shock events; AUC 0.85 at 7-day horizon |
| Quantitative Finance | Neural Net + Factor Model | 11.71% annualized return, 7.71% alpha, Sharpe 0.71 (2020-2023 OOS) |
| Air Quality Forecasting | Random Forest | R² = 0.92, MAE = 0.08 on UCI benchmark dataset |
| Social Media Causal Inference | DiD + Network Analysis | Louvain community modularity 0.9174; EUA causal impact quantified |
| Email Campaign Uplift | CausalML Meta-Learners | ATE = +0.0068 lift, validated via placebo refutation |
| Credit Risk (Production) | ARIMA + Azure ML | Deployed to BNP Paribas production environment |

</div>

---

## Featured Projects

<details open>
<summary><b>SCRI: Supply Chain Risk Intelligence System</b> &nbsp;|&nbsp; <a href="https://github.com/Agent007repo/SCRI-Supply-Chain-Risk-Intelligence-System">View Repository</a></summary>

<br/>

> **Problem:** $56T in global trade is exposed to tariff shocks, port closures, and geopolitical cascades. Batch-daily systems react after the damage is done.

**Solution:** A near-real-time, 4-layer ML pipeline that detects supply chain stress before it propagates.

| Layer | Model | Purpose |
|:---|:---|:---|
| 1 - Detection | LSTM Autoencoder (2L, 64 hidden, latent=32) | Unsupervised shock detection on sequential signal patterns |
| 2 - Forecast | LightGBM multi-horizon | Binary risk classification: 7d / 14d / 30d ahead |
| 3 - Score | Composite SCSI index | Continuous stress scoring per timestep |
| 4 - Alert | Threshold engine | CLEAR / ELEVATED / HIGH / CRITICAL tiers |

**Signals ingested:** Baltic Dry Index, WTI Crude, ISM Manufacturing PMI, PPI All Commodities, US-China trade balance, shipping equity basket (ZIM, FDX, UPS, BDRY), T10Y2Y yield curve, NY Fed GSCPI.

**Backtested against:** US-China tariff war (2018-19), COVID demand collapse (Mar 2020), Suez Canal blockage (Mar 2021), Russia-Ukraine invasion (Feb 2022), Shanghai lockdowns (Mar-Jun 2022), Red Sea / Houthi attacks (Late 2023).

**Results:** LSTM AE recall >80% on top-10 shock events. LightGBM AUC-ROC: 0.85+ at 7d, 0.82+ at 14d, 0.78+ at 30d.

`Python` `TensorFlow` `LightGBM` `LSTM` `FRED API` `Time Series` `Anomaly Detection` `Geopolitical Risk`

</details>

---

<details>
<summary><b>Advanced Stock Return Prediction and Portfolio Optimization</b> &nbsp;|&nbsp; <a href="https://github.com/Agent007repo/Advanced-Stock-Return-Prediction-and-Portfolio-Optimization">View Repository</a></summary>

<br/>

> ML-driven quantitative investment framework on 147 stock characteristics with out-of-sample validation across 2020-2023.

Ridge, LASSO, Elastic Net, and Neural Networks with residual connections. Mixed 70/30 long-short strategy with volatility-based position sizing and 3% concentration caps. **11.71% annualized return, 7.71% alpha, Sharpe 0.71.**

`Python` `TensorFlow` `scikit-learn` `Quantitative Finance` `Factor Models` `Portfolio Optimization`

</details>

---

<details>
<summary><b>Vaccination Tweet Analysis - NLP + Causal Inference</b> &nbsp;|&nbsp; <a href="https://github.com/Agent007repo/Vaccination-Tweet-Analysis">View Repository</a></summary>

<br/>

> End-to-end social network analytics on COVID-19 vaccine discourse at scale.

VADER sentiment, PageRank influencer detection, Louvain community detection (modularity **0.9174**), information cascade modeling, and difference-in-differences causal inference to measure the effect of EUA announcements on public sentiment.

`Python` `NetworkX` `NLTK` `Causal Inference` `NLP` `Social Network Analysis`

</details>

---

<details>
<summary><b>Causal Inference - Email Marketing Campaign</b> &nbsp;|&nbsp; <a href="https://github.com/Agent007repo/Causal_Inference_Project-">View Repository</a></summary>

<br/>

> CausalML meta-learners (S-Learner via LR, T-Learner via XGBoost) and DoWhy causal graph framework to estimate ATE of a men's email campaign on e-commerce conversions. **ATE = +0.0068** validated via placebo refutation.

`Python` `CausalML` `DoWhy` `XGBoost` `A/B Testing`

</details>

---

<details>
<summary><b>Air Quality Prediction - Random Forest</b> &nbsp;|&nbsp; <a href="https://github.com/Agent007repo/Air_Quality_Random_Forest_Model_Project">View Repository</a></summary>

<br/>

> CO concentration prediction on UCI's Air Quality dataset. **R² = 0.92, MAE = 0.08, RMSE = 0.12.** Rigorous EDA, multicollinearity-aware feature selection, and temporal diurnal pattern analysis.

`Python` `scikit-learn` `EDA` `Feature Engineering` `Random Forest`

</details>

---

<details>
<summary><b>Avocado Prices Prediction</b> &nbsp;|&nbsp; <a href="https://github.com/Agent007repo/-Avocado-Prices-Prediction">View Repository</a></summary>

<br/>

> Regression and time series analysis on Hass Avocado Board data. EDA, seasonal decomposition, multi-model comparison across US regions.

`Python` `Regression` `EDA` `Time Series` `Feature Engineering`

</details>

---

## Full-Stack AI Competency Map

> Organized by architectural layer — from mathematical primitives to deployed agentic systems.

<div align="center">

```
LAYER 0 — Mathematical & Statistical Foundations
├── Probability       Bayesian inference · MLE/MAP · conjugate priors · Monte Carlo
├── Statistics        Hypothesis testing · confidence intervals · power analysis · bootstrap
├── Linear Algebra    Matrix decomposition · SVD · PCA · eigenvalue methods
├── Optimization      Gradient descent · Adam/AdamW · convex/non-convex · regularization
└── Causal Theory     DAGs · do-calculus · SCMs · identification · counterfactuals

LAYER 1 — Classical Machine Learning
├── Supervised        XGBoost · LightGBM · Random Forest · Ridge / LASSO / ElasticNet · SVM
├── Unsupervised      K-Means · DBSCAN · Louvain · PageRank · PCA · t-SNE · UMAP
├── Causal ML         CausalML · DoWhy · DiD · S/T/X-Learners · Propensity · Refutation
├── Time Series       ARIMA · SARIMA · Prophet · seasonal decomp · multi-horizon forecasting
└── Evaluation        AUC-ROC · precision/recall · SHAP · permutation importance · calibration

LAYER 2 — Deep Learning
├── Frameworks        TensorFlow / Keras · PyTorch · JAX (reading fluency)
├── Architectures     LSTM · GRU · Transformer · CNN · Autoencoder · Residual / Skip-connect
├── Training          Batch norm · dropout · learning rate scheduling · early stopping
├── Specialized       LSTM Autoencoder (anomaly) · Temporal Fusion Transformer · Seq2Seq
└── Fine-tuning       LoRA · PEFT · QLoRA · instruction tuning · RLHF fundamentals

LAYER 3 — LLMs & Foundation Models
├── Model APIs        OpenAI (GPT-4o / o1 / o3) · Anthropic (Claude) · Google (Gemini)
├── Open-weight       Llama 3 · Mistral · Qwen · Phi-3 · via Hugging Face / Ollama
├── Serving           vLLM · llama.cpp · Ollama · Text Generation Inference (TGI)
├── Evaluation        RAGAS · LangSmith · PromptFoo · G-Eval · hallucination benchmarks
└── Prompt Eng.       Chain-of-thought · few-shot · system prompt architecture · structured output

LAYER 4 — AI Agent Frameworks & Orchestration
├── Orchestration     LangChain · LangGraph (stateful multi-agent) · LlamaIndex
├── Multi-agent       CrewAI · AutoGen (Microsoft) · Agency Swarm · Phidata
├── Low-code Agents   n8n · Zapier AI · Make · Voiceflow
├── Emerging          Vercel AI SDK · Pydantic AI · DSPy · Semantic Kernel
├── Tool Use          Function calling · MCP (Model Context Protocol) · tool routing
└── Patterns          ReAct · Reflection · Plan-and-Execute · LATS · self-critique loops

LAYER 5 — RAG & Knowledge Infrastructure
├── Vector DBs        Pinecone · Weaviate · Chroma · FAISS · pgvector · Qdrant
├── Retrieval         Hybrid search (BM25 + dense) · reranking · HyDE · RAPTOR
├── Chunking          Semantic · recursive character · document hierarchy · late chunking
├── Knowledge         Neo4j (graph RAG) · knowledge graph extraction · entity linking
└── Pipelines         Ingestion · indexing · retrieval · generation · feedback loops

LAYER 6 — MLOps & Production AI
├── Experiment        MLflow · Weights & Biases · DVC · experiment versioning
├── Deployment        FastAPI · Streamlit · Gradio · Docker · Azure ML endpoints
├── Cloud             Azure ML · Azure Blob · Azure Pipelines · AWS SageMaker (working)
├── Monitoring        Data drift · concept drift · latency tracking · cost observability
└── CI/CD             GitHub Actions · model registry · automated eval pipelines

LAYER 7 — Data Engineering & Analytics
├── Languages         Python · SQL (PostgreSQL · Snowflake) · R (working knowledge)
├── Processing        Pandas · Polars · PySpark (basics) · dbt · Airflow
├── Visualization     Power BI · Tableau · Plotly · Matplotlib · Seaborn
├── Data Sources      FRED API · yfinance · Bloomberg (academic) · REST APIs · webscraping
└── Analytics Ops     Cohort analysis · funnel modeling · A/B testing · CLV · attribution
```

</div>

---

## AI Engineering Badge Wall

<div align="center">

**Agent Frameworks**

![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langchain&logoColor=00D9FF)
![LlamaIndex](https://img.shields.io/badge/LlamaIndex-8B5CF6?style=flat-square&logoColor=white)
![CrewAI](https://img.shields.io/badge/CrewAI-EF4444?style=flat-square&logoColor=white)
![AutoGen](https://img.shields.io/badge/AutoGen-0078D4?style=flat-square&logo=microsoft&logoColor=white)
![n8n](https://img.shields.io/badge/n8n-EA4B71?style=flat-square&logo=n8n&logoColor=white)
![Vercel AI SDK](https://img.shields.io/badge/Vercel%20AI%20SDK-000000?style=flat-square&logo=vercel&logoColor=white)
![Semantic Kernel](https://img.shields.io/badge/Semantic%20Kernel-5C2D91?style=flat-square&logo=microsoft&logoColor=white)
![Pydantic AI](https://img.shields.io/badge/Pydantic%20AI-E92063?style=flat-square&logoColor=white)
![DSPy](https://img.shields.io/badge/DSPy-412991?style=flat-square&logoColor=white)

**LLMs & APIs**

![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)
![Anthropic](https://img.shields.io/badge/Anthropic%20Claude-D97706?style=flat-square&logoColor=white)
![Hugging Face](https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Gemini-4285F4?style=flat-square&logo=google&logoColor=white)
![vLLM](https://img.shields.io/badge/vLLM-06B6D4?style=flat-square&logoColor=white)

**Vector & RAG Infrastructure**

![Pinecone](https://img.shields.io/badge/Pinecone-000000?style=flat-square&logoColor=white)
![Weaviate](https://img.shields.io/badge/Weaviate-4CAF50?style=flat-square&logoColor=white)
![Chroma](https://img.shields.io/badge/Chroma-F97316?style=flat-square&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-0467DF?style=flat-square&logo=meta&logoColor=white)
![pgvector](https://img.shields.io/badge/pgvector-336791?style=flat-square&logo=postgresql&logoColor=white)

**ML / Deep Learning**

![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-006600?style=flat-square&logoColor=white)
![LightGBM](https://img.shields.io/badge/LightGBM-2980B9?style=flat-square&logoColor=white)

**MLOps & Deployment**

![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white)
![Weights & Biases](https://img.shields.io/badge/W%26B-FFBE00?style=flat-square&logo=weightsandbiases&logoColor=black)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoft-azure&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

</div>

---

## GitHub Activity

<div align="center">

<img src="https://github-readme-streak-stats.herokuapp.com?user=Agent007repo&theme=tokyonight&hide_border=true&date_format=M%20j%5B%2C%20Y%5D" alt="GitHub Streak" />

<br/><br/>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Agent007repo&layout=compact&theme=tokyonight&hide_border=true&langs_count=6" height="160" alt="Top Languages"/>

<br/><br/>

<img src="https://github-profile-trophy.vercel.app/?username=Agent007repo&theme=tokyonight&no-frame=true&row=1&column=6" alt="Trophies"/>

</div>

---

## Currently Building

```python
current_stack = {
    "agentic_systems": [
        "LangGraph stateful multi-agent pipelines",
        "CrewAI role-based agent orchestration",
        "MCP server integrations for tool-augmented agents",
    ],
    "rag_and_retrieval": [
        "Hybrid BM25 + dense retrieval with reranking",
        "GraphRAG with Neo4j for knowledge-dense domains",
        "RAPTOR hierarchical indexing for long-context retrieval",
    ],
    "mlops_maturity": [
        "MLflow model registry + automated eval pipelines",
        "Drift monitoring + cost observability dashboards",
        "FastAPI model serving with Docker + Azure deployment",
    ],
    "research_frontier": [
        "Temporal Fusion Transformers for interpretable forecasting",
        "DSPy for programmatic LLM optimization",
        "RLHF annotation frameworks and preference modeling",
    ],
}
```

---

## Open To

<div align="center">

| Track | Target Roles |
|:---|:---|
| **AI / ML Engineering** | ML Engineer, AI Engineer, MLOps, Member of Technical Staff |
| **Quantitative** | Quant Researcher, Risk Modeler, Algo Strategist |
| **Analytics** | Product Analytics, Growth Analytics, Business Intelligence |
| **Product / Strategy** | PM, Revenue Ops, GTM Ops, Product Operations |
| **Technical Sales** | Solutions Engineering, Pre-Sales, Data Architecture |

*Montreal-based. Open to Canada-wide and remote. Canadian work authorization (PGWP).*

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

**If it touches data, I can build it. If it involves AI, I know where in the stack it lives.**

[![LinkedIn](https://img.shields.io/badge/Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/samarth-annigeri-14326a178/)
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=notion&logoColor=white)](https://theindianmagenta.notion.site/Product-Portfolio-f56b69796af74829a005df99d3cadf4b)

</div>
