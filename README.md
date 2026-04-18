<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=180&section=header&text=Samarth%20Annigeri&fontSize=42&fontColor=fff&animation=twinkling&fontAlignY=32&desc=Machine%20Learning%20%E2%80%A2%20AI%20Systems%20%E2%80%A2%20Data%20Architecture%20%E2%80%A2%20Product&descAlignY=55&descSize=16" width="100%"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&pause=1200&color=00D9FF&center=true&vCenter=true&width=800&lines=Building+production+ML+pipelines+that+ship.;From+LSTM+autoencoders+to+Azure+deployments.;Credit+risk+%7C+Supply+chain+%7C+Quant+finance+%7C+NLP.;McGill+MMA+%7C+BNP+Paribas+%7C+Montreal+%F0%9F%87%A8%F0%9F%87%A6" alt="Typing SVG" />

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

I design and ship **production ML systems** at the intersection of quantitative analysis, AI engineering, and business strategy. My work spans credit risk (ARIMA pipelines in Azure), supply chain intelligence (LSTM + LightGBM multi-horizon forecasting), and quantitative investment (alpha generation on 147 stock characteristics).

I think in systems, not scripts. Every model I build has a deployment story, a monitoring plan, and a business metric it moves.

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

## Technical Depth

<div align="center">

```
Core ML / AI
├── Supervised        XGBoost · LightGBM · Random Forest · Ridge / LASSO / ElasticNet
├── Deep Learning     LSTM · Autoencoder · Residual Neural Nets (TensorFlow / Keras)
├── Causal Inference  CausalML · DoWhy · DiD · Propensity Scoring · Refutation Testing
├── NLP               VADER · BERT (fine-tuned) · LangChain · RAG Pipelines
├── Time Series       ARIMA · Seasonal Decomp · Multi-horizon Forecasting (7/14/30d)
└── Unsupervised      Louvain Community Detection · PageRank · LSTM Anomaly Detection

MLOps & Infrastructure
├── Cloud             Azure ML · Azure Blob Storage · Azure Pipelines
├── Tracking          MLflow · Experiment versioning · Model registry
├── Orchestration     n8n · Python ML workflows · Batch + near-real-time
└── Infra             Git · Jupyter · Docker (basics) · FRED API · yfinance

Analytics & BI
├── Languages         Python · SQL (PostgreSQL) · R (working knowledge)
├── Visualization     Power BI · Tableau · Plotly · Matplotlib · Seaborn
└── Methods           Cohort analysis · Funnel modeling · A/B testing · CLV modeling

Product & Strategy
├── Frameworks        PRDs · Roadmapping · OKRs · Jobs-to-be-Done
├── Tools             Notion · Linear · Figma (wireframes) · Mixpanel
└── Domains           FinTech · Supply Chain · MarTech · Growth
```

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
focus_2025 = {
    "MLOps":       ["MLflow experiment tracking", "model versioning", "deployment pipelines"],
    "LLM_Arch":    ["RAG systems", "agentic frameworks", "multi-step reasoning pipelines"],
    "Automation":  ["n8n AI-augmented workflows", "data ingestion pipelines"],
    "Research":    ["Temporal Fusion Transformers", "interpretable multi-horizon forecasting"],
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

**If it touches data, I can build it. If it ships, I've probably already broken and fixed it.**

[![LinkedIn](https://img.shields.io/badge/Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/samarth-annigeri-14326a178/)
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=notion&logoColor=white)](https://theindianmagenta.notion.site/Product-Portfolio-f56b69796af74829a005df99d3cadf4b)

</div>
