# TrustTask — Genuine Survey & Microtask Hunter

A local intelligence application and aggregator designed to search, filter, and verify legitimate paying surveys, usability tests, AI data training annotations, and microtasks across the web, while protecting users from predatory scams and fake panels.

---

## Key Features

1. **Anti-Scam Trust Engine**:
   - Automated detection of upfront registration/starter fees (instant 100% scam flag).
   - Sanity checks on advertised compensation vs. time (flags unrealistic "$500/day for 10-minute surveys").
   - Minimum cashout threshold warning analysis.
   - Built-in domain reputation verification against reputable research panels (Prolific, UserTesting, DataAnnotation, Clickworker, Respondent, etc.).

2. **Normalized Hourly Wage Calculator**:
   - Automatically computes true effective **\$/hour** compensation so you only spend time on high-yielding opportunities.

3. **Built-in Scam Detector Tool**:
   - Paste any suspicious survey URL or job offer text to get an instant safety score (0–100%), detected red flags, and recommendations.

4. **Verified Platforms Directory**:
   - Comprehensive breakdown of reputable sites with minimum payout thresholds, supported payment methods (PayPal, Bank, Crypto), and pros & cons.

5. **Self-Contained Local Web Dashboard**:
   - Responsive UI with live search, category filters, and modal inspection views.

---

## Folder Structure

```text
survey-aggregator/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py           # REST API endpoints (/api/tasks, /api/check-url, etc.)
│   ├── services/
│   │   ├── __init__.py
│   │   ├── trust_engine.py     # Scam rules & legitimacy scoring
│   │   └── aggregator.py       # Task catalog & live web inspectors
│   ├── models.py               # Pydantic data schemas
│   └── main.py                 # FastAPI application & static mount
├── static/
│   ├── index.html              # Modern Web Dashboard
│   ├── style.css               # Styling & animations
│   └── app.js                  # Frontend client logic & filters
├── requirements.txt            # Python dependencies
├── run.py                      # One-click local server launcher
└── README.md
```

---

## How to Run Locally

### 1. Activate Environment or Install Dependencies
```powershell
cd survey-aggregator
# Using the pre-configured virtual environment:
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Launch the Application
```powershell
python run.py
```

### 3. Open in Browser
- **Dashboard**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Interactive API Docs (Swagger UI)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
