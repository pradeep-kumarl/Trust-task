import re
from typing import List, Dict, Any, Tuple
from urllib.parse import urlparse
from app.models import ScamCheckResponse, RiskLevel

# Verified legitimate platforms database
VERIFIED_DOMAINS = {
    "prolific.com": {"name": "Prolific", "trust": 98, "badge": "Gold Standard (Academic)"},
    "usertesting.com": {"name": "UserTesting", "trust": 96, "badge": "Verified UX Testing"},
    "dataannotation.tech": {"name": "DataAnnotation.tech", "trust": 95, "badge": "Verified AI Training"},
    "outlier.ai": {"name": "Outlier.ai", "trust": 92, "badge": "Verified AI Training"},
    "clickworker.com": {"name": "Clickworker", "trust": 90, "badge": "Established Microtasks"},
    "mturk.com": {"name": "Amazon MTurk", "trust": 88, "badge": "Amazon Backed"},
    "respondent.io": {"name": "Respondent", "trust": 94, "badge": "High Payout Research"},
    "dscout.com": {"name": "Dscout", "trust": 93, "badge": "Verified Diary Studies"},
    "pineconeresearch.com": {"name": "Pinecone Research", "trust": 91, "badge": "Established Survey Panel"},
    "freecash.com": {"name": "Freecash", "trust": 86, "badge": "Verified Offerwall & Surveys"},
    "swagbucks.com": {"name": "Swagbucks", "trust": 87, "badge": "Prodege Verified"},
    "yougov.com": {"name": "YouGov", "trust": 92, "badge": "Global Public Research"},
    "testingtime.com": {"name": "TestingTime", "trust": 93, "badge": "European UX Research"},
    "neevo.defined.ai": {"name": "Neevo", "trust": 85, "badge": "AI Voice & Text Tasks"},
    "remotasks.com": {"name": "Remotasks", "trust": 86, "badge": "Scale AI Platform"},
    "userresearch.google.com": {"name": "Google UX Research", "trust": 99, "badge": "Google Official"},
    "google.com": {"name": "Google", "trust": 99, "badge": "Google Official"},
    "microsoft.com": {"name": "Microsoft Research", "trust": 99, "badge": "Microsoft Official"},
    "apple.com": {"name": "Apple Research", "trust": 98, "badge": "Apple Official"},
    "facebook.com": {"name": "Meta Research", "trust": 97, "badge": "Meta Official"},
    "amazonshopper.com": {"name": "Amazon Shopper Panel", "trust": 97, "badge": "Amazon Official"},
    "samsung.com": {"name": "Samsung UX Research", "trust": 96, "badge": "Samsung Official"}
}

# Explicit scam keywords
SCAM_TRIGGERS = [
    (r"(registration|membership|starter|kit|activation)\s+fee", "Demands upfront payment or registration fee (100% scam sign)"),
    (r"pay\s+\$\d+\s+to\s+(start|access|unlock|join)", "Asks for money before allowing you to work"),
    (r"wire\s+transfer|western\s+union|moneygram", "Requests untraceable payment services"),
    (r"earn\s+\$(?:100|200|300|500|1000)\s+(?:per\s+hour|a\s+day|in\s+minutes)", "Promised earnings are astronomically unrealistic for basic surveys"),
    (r"credit\s+card\s+number\s+required\s+to\s+register", "Demands payment card details during signup"),
    (r"minimum\s+(cashout|withdrawal)\s+\$(?:100|150|200)", "Excessively high minimum cashout threshold designed to trap worker balances"),
    (r"guaranteed\s+(wealth|rich|passive\s+income)", "Uses get-rich-quick predatory language")
]

# Genuine indicators
TRUST_SIGNALS = [
    (r"paypal|direct\s+deposit|bank\s+transfer|wise", "Offers standard, secure payment channels (PayPal, Bank Deposit)"),
    (r"academic\s+research|university|irb\s+approved", "Conducted by accredited universities or institutional review boards"),
    (r"no\s+(payment|fee|credit\s+card)\s+required", "Explicitly confirms zero cost to workers"),
    (r"privacy\s+policy|terms\s+of\s+service|gdpr", "Publishes standard legal and data privacy policies"),
    (r"per\s+hour:\s*\$(?:6|8|10|12|15|20|25|30)", "Realistic transparent wage bracket aligned with industry standards")
]

