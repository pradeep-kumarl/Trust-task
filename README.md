# TrustTask — Genuine Survey & Microtask Hunter

A local intelligence application and aggregator designed to search, filter, and verify legitimate paying surveys, usability tests, AI data training annotations, and research studies across the web, prioritizing **high-yield USD earnings** payable directly to international accounts (including PayPal/Payoneer for India) while protecting users from scams and low-paying panels.

---

## Key Features

1. **High-Yield USD Focus**:
   - Curated list of verified opportunities paying **$15.00 to $100.00+ / hour**.
   - Filters out predatory or sub-dollar panels in favor of globally payable platforms.
   - International eligibility tags (US, UK, CA, AU, IN, EU, Global).

2. **Big Tech & Official Research Programs**:
   - **Google UX Research**: 1-on-1 remote feature evaluations ($50–$75/hr).
   - **Microsoft Research Panel**: AI Copilot & Windows/Office feedback ($60–$100/hr).
   - **Meta Research**: Facebook, Instagram, and WhatsApp user research ($80–$120/hr).
   - **Apple Research**: Health & movement studies via the Apple Research App.
   - **Amazon Shopper Panel**: Monthly consumer panel & receipt audits.
   - **Samsung UX Research**: Galaxy AI & hardware usability studies ($60–$100/hr).
   - **Frontier AI Training**: High-paying RLHF & evaluation for OpenAI and Anthropic models via DataAnnotation.tech and Outlier AI ($20–$40/hr).

3. **Anti-Scam Trust Engine**:
   - Automated detection of upfront registration/starter fees (instant 100% scam flag).
   - Sanity checks on advertised compensation vs. time (flags unrealistic "$500/day in 10 minutes").
   - Minimum cashout threshold warning analysis.
   - Built-in domain reputation verification against trusted research panels and big tech platforms.

4. **Normalized Hourly Wage Calculator**:
   - Automatically computes true effective **\$/hour** compensation so you prioritize only high-earning opportunities.

5. **Built-in URL & Offer Scanner**:
   - Paste any suspicious survey URL or job offer text into the dashboard to get an instant safety score (0–100%), detected red flags, and trust signals.

6. **Self-Contained Web Dashboard**:
   - Modern, responsive UI with live search, category filters, minimum hourly wage filter, and country-specific filters.

---

## Verified High-Paying Platforms (Payable to India & Global)

| Platform | Real Rates | Payment Channel | Primary Task Type |
| :--- | :--- | :--- | :--- |
| **DataAnnotation.tech** | $20 – $40 / hr | PayPal | AI Model Evaluation & Coding |
| **Outlier AI** | $15 – $40 / hr | PayPal | RLHF, Reasoning, & Fact-checking |
| **UserTesting** | $10 – $60 / test | PayPal | Website & App Prototype Usability |
| **Respondent.io** | $50 – $150 / hr | PayPal | 1-on-1 Tech & Business Interviews |
| **Google UX Research** | $50 – $100 / hr | Amazon / Visa Gift Cards | Remote Product Discovery Sessions |
| **Microsoft Research** | $60 – $100 / hr | Amazon Cards / MS Rewards | Copilot & Office Tooling Studies |
| **Meta Research** | $60 – $120 / hr | PayPal / Visa Gift Cards | Social & Messaging Product Feedback |

---

## Folder Structure

```text
survey-aggregator/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py           # REST API endpoints (/api/tasks, /api/platforms, /api/check-url, etc.)
│   ├── services/
│   │   ├── __init__.py
│   │   ├── trust_engine.py     # Scam rules & domain verification logic
│   │   └── aggregator.py       # Curated tasks repository & platforms directory
│   ├── models.py               # Pydantic data schemas
│   └── main.py                 # FastAPI application & static mount
├── static/
│   ├── index.html              # Modern Web Dashboard
│   ├── style.css               # Styling & responsive design
│   └── app.js                  # Frontend client logic & filters
├── requirements.txt            # Python dependencies
├── run.py                      # Local server launcher
├── test_endpoints.py           # Comprehensive backend test suite
└── README.md
```

---

## How to Run Locally

### Location on Machine
```powershell
D:\projects\survey-aggregator
```

### 1. Launch the Server
Using the pre-configured virtual environment on your system:
```powershell
cd D:\projects\survey-aggregator
.\venv\Scripts\python.exe run.py
```

Or activate the environment:
```powershell
cd D:\projects\survey-aggregator
.\venv\Scripts\Activate.ps1
python run.py
```

### 2. Access the Application
- **Web Dashboard**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Interactive API Docs (Swagger UI)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 3. Run Test Suite
```powershell
.\venv\Scripts\python.exe test_endpoints.py
```
*(All 8 endpoint and validation tests pass cleanly).*