class TrustEngine:
    @staticmethod
    def extract_domain(url: str) -> str:
        """Extract root domain from URL."""
        if not url:
            return ""
        try:
            parsed = urlparse(url if "://" in url else f"https://{url}")
            domain = parsed.netloc.lower()
            if domain.startswith("www."):
                domain = domain[4:]
            return domain
        except Exception:
            return ""

    @classmethod
    def calculate_hourly_rate(cls, reward: float, minutes: int) -> float:
        """Calculate normalized USD hourly rate."""
        if minutes <= 0:
            return 0.0
        return round((reward / minutes) * 60, 2)

    @classmethod
    def analyze_content(cls, text: str, url: str = "") -> ScamCheckResponse:
        """Analyze text and URL for scam indicators and trust signals."""
        red_flags: List[str] = []
        trust_signals: List[str] = []
        base_score = 70  # Neutral starting point
        
        domain = cls.extract_domain(url)
        known_platform = None

        # 1. Check known domain database
        for verified_dom, meta in VERIFIED_DOMAINS.items():
            if domain == verified_dom or domain.endswith("." + verified_dom):
                known_platform = meta
                base_score = meta["trust"]
                trust_signals.append(f"Domain matches verified platform: {meta['name']} ({meta['badge']})")
                break

        full_text = f"{text or ''} {url or ''}".lower()

        # 2. Check for Scam triggers
        for pattern, explanation in SCAM_TRIGGERS:
            if re.search(pattern, full_text):
                red_flags.append(explanation)
                base_score -= 35

        # 3. Check for Trust signals
        for pattern, explanation in TRUST_SIGNALS:
            if re.search(pattern, full_text):
                trust_signals.append(explanation)
                base_score += 6

        # 4. Check for Hourly Rate sanity if numbers are present
        rate_matches = re.findall(r"\$(\d+(?:\.\d{2})?)\s*(?:for|\/)\s*(\d+)\s*(?:min|minute)", full_text)
        if rate_matches:
            pay, mins = float(rate_matches[0][0]), float(rate_matches[0][1])
            if mins > 0:
                hourly = (pay / mins) * 60
                if hourly > 80 and not any(kw in full_text for kw in ["software", "ai training", "developer", "expert"]):
                    red_flags.append(f"Calculated rate (${hourly:.2f}/hr) is suspiciously high for simple task")
                    base_score -= 25
                elif 5 <= hourly <= 40:
                    trust_signals.append(f"Fair, realistic compensation rate detected (~${hourly:.2f}/hr)")
                    base_score += 8

        # Clamp score between 0 and 100
        final_score = max(0, min(100, base_score))

        # Risk classification
        if final_score >= 80 and len(red_flags) == 0:
            verdict = "Genuine & Verified"
            risk_level = RiskLevel.SAFE
            is_safe = True
            recommendation = "Safe to participate. Platform maintains legitimate payout proof and zero upfront charges."
        elif final_score >= 50 and len(red_flags) <= 1:
            verdict = "Proceed With Caution"
            risk_level = RiskLevel.CAUTION
            is_safe = True
            recommendation = "Review payout thresholds and never provide sensitive personal or payment card data."
        else:
            verdict = "High Scam Risk"
            risk_level = RiskLevel.DANGER
            is_safe = False
            recommendation = "Do not register or deposit any funds. Severe scam warning flags detected."

        return ScamCheckResponse(
            score=final_score,
            verdict=verdict,
            risk_level=risk_level,
            is_safe=is_safe,
            detected_red_flags=red_flags,
            trust_signals=trust_signals,
            recommendation=recommendation,
            analysis_details={
                "domain": domain,
                "is_whitelisted": known_platform is not None,
                "platform_name": known_platform["name"] if known_platform else "Independent/Unverified Site"
            }
        )
