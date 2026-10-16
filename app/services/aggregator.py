import httpx
from bs4 import BeautifulSoup
from typing import List, Optional
from app.models import Task, Platform, RiskLevel
from app.services.trust_engine import TrustEngine, VERIFIED_DOMAINS

# ──────────────────────────────────────────────────────────────────────────────
# VERIFIED CURATED TASK REPOSITORY  (35+ tasks across all regions)
# ──────────────────────────────────────────────────────────────────────────────
CURATED_TASKS: List[Task] = [

    # ══ GLOBAL / WESTERN ════════════════════════════════════════════════════

    Task(
        id="task-prolific-01",
        title="Consumer Financial Decision Making in Digital Markets",
        description="Academic research study exploring how individuals evaluate digital financial products and compare interest rates.",
        platform="Prolific", platform_url="https://www.prolific.com",
        category="survey", reward_amount=7.50, currency="GBP",
        estimated_minutes=25, hourly_rate_usd=23.40, trust_score=98, verified=True,
        payment_methods=["PayPal"],
        eligible_countries=["US", "UK", "CA", "AU", "DE", "FR", "NL", "PL", "IE"],
        min_age=18, requirements=["Desktop/Laptop", "Good approval rating (>98%)"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://app.prolific.com/studies", date_posted="2026-10-16"
    ),
    Task(
        id="task-prolific-02",
        title="Online Social Behaviour & Digital Privacy Attitudes Study",
        description="Questionnaire examining social media usage, data privacy awareness, and attitudes toward algorithmic curation. Desktop preferred.",
        platform="Prolific", platform_url="https://www.prolific.com",
        category="survey", reward_amount=5.00, currency="GBP",
        estimated_minutes=18, hourly_rate_usd=21.60, trust_score=98, verified=True,
        payment_methods=["PayPal"],
        eligible_countries=["US", "UK", "CA", "AU", "DE", "FR", "NL"],
        min_age=18, requirements=["18-45 age group preferred", "Active social media user"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://app.prolific.com/studies", date_posted="2026-10-17"
    ),
    Task(
        id="task-usertesting-01",
        title="Mobile Banking App Navigation & UX Testing",
        description="Speak-out-loud prototype usability test. Navigate wireframes and provide feedback on layout clarity.",
        platform="UserTesting", platform_url="https://www.usertesting.com",
        category="usability_testing", reward_amount=30.00, currency="USD",
        estimated_minutes=30, hourly_rate_usd=60.00, trust_score=96, verified=True,
        payment_methods=["PayPal"],
        eligible_countries=["US", "UK", "CA", "AU", "DE", "IN"],
        min_age=18, requirements=["Microphone", "Screen recording consent", "Fluent English"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://www.usertesting.com/get-paid-to-test", date_posted="2026-10-16"
    ),
    Task(
        id="task-usertesting-02",
        title="Smart Home Device Setup & Onboarding Experience Test",
        description="Unbox a simulated smart thermostat app. Walk through installation steps and share first-impressions aloud.",
        platform="UserTesting", platform_url="https://www.usertesting.com",
        category="usability_testing", reward_amount=10.00, currency="USD",
        estimated_minutes=20, hourly_rate_usd=30.00, trust_score=96, verified=True,
        payment_methods=["PayPal"],
        eligible_countries=["US", "UK", "CA", "AU", "IN", "Global"],
        min_age=18, requirements=["Microphone", "iOS or Android phone"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://www.usertesting.com/get-paid-to-test", date_posted="2026-10-15"
    ),
    Task(
        id="task-userlytics-01",
        title="E-Learning Platform Navigation Feedback (Unmoderated)",
        description="Explore an online course marketplace, attempt to find and enrol in a specific course, then answer post-test survey questions.",
        platform="Userlytics", platform_url="https://www.userlytics.com",
        category="usability_testing", reward_amount=12.00, currency="USD",
        estimated_minutes=20, hourly_rate_usd=36.00, trust_score=88, verified=True,
        payment_methods=["PayPal"],
        eligible_countries=["US", "UK", "CA", "AU", "IN", "SG", "Global"],
        min_age=18, requirements=["Webcam preferred", "Fluent English"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://www.userlytics.com/participate", date_posted="2026-10-16"
    ),
    Task(
        id="task-dataannotation-01",
        title="AI Response Evaluation & Fact-Checking (Core)",
        description="Compare two AI chatbot answers for accuracy, tone, and safety compliance. Annotate discrepancies.",
        platform="DataAnnotation.tech", platform_url="https://www.dataannotation.tech",
        category="ai_annotation", reward_amount=20.00, currency="USD",
        estimated_minutes=60, hourly_rate_usd=20.00, trust_score=95, verified=True,
        payment_methods=["PayPal"],
        eligible_countries=["US", "UK", "CA", "AU", "NZ", "IE", "IN"],
        min_age=18, requirements=["Pass initial skills assessment", "Detail-oriented writing"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://www.dataannotation.tech", date_posted="2026-10-15"
    ),
    Task(
        id="task-dataannotation-02",
        title="Python & JavaScript Code Bug Identification for AI Training",
        description="Review AI-generated code snippets, identify logical errors, suggest corrections, and score overall quality.",
        platform="DataAnnotation.tech", platform_url="https://www.dataannotation.tech",
        category="ai_annotation", reward_amount=35.00, currency="USD",
        estimated_minutes=90, hourly_rate_usd=23.33, trust_score=95, verified=True,
        payment_methods=["PayPal"],
        eligible_countries=["US", "UK", "CA", "AU", "IN", "DE", "Global"],
        min_age=18, requirements=["Programming background (Python/JS)", "Skills test required"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://www.dataannotation.tech", date_posted="2026-10-17"
    ),
    Task(
        id="task-respondent-01",
        title="Developer Experience & Cloud Tooling Feedback Session",
        description="1-on-1 moderated video call with product researchers discussing cloud CI/CD pipelines.",
        platform="Respondent", platform_url="https://www.respondent.io",
        category="focus_group", reward_amount=120.00, currency="USD",
        estimated_minutes=45, hourly_rate_usd=160.00, trust_score=94, verified=True,
        payment_methods=["PayPal"],
        eligible_countries=["US", "UK", "CA", "AU", "IN", "SG", "DE"],
        min_age=18, requirements=["Webcam & Mic", "Software development / DevOps background"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://www.respondent.io/respondents", date_posted="2026-10-15"
    ),
    Task(
        id="task-respondent-02",
        title="SaaS Product Manager 45-min Interview ($150)",
        description="Participate in a product discovery session about project management tools. Requires 2+ years PM experience.",
        platform="Respondent", platform_url="https://www.respondent.io",
        category="focus_group", reward_amount=150.00, currency="USD",
        estimated_minutes=45, hourly_rate_usd=200.00, trust_score=94, verified=True,
        payment_methods=["PayPal"],
        eligible_countries=["US", "UK", "CA", "AU", "IN", "SG"],
        min_age=21, requirements=["2+ years Product Management experience", "Webcam & Microphone"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://www.respondent.io/respondents", date_posted="2026-10-17"
    ),
    Task(
        id="task-clickworker-01",
        title="Search Engine Relevance & Web Classification (UHRS)",
        description="Label search results based on user query intent. Short 30-second micro-assessments.",
        platform="Clickworker", platform_url="https://www.clickworker.com",
        category="microtask", reward_amount=4.80, currency="USD",
        estimated_minutes=20, hourly_rate_usd=14.40, trust_score=90, verified=True,
        payment_methods=["PayPal", "Payoneer", "SEPA"],
        eligible_countries=["Global"],
        min_age=18, requirements=["Web browser", "UHRS qualification test"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://www.clickworker.com/clickworker/", date_posted="2026-10-14"
    ),
    Task(
        id="task-dscout-01",
        title="Weekly Healthy Cooking & Grocery Habits Video Diary",
        description="Record three 2-minute video clips showing food preparation and grocery receipts over 4 days.",
        platform="Dscout", platform_url="https://www.dscout.com",
        category="focus_group", reward_amount=70.00, currency="USD",
        estimated_minutes=50, hourly_rate_usd=84.00, trust_score=93, verified=True,
        payment_methods=["PayPal"],
        eligible_countries=["US", "UK", "CA"],
        min_age=18, requirements=["Smartphone app", "Front-facing camera"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://dscout.com/be-a-scout", date_posted="2026-10-16"
    ),
    Task(
        id="task-pinecone-01",
        title="Household Product Packaging & Brand Concept Survey",
        description="Evaluate concepts for upcoming eco-friendly cleaning solutions and packaging.",
        platform="Pinecone Research", platform_url="https://www.pineconeresearch.com",
        category="survey", reward_amount=3.00, currency="USD",
        estimated_minutes=12, hourly_rate_usd=15.00, trust_score=91, verified=True,
        payment_methods=["Direct Deposit", "PayPal", "Gift Card"],
        eligible_countries=["US", "UK", "CA", "FR", "DE", "AU"],
        min_age=18, requirements=["Panel membership confirmation"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://www.pineconeresearch.com", date_posted="2026-10-15"
    ),
    Task(
        id="task-freecash-01",
        title="Fintech Mobile App Verification & Onboarding Survey",
        description="Install partner financial tracker, complete basic profile setup and submit in-app survey.",
        platform="Freecash", platform_url="https://www.freecash.com",
        category="microtask", reward_amount=8.50, currency="USD",
        estimated_minutes=25, hourly_rate_usd=20.40, trust_score=86, verified=True,
        payment_methods=["PayPal", "Crypto", "Visa Prepaid", "Bank Transfer"],
        eligible_countries=["Global"],
        min_age=16, requirements=["iOS or Android Device"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=["Offers vary by region"],
        direct_apply_url="https://freecash.com", date_posted="2026-10-16"
    ),
    Task(
        id="task-swagbucks-01",
        title="Daily Survey Pack — 3 Consumer Opinion Surveys",
        description="Complete a bundle of 3 short consumer surveys on food brands, streaming services, and travel intent.",
        platform="Swagbucks", platform_url="https://www.swagbucks.com",
        category="survey", reward_amount=2.00, currency="USD",
        estimated_minutes=15, hourly_rate_usd=8.00, trust_score=87, verified=True,
        payment_methods=["PayPal", "Gift Card"],
        eligible_countries=["US", "UK", "CA", "AU", "IN", "Global"],
        min_age=13, requirements=["Free account signup"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=["Disqualification from some surveys is common"],
        direct_apply_url="https://www.swagbucks.com/surveys", date_posted="2026-10-17"
    ),
    Task(
        id="task-scaleai-01",
        title="Medical Imaging Annotation for AI Diagnostics (Scale AI)",
        description="Draw segmentation masks around anatomical features in de-identified X-ray and MRI images for healthcare AI training.",
        platform="Scale AI", platform_url="https://scale.com",
        category="ai_annotation", reward_amount=25.00, currency="USD",
        estimated_minutes=60, hourly_rate_usd=25.00, trust_score=91, verified=True,
        payment_methods=["PayPal", "Payoneer"],
        eligible_countries=["US", "UK", "CA", "IN", "PH", "Global"],
        min_age=18, requirements=["Attention to detail", "Annotation qualification pass"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://scale.com/jobs", date_posted="2026-10-16"
    ),
    Task(
        id="task-lionbridge-01",
        title="Ads & Web Content Quality Rater (Work From Home)",
        description="Rate internet ads, web search results, and AI assistant responses for relevance and quality. Flexible self-paced hours.",
        platform="Lionbridge", platform_url="https://www.lionbridge.com",
        category="ai_annotation", reward_amount=14.00, currency="USD",
        estimated_minutes=60, hourly_rate_usd=14.00, trust_score=89, verified=True,
        payment_methods=["PayPal"],
        eligible_countries=["US", "UK", "CA", "AU", "IN", "DE", "Global"],
        min_age=18, requirements=["Pass Search Quality Rater exam", "Stable internet connection"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://www.lionbridge.com/be-a-lionbridge-ai-trainer/", date_posted="2026-10-15"
    ),
    Task(
        id="task-surgeai-01",
        title="Conversation Dataset Quality Review & Labelling",
        description="Review human-to-AI conversation transcripts, tag intents, flag unsafe outputs, and score overall quality.",
        platform="Surge AI", platform_url="https://www.surgehq.ai",
        category="ai_annotation", reward_amount=12.00, currency="USD",
        estimated_minutes=45, hourly_rate_usd=16.00, trust_score=87, verified=True,
        payment_methods=["PayPal"],
        eligible_countries=["US", "UK", "CA", "AU", "IN", "Global"],
        min_age=18, requirements=["Strong English reading comprehension", "Qualification task"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://app.surgehq.ai/workers/signup", date_posted="2026-10-14"
    ),
    Task(
        id="task-trymyui-01",
        title="Travel Booking Website Usability Test (Unmoderated)",
        description="Search for and attempt to book a flight on a prototype travel site. Record your screen and think aloud.",
        platform="TryMyUI", platform_url="https://www.trymyui.com",
        category="usability_testing", reward_amount=10.00, currency="USD",
        estimated_minutes=20, hourly_rate_usd=30.00, trust_score=85, verified=True,
        payment_methods=["PayPal"],
        eligible_countries=["US", "UK", "CA", "AU", "IN", "Global"],
        min_age=18, requirements=["Microphone", "Desktop or laptop"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://www.trymyui.com/take-part-in-studies", date_posted="2026-10-16"
    ),
    Task(
        id="task-enroll-01",
        title="Healthcare App Diary Study — Chronic Condition Tracking",
        description="Use a prototype chronic illness management app daily for 7 days and submit nightly diary entries about your experience.",
        platform="Enroll", platform_url="https://www.enrollapp.com",
        category="focus_group", reward_amount=90.00, currency="USD",
        estimated_minutes=70, hourly_rate_usd=77.14, trust_score=88, verified=True,
        payment_methods=["PayPal", "Visa Gift Card"],
        eligible_countries=["US", "UK", "CA"],
        min_age=18, requirements=["iOS or Android device", "Lives with a chronic health condition"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://www.enrollapp.com", date_posted="2026-10-15"
    ),
    Task(
        id="task-yougov-us-01",
        title="US Political Attitudes & Election Outlook Survey",
        description="Share your political views, party alignment, and voting intentions in this quarterly YouGov panel survey.",
        platform="YouGov US", platform_url="https://today.yougov.com",
        category="survey", reward_amount=1.00, currency="USD",
        estimated_minutes=7, hourly_rate_usd=8.57, trust_score=92, verified=True,
        payment_methods=["Gift Card", "PayPal"],
        eligible_countries=["US"],
        min_age=18, requirements=["US resident"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://today.yougov.com/register", date_posted="2026-10-17"
    ),

    # ══ INDIA-FOCUSED ════════════════════════════════════════════════════════

    Task(
        id="task-mturk-in-01",
        title="Product Image Tagging & Object Detection (MTurk HIT)",
        description="Label objects in product photographs for e-commerce AI training. Draw bounding boxes on clothing, electronics, or furniture.",
        platform="Amazon Mechanical Turk", platform_url="https://www.mturk.com",
        category="ai_annotation", reward_amount=2.50, currency="USD",
        estimated_minutes=15, hourly_rate_usd=10.00, trust_score=88, verified=True,
        payment_methods=["Amazon Gift Card", "Bank Transfer (IN)"],
        eligible_countries=["IN", "US", "PH", "BD", "Global"],
        min_age=18, requirements=["MTurk Worker account", "English literacy"],
        scam_risk_level=RiskLevel.SAFE,
        scam_warnings=["Indian workers paid via Amazon.in gift cards"],
        direct_apply_url="https://worker.mturk.com", date_posted="2026-10-16"
    ),
    Task(
        id="task-neevo-in-01",
        title="Hindi & Tamil Speech Recording for Voice AI Dataset",
        description="Read 200 short Hindi and Tamil sentences aloud. Used to train regional speech recognition models.",
        platform="Neevo (Defined.ai)", platform_url="https://neevo.defined.ai",
        category="ai_annotation", reward_amount=6.00, currency="USD",
        estimated_minutes=30, hourly_rate_usd=12.00, trust_score=85, verified=True,
        payment_methods=["PayPal", "Bank Transfer"],
        eligible_countries=["IN", "Global"],
        min_age=18, requirements=["Quiet room", "Microphone", "Native Hindi/Tamil speaker"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://neevo.defined.ai", date_posted="2026-10-16"
    ),
    Task(
        id="task-neevo-in-02",
        title="Bengali & Marathi Text Translation & Correction Task",
        description="Translate 50 English sentences into Bengali or Marathi and verify machine-translated outputs for fluency.",
        platform="Neevo (Defined.ai)", platform_url="https://neevo.defined.ai",
        category="ai_annotation", reward_amount=8.00, currency="USD",
        estimated_minutes=40, hourly_rate_usd=12.00, trust_score=85, verified=True,
        payment_methods=["PayPal", "Bank Transfer"],
        eligible_countries=["IN", "Global"],
        min_age=18, requirements=["Native Bengali or Marathi speaker", "Translation proficiency"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://neevo.defined.ai", date_posted="2026-10-17"
    ),
    Task(
        id="task-remotasks-in-01",
        title="LiDAR Point Cloud Annotation for Autonomous Vehicles",
        description="Annotate 3D LiDAR scans from self-driving car sensors. Mark pedestrians, vehicles, and road objects.",
        platform="Remotasks", platform_url="https://www.remotasks.com",
        category="ai_annotation", reward_amount=15.00, currency="USD",
        estimated_minutes=60, hourly_rate_usd=15.00, trust_score=86, verified=True,
        payment_methods=["PayPal", "Payoneer"],
        eligible_countries=["IN", "PH", "KE", "NG", "VN", "Global"],
        min_age=18, requirements=["Desktop/Laptop", "Pass annotation bootcamp training"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://www.remotasks.com", date_posted="2026-10-15"
    ),
    Task(
        id="task-yougov-in-01",
        title="Consumer Electronics Purchase Intent Survey (India)",
        description="Share your smartphone buying habits, brand preferences, and budget range.",
        platform="YouGov India", platform_url="https://india.yougov.com",
        category="survey", reward_amount=1.50, currency="USD",
        estimated_minutes=10, hourly_rate_usd=9.00, trust_score=92, verified=True,
        payment_methods=["Amazon Voucher", "Flipkart Voucher", "PayPal"],
        eligible_countries=["IN"],
        min_age=18, requirements=["Indian resident"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://india.yougov.com/en-in/account/register/", date_posted="2026-10-16"
    ),
    Task(
        id="task-toluna-in-01",
        title="India Food Delivery App Usage & Satisfaction Survey",
        description="Share your Zomato/Swiggy order habits, satisfaction ratings, and feature requests.",
        platform="Toluna India", platform_url="https://in.toluna.com",
        category="survey", reward_amount=1.20, currency="USD",
        estimated_minutes=8, hourly_rate_usd=9.00, trust_score=83, verified=True,
        payment_methods=["Amazon Voucher", "Paytm", "PayPal"],
        eligible_countries=["IN"],
        min_age=18, requirements=["Indian resident", "Has used food delivery apps"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://in.toluna.com/register", date_posted="2026-10-15"
    ),
    Task(
        id="task-panelstation-in-01",
        title="India OTT Streaming Habits & Subscription Survey",
        description="Tell us about your Netflix, Amazon Prime, Hotstar viewing patterns, subscription spending, and content preferences.",
        platform="The Panel Station India", platform_url="https://www.thepanelstation.com",
        category="survey", reward_amount=1.00, currency="USD",
        estimated_minutes=8, hourly_rate_usd=7.50, trust_score=82, verified=True,
        payment_methods=["Paytm", "Amazon Pay", "PayPal"],
        eligible_countries=["IN"],
        min_age=18, requirements=["Indian resident", "Has OTT subscription"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://www.thepanelstation.com/register", date_posted="2026-10-16"
    ),
    Task(
        id="task-ipanel-in-01",
        title="Indian Banking & UPI Payments Experience Survey",
        description="Share your UPI app usage (GPay/PhonePe/BHIM), digital payment frequency, and banking satisfaction.",
        platform="iPanel Online India", platform_url="https://www.ipanelonline.com",
        category="survey", reward_amount=0.80, currency="USD",
        estimated_minutes=7, hourly_rate_usd=6.86, trust_score=80, verified=True,
        payment_methods=["Paytm", "Bank Transfer"],
        eligible_countries=["IN"],
        min_age=18, requirements=["Indian resident", "Uses UPI payments"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=["Low payout; suited for occasional side income"],
        direct_apply_url="https://www.ipanelonline.com/in/survey", date_posted="2026-10-15"
    ),
    Task(
        id="task-outlier-in-01",
        title="Creative Writing Prompt Evaluation & AI Model Feedback",
        description="Review AI-generated stories and poems. Rate creativity, coherence, and factual accuracy.",
        platform="Outlier AI", platform_url="https://outlier.ai",
        category="ai_annotation", reward_amount=18.00, currency="USD",
        estimated_minutes=60, hourly_rate_usd=18.00, trust_score=92, verified=True,
        payment_methods=["PayPal"],
        eligible_countries=["IN", "US", "UK", "CA", "AU", "PH", "Global"],
        min_age=18, requirements=["Strong English writing skills", "Skills assessment required"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://outlier.ai/contributors", date_posted="2026-10-16"
    ),
    Task(
        id="task-microworkers-in-01",
        title="Google Maps Business Listing Verification (India Local)",
        description="Verify business name, address, phone number, and hours on Google Maps for local Indian businesses.",
        platform="Microworkers", platform_url="https://www.microworkers.com",
        category="microtask", reward_amount=0.80, currency="USD",
        estimated_minutes=5, hourly_rate_usd=9.60, trust_score=78, verified=True,
        payment_methods=["PayPal", "Payoneer", "Skrill"],
        eligible_countries=["IN", "PH", "BD", "PK", "VN", "Global"],
        min_age=18, requirements=["Smartphone with GPS"],
        scam_risk_level=RiskLevel.SAFE,
        scam_warnings=["Low per-task pay; stack multiple tasks"],
        direct_apply_url="https://www.microworkers.com/register.php", date_posted="2026-10-14"
    ),
    Task(
        id="task-valued-in-01",
        title="FMCG Brand Awareness & Purchase Behaviour Survey (India)",
        description="Rate your awareness and usage of popular FMCG brands across personal care, food, and beverages.",
        platform="Valued Opinions India", platform_url="https://www.valuedopinions.co.in",
        category="survey", reward_amount=1.20, currency="USD",
        estimated_minutes=10, hourly_rate_usd=7.20, trust_score=82, verified=True,
        payment_methods=["Amazon Voucher", "Myntra Voucher", "Paytm"],
        eligible_countries=["IN"],
        min_age=18, requirements=["Indian resident"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://www.valuedopinions.co.in/register", date_posted="2026-10-17"
    ),
    Task(
        id="task-ysense-in-01",
        title="Lifestyle & Health Habit Survey Bundle (ySense India)",
        description="Complete a 3-survey pack covering exercise habits, dietary choices, and health app usage.",
        platform="ySense", platform_url="https://www.ysense.com",
        category="survey", reward_amount=2.50, currency="USD",
        estimated_minutes=18, hourly_rate_usd=8.33, trust_score=84, verified=True,
        payment_methods=["PayPal", "Skrill", "Gift Card"],
        eligible_countries=["IN", "US", "UK", "CA", "AU", "Global"],
        min_age=16, requirements=["Free ySense account"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://www.ysense.com/register", date_posted="2026-10-16"
    ),

    # ══ SOUTHEAST ASIA / PHILIPPINES ════════════════════════════════════════

    Task(
        id="task-appen-ph-01",
        title="Social Media Content Relevance Rating (Philippines/Global)",
        description="Rate whether social media posts and ads are relevant to given user profiles. Flexible hours.",
        platform="Appen", platform_url="https://appen.com",
        category="ai_annotation", reward_amount=5.00, currency="USD",
        estimated_minutes=30, hourly_rate_usd=10.00, trust_score=84, verified=True,
        payment_methods=["PayPal", "Payoneer"],
        eligible_countries=["PH", "IN", "AU", "US", "UK", "Global"],
        min_age=18, requirements=["Pass qualification test", "Native/fluent language speaker"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://connect.appen.com/qrp/public/jobs", date_posted="2026-10-15"
    ),

    # ══ BIG TECH / GENUINE LARGE COMPANIES ══════════════════════════════════

    Task(
        id="task-google-uxr-01",
        title="Google UX Research Study — Search & AI Features Feedback",
        description="Participate in a 1-on-1 remote session with Google's UX Research team. Share your experience using Google Search, Bard/Gemini, or Chrome features. Session conducted via Google Meet.",
        platform="Google UX Research", platform_url="https://userresearch.google.com",
        category="usability_testing", reward_amount=75.00, currency="USD",
        estimated_minutes=60, hourly_rate_usd=75.00, trust_score=99, verified=True,
        payment_methods=["Amazon Gift Card", "Visa Gift Card"],
        eligible_countries=["US", "UK", "CA", "AU", "IN", "DE", "SG", "Global"],
        min_age=18, requirements=["Webcam & Microphone", "Google account", "Screener qualification"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://userresearch.google.com", date_posted="2026-10-17"
    ),
    Task(
        id="task-google-uxr-02",
        title="Google Maps & Local Search Usability Evaluation",
        description="Test upcoming Google Maps features including AI-powered local discovery, business search, and navigation. 45-minute remote unmoderated session.",
        platform="Google UX Research", platform_url="https://userresearch.google.com",
        category="usability_testing", reward_amount=50.00, currency="USD",
        estimated_minutes=45, hourly_rate_usd=66.67, trust_score=99, verified=True,
        payment_methods=["Amazon Gift Card", "Visa Gift Card"],
        eligible_countries=["US", "UK", "CA", "AU", "IN", "Global"],
        min_age=18, requirements=["Android or iOS smartphone", "Uses Google Maps regularly"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://userresearch.google.com", date_posted="2026-10-16"
    ),
    Task(
        id="task-microsoft-research-01",
        title="Microsoft Research — AI Copilot Productivity Study",
        description="Help Microsoft Research understand how knowledge workers use AI tools like Copilot in Word, Excel, and Teams. 60-minute moderated video session with a Microsoft researcher.",
        platform="Microsoft Research Panel", platform_url="https://www.microsoft.com/en-us/research/connect",
        category="focus_group", reward_amount=100.00, currency="USD",
        estimated_minutes=60, hourly_rate_usd=100.00, trust_score=99, verified=True,
        payment_methods=["Microsoft Rewards", "Amazon Gift Card"],
        eligible_countries=["US", "UK", "CA", "AU", "IN", "DE", "SG"],
        min_age=18, requirements=["Microsoft 365 user", "Webcam & Microphone", "Proficient English"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://www.microsoft.com/en-us/research/connect", date_posted="2026-10-17"
    ),
    Task(
        id="task-microsoft-bing-01",
        title="Bing Search & Microsoft Edge Browser UX Testing",
        description="Evaluate new Bing AI search features and Edge sidebar tools. Complete a series of search tasks and provide verbal feedback on quality and usefulness.",
        platform="Microsoft Research Panel", platform_url="https://www.microsoft.com/en-us/research/connect",
        category="usability_testing", reward_amount=60.00, currency="USD",
        estimated_minutes=45, hourly_rate_usd=80.00, trust_score=99, verified=True,
        payment_methods=["Amazon Gift Card", "Microsoft Rewards"],
        eligible_countries=["US", "UK", "CA", "AU", "IN", "Global"],
        min_age=18, requirements=["Desktop/Laptop", "Microsoft Edge browser", "Webcam"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://www.microsoft.com/en-us/research/connect", date_posted="2026-10-15"
    ),
    Task(
        id="task-apple-researchkit-01",
        title="Apple Heart & Movement Study — Passive Health Data Contribution",
        description="Contribute anonymized health metrics (heart rate, activity levels) via the Apple Research app for 4 weeks. Passive participation — no tasks required beyond enrollment and surveys.",
        platform="Apple Research App", platform_url="https://www.apple.com/apple-research-app/",
        category="survey", reward_amount=30.00, currency="USD",
        estimated_minutes=20, hourly_rate_usd=90.00, trust_score=98, verified=True,
        payment_methods=["Apple Gift Card"],
        eligible_countries=["US"],
        min_age=18, requirements=["iPhone with Apple Watch", "iOS 15+", "US resident"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://www.apple.com/apple-research-app/", date_posted="2026-10-16"
    ),
    Task(
        id="task-meta-research-01",
        title="Meta (Facebook/Instagram) Product Experience Study",
        description="Participate in a 45-minute 1-on-1 session with Meta's UX Research team. Provide feedback on new features in Facebook, Instagram, or WhatsApp. Conducted over video call.",
        platform="Meta Research", platform_url="https://research.facebook.com/research-programs/",
        category="focus_group", reward_amount=80.00, currency="USD",
        estimated_minutes=45, hourly_rate_usd=106.67, trust_score=97, verified=True,
        payment_methods=["PayPal", "Visa Gift Card"],
        eligible_countries=["US", "UK", "CA", "AU", "IN", "DE", "BR", "Global"],
        min_age=18, requirements=["Active Facebook/Instagram account", "Webcam & Microphone"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://research.facebook.com/research-programs/", date_posted="2026-10-17"
    ),
    Task(
        id="task-amazon-shopper-01",
        title="Amazon Shopper Panel — Monthly Receipt Upload & Surveys",
        description="Upload grocery and retail receipts (from any store) monthly via the Amazon Shopper Panel app and complete short surveys about your purchases. Earn Amazon credit each month.",
        platform="Amazon Shopper Panel", platform_url="https://www.amazonshopper.com",
        category="survey", reward_amount=10.00, currency="USD",
        estimated_minutes=20, hourly_rate_usd=30.00, trust_score=97, verified=True,
        payment_methods=["Amazon Credit", "Cash Deposit to Amazon Balance"],
        eligible_countries=["US"],
        min_age=18, requirements=["US resident", "Amazon account", "Smartphone app"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://www.amazonshopper.com", date_posted="2026-10-16"
    ),
    Task(
        id="task-openai-rlhf-01",
        title="OpenAI ChatGPT Response Quality & Safety Evaluation",
        description="Evaluate and rank ChatGPT outputs for helpfulness, harmlessness, and accuracy. Provide expert feedback used to improve frontier AI models via OpenAI's contractor programs (Scale AI / DataAnnotation).",
        platform="OpenAI (via DataAnnotation.tech)", platform_url="https://www.dataannotation.tech",
        category="ai_annotation", reward_amount=30.00, currency="USD",
        estimated_minutes=90, hourly_rate_usd=20.00, trust_score=96, verified=True,
        payment_methods=["PayPal"],
        eligible_countries=["US", "UK", "CA", "AU", "IN", "DE", "Global"],
        min_age=18, requirements=["Strong written English", "Pass qualification assessment", "Logical reasoning ability"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://www.dataannotation.tech", date_posted="2026-10-17"
    ),
    Task(
        id="task-anthropic-rlhf-01",
        title="Anthropic Claude AI Training — Response Preference Ranking",
        description="Compare pairs of Claude AI responses and rank them for safety, helpfulness, and factual accuracy. Work on Anthropic's Constitutional AI training pipeline through vetted contractor networks.",
        platform="Anthropic (via Outlier AI)", platform_url="https://outlier.ai",
        category="ai_annotation", reward_amount=25.00, currency="USD",
        estimated_minutes=60, hourly_rate_usd=25.00, trust_score=97, verified=True,
        payment_methods=["PayPal"],
        eligible_countries=["US", "UK", "CA", "AU", "IN", "Global"],
        min_age=18, requirements=["Excellent English reading comprehension", "Skills assessment required"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://outlier.ai/contributors", date_posted="2026-10-16"
    ),
    Task(
        id="task-samsung-uxr-01",
        title="Samsung Galaxy AI Features Usability Study",
        description="Test AI-powered features on Samsung Galaxy smartphones — Circle to Search, Live Translate, Generative Edit. 30-minute remote session with Samsung's UX Research team.",
        platform="Samsung UX Research", platform_url="https://research.samsung.com",
        category="usability_testing", reward_amount=45.00, currency="USD",
        estimated_minutes=30, hourly_rate_usd=90.00, trust_score=96, verified=True,
        payment_methods=["Amazon Gift Card", "PayPal"],
        eligible_countries=["US", "UK", "CA", "AU", "IN", "KR", "SG", "Global"],
        min_age=18, requirements=["Samsung Galaxy smartphone (2022 or newer)", "Webcam & Microphone"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://research.samsung.com", date_posted="2026-10-15"
    ),

    # ══ EUROPE / GERMANY ════════════════════════════════════════════════════

    Task(
        id="task-testingtime-de-01",
        title="German Language E-Commerce Checkout UX Test",
        description="Shop on a German e-commerce prototype, attempt checkout, and provide verbal feedback on friction points.",
        platform="TestingTime", platform_url="https://www.testingtime.com",
        category="usability_testing", reward_amount=50.00, currency="EUR",
        estimated_minutes=45, hourly_rate_usd=72.00, trust_score=93, verified=True,
        payment_methods=["Bank Transfer", "PayPal"],
        eligible_countries=["DE", "AT", "CH", "FR", "NL"],
        min_age=18, requirements=["Native German speaker", "Webcam & Microphone"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://www.testingtime.com/en/become-a-test-user/", date_posted="2026-10-16"
    ),
    Task(
        id="task-prolific-de-01",
        title="Cognitive Load & Multitasking Study (German Panel)",
        description="Complete a series of memory and attention tasks while tracking cognitive performance under varying workloads.",
        platform="Prolific", platform_url="https://www.prolific.com",
        category="survey", reward_amount=8.00, currency="GBP",
        estimated_minutes=30, hourly_rate_usd=16.00, trust_score=98, verified=True,
        payment_methods=["PayPal"],
        eligible_countries=["DE", "AT", "CH", "FR", "NL"],
        min_age=18, requirements=["Native German speaker", "Desktop/Laptop"],
        scam_risk_level=RiskLevel.SAFE, scam_warnings=[],
        direct_apply_url="https://app.prolific.com/studies", date_posted="2026-10-15"
    ),
]

# ──────────────────────────────────────────────────────────────────────────────
# VERIFIED PLATFORMS DIRECTORY
# ──────────────────────────────────────────────────────────────────────────────
PLATFORMS_DIRECTORY: List[Platform] = [
    Platform(
        id="plat-prolific",
        name="Prolific",
        website="https://www.prolific.com",
        category="Academic & Scientific Surveys",
        trust_score=98,
        avg_hourly_pay="$10 – $22 / hr",
        min_payout="£6.00",
        payment_methods=["PayPal"],
        reputation="Gold standard for academic survey platforms. Mandatory £6/hr minimum wage policy, strict rejection appeal system, no disqualifications mid-study.",
        pros=["Guaranteed minimum pay rate", "Very low rejection rate", "No mid-study disqualification"],
        cons=["Not available in India", "Studies fill within seconds"],
        is_verified=True
    ),
    Platform(
        id="plat-usertesting",
        name="UserTesting",
        website="https://www.usertesting.com",
        category="Website & App Usability",
        trust_score=96,
        avg_hourly_pay="$20 – $60 / hr",
        min_payout="$10.00 per test",
        payment_methods=["PayPal"],
        reputation="Top global usability testing platform. Pays $10 per 20-min test and $30–$60 for live moderated interviews. Available in India.",
        pros=["High payout per test", "Reliable weekly payouts", "Available in India & globally"],
        cons=["Competitive screener filters", "Requires clear English & microphone"],
        is_verified=True
    ),
    Platform(
        id="plat-dataannotation",
        name="DataAnnotation.tech",
        website="https://www.dataannotation.tech",
        category="AI Training & RLHF",
        trust_score=95,
        avg_hourly_pay="$20 – $40 / hr",
        min_payout="Per completion (no minimum)",
        payment_methods=["PayPal"],
        reputation="Premier RLHF platform for training frontier AI models. Large volume of consistent work. Available to India.",
        pros=["High hourly rates", "Work at your own pace", "Open to Indian workers"],
        cons=["Strict initial qualification", "Limited to select countries"],
        is_verified=True
    ),
    Platform(
        id="plat-mturk",
        name="Amazon Mechanical Turk",
        website="https://www.mturk.com",
        category="Microtasks & Data Entry",
        trust_score=88,
        avg_hourly_pay="$5 – $15 / hr",
        min_payout="$1.00 (Gift Cards for IN)",
        payment_methods=["Amazon Gift Card (India)", "Bank Transfer (US)"],
        reputation="Amazon-backed microtask marketplace. Huge task volume daily. Indian workers are paid via Amazon.in gift cards. Best for stacking many small HITs.",
        pros=["Massive task availability", "Amazon-backed reliability", "Available in India"],
        cons=["India workers get gift cards not cash", "Pay per task is very low individually"],
        is_verified=True
    ),
    Platform(
        id="plat-remotasks",
        name="Remotasks",
        website="https://www.remotasks.com",
        category="AI Annotation & Labelling",
        trust_score=86,
        avg_hourly_pay="$5 – $20 / hr",
        min_payout="$5.00",
        payment_methods=["PayPal", "Payoneer"],
        reputation="Scale AI platform with strong presence in India & Southeast Asia. Free training bootcamp for new task types (LiDAR, image annotation, NLP).",
        pros=["Free skills training", "Available in India & Philippines", "Consistent work volume"],
        cons=["Must complete unpaid bootcamp first", "Some tasks are region-locked"],
        is_verified=True
    ),
    Platform(
        id="plat-outlier",
        name="Outlier AI",
        website="https://outlier.ai",
        category="AI Training & Creative Evaluation",
        trust_score=92,
        avg_hourly_pay="$15 – $40 / hr",
        min_payout="Per completion",
        payment_methods=["PayPal"],
        reputation="High-quality AI evaluation work — creative writing, math, coding tasks. Pays well and is available in India and most countries globally.",
        pros=["High pay for skilled tasks", "Available in India", "Flexible hours"],
        cons=["Requires demonstrated expertise in subject area", "Competitive application"],
        is_verified=True
    ),
    Platform(
        id="plat-neevo",
        name="Neevo (Defined.ai)",
        website="https://neevo.defined.ai",
        category="Speech & Language AI Data",
        trust_score=85,
        avg_hourly_pay="$8 – $15 / hr",
        min_payout="$5.00",
        payment_methods=["PayPal", "Bank Transfer"],
        reputation="Specializes in voice/speech and NLP data collection. Excellent for Indian language speakers (Hindi, Tamil, Bengali, Telugu). Pays per recorded sentence.",
        pros=["Perfect for Indian regional language speakers", "Available in India", "No experience needed"],
        cons=["Task availability is sporadic", "Specialized in voice/text tasks only"],
        is_verified=True
    ),
    Platform(
        id="plat-yougov-in",
        name="YouGov India",
        website="https://india.yougov.com",
        category="Consumer Opinion Surveys",
        trust_score=92,
        avg_hourly_pay="₹150 – ₹400 / hr",
        min_payout="₹1,000 (Amazon / Flipkart voucher)",
        payment_methods=["Amazon Voucher", "Flipkart Voucher", "PayPal"],
        reputation="Leading global research firm with a dedicated India panel. Surveys on politics, brands, and consumer goods. Points redeemable for popular Indian vouchers.",
        pros=["Trusted global research firm", "India-specific surveys", "Paytm & Flipkart redemption"],
        cons=["Low points per survey", "High minimum for cash-out"],
        is_verified=True
    ),
    Platform(
        id="plat-toluna-in",
        name="Toluna India",
        website="https://in.toluna.com",
        category="Consumer Surveys",
        trust_score=83,
        avg_hourly_pay="₹200 – ₹500 / hr",
        min_payout="₹800",
        payment_methods=["Amazon Voucher", "Paytm"],
        reputation="Large global panel with India-specific community. Surveys on FMCGs, food, finance, and tech. Points redeemable for Paytm cash.",
        pros=["Paytm cash redemption", "India-localized surveys", "Regular survey frequency"],
        cons=["Disqualification rate can be high", "Points expire if inactive"],
        is_verified=True
    ),
    Platform(
        id="plat-clickworker",
        name="Clickworker",
        website="https://www.clickworker.com",
        category="Microtasks & Data Entry",
        trust_score=90,
        avg_hourly_pay="$8 – $16 / hr",
        min_payout="$5.00",
        payment_methods=["PayPal", "Payoneer", "SEPA"],
        reputation="Established German microtask platform operating globally including India. Best known for UHRS search quality tasks. Reliable payments.",
        pros=["Available in India & 100+ countries", "Diverse task types", "Reliable payment schedule"],
        cons=["UHRS requires periodic qualifications", "Processing time 3–7 days"],
        is_verified=True
    ),
    Platform(
        id="plat-respondent",
        name="Respondent.io",
        website="https://www.respondent.io",
        category="Professional Research Interviews",
        trust_score=94,
        avg_hourly_pay="$50 – $150 / hr",
        min_payout="Per study (direct payout)",
        payment_methods=["PayPal"],
        reputation="High-paying B2B research interviews. Developers, managers, and professionals in India can qualify for tech and startup studies.",
        pros=["Very high payouts per session", "India participants accepted for tech studies", "Legitimate Fortune 500 researchers"],
        cons=["Requires specific professional profile", "5% platform fee on earnings"],
        is_verified=True
    ),
    Platform(
        id="plat-microworkers",
        name="Microworkers",
        website="https://www.microworkers.com",
        category="Microtasks",
        trust_score=78,
        avg_hourly_pay="$3 – $10 / hr",
        min_payout="$9.00",
        payment_methods=["PayPal", "Payoneer", "Skrill"],
        reputation="Global microtask marketplace with strong India user base. Tasks include app testing, SEO verification, social actions, and local research.",
        pros=["Available in India", "Wide task variety", "PayPal & Payoneer payouts"],
        cons=["Low per-task pay", "Need to stack many tasks", "Quality tasks can be scarce"],
        is_verified=True
    ),

    # ══ BIG TECH / GENUINE LARGE COMPANIES ══════════════════════════════════

    Platform(
        id="plat-google-uxr",
        name="Google UX Research",
        website="https://userresearch.google.com",
        category="Big Tech UX Research",
        trust_score=99,
        avg_hourly_pay="$50 – $100 / hr",
        min_payout="$50 per session (Gift Card)",
        payment_methods=["Amazon Gift Card", "Visa Gift Card"],
        reputation="Google's official UX Research recruitment portal. Studies cover Search, Maps, Chrome, Android, Workspace, and AI/Gemini products. Sessions are 1-on-1 with professional Google researchers and pay generously in gift cards.",
        pros=["Direct from Google — zero scam risk", "High pay per session", "Available globally including India", "No special equipment beyond webcam"],
        cons=["Invitation-based; competitive screeners", "Infrequent availability per user"],
        is_verified=True
    ),
    Platform(
        id="plat-microsoft-research",
        name="Microsoft Research Panel",
        website="https://www.microsoft.com/en-us/research/connect",
        category="Big Tech UX Research",
        trust_score=99,
        avg_hourly_pay="$60 – $100 / hr",
        min_payout="$60 per session",
        payment_methods=["Amazon Gift Card", "Microsoft Rewards"],
        reputation="Microsoft's official research participant recruitment program. Studies cover Windows, Office, Teams, Azure, Bing, and AI Copilot products. Legitimate Fortune 500 research with professional compensation.",
        pros=["Direct from Microsoft", "High payouts for professional studies", "Available in India & globally", "Covers wide range of Microsoft products"],
        cons=["Requires relevant Microsoft product usage", "Screener qualification required"],
        is_verified=True
    ),
    Platform(
        id="plat-apple-research",
        name="Apple Research App",
        website="https://www.apple.com/apple-research-app/",
        category="Big Tech Health & UX Research",
        trust_score=98,
        avg_hourly_pay="$15 – $40 / hr",
        min_payout="$20 per study",
        payment_methods=["Apple Gift Card"],
        reputation="Apple's official research app for iPhone and Apple Watch users. Conducts long-term longitudinal health studies (Heart & Movement, Women's Health) in partnership with leading universities. Data is privacy-first and encrypted end-to-end.",
        pros=["Official Apple research", "Passive participation (no active tasks)", "Privacy-first data collection", "Partners with Harvard, NIH"],
        cons=["US-only currently", "Requires Apple Watch for some studies", "Passive earnings — not high active income"],
        is_verified=True
    ),
    Platform(
        id="plat-meta-research",
        name="Meta Research",
        website="https://research.facebook.com/research-programs/",
        category="Big Tech UX Research",
        trust_score=97,
        avg_hourly_pay="$60 – $120 / hr",
        min_payout="$80 per session",
        payment_methods=["PayPal", "Visa Gift Card"],
        reputation="Meta's (Facebook) official UX Research recruitment program. Studies cover Facebook, Instagram, WhatsApp, Messenger, and VR/AR (Meta Quest) products. Sessions run globally with professional Meta researchers.",
        pros=["Direct from Meta", "High payout per session", "Available globally including India & Brazil", "Covers multiple product lines"],
        cons=["Requires active use of Meta apps", "Screener filters can be strict", "VR studies require Quest hardware"],
        is_verified=True
    ),
    Platform(
        id="plat-amazon-shopper",
        name="Amazon Shopper Panel",
        website="https://www.amazonshopper.com",
        category="Consumer Research Panel",
        trust_score=97,
        avg_hourly_pay="$10 – $30 / month passive",
        min_payout="$5 (Amazon Credit)",
        payment_methods=["Amazon Credit", "Cash Deposit to Amazon Balance"],
        reputation="Amazon's official opt-in research panel. Members share purchase receipts and complete monthly surveys to earn Amazon credits. Backed directly by Amazon with robust privacy controls. US-only.",
        pros=["Direct from Amazon", "Passive earnings for ongoing participation", "Instant Amazon credit redemption", "No complex tasks required"],
        cons=["US-only", "Modest monthly earnings ($10–$20)", "Requires sharing purchase data"],
        is_verified=True
    ),
    Platform(
        id="plat-samsung-research",
        name="Samsung UX Research",
        website="https://research.samsung.com",
        category="Big Tech UX Research",
        trust_score=96,
        avg_hourly_pay="$60 – $100 / hr",
        min_payout="$45 per session",
        payment_methods=["Amazon Gift Card", "PayPal"],
        reputation="Samsung's global UX Research program for Galaxy smartphone and SmartTV users. Sessions focus on AI features, One UI design, Bixby, and new hardware experiences. Available in multiple countries including India.",
        pros=["Direct from Samsung", "High payout per session", "Available in India, Korea, and globally", "Tests cutting-edge Galaxy features"],
        cons=["Requires Samsung device", "Session availability varies by region"],
        is_verified=True
    ),
]


class AggregatorService:
    @classmethod
    async def get_tasks(
        cls,
        search: Optional[str] = None,
        category: Optional[str] = None,
        min_hourly: Optional[float] = None,
        country: Optional[str] = None,
        verified_only: bool = True
    ) -> List[Task]:
        results = list(CURATED_TASKS)

        if search:
            q = search.lower()
            results = [
                t for t in results
                if q in t.title.lower() or q in t.description.lower() or q in t.platform.lower()
            ]

        if category and category != "all":
            results = [t for t in results if t.category.lower() == category.lower()]

        if min_hourly and min_hourly > 0:
            results = [t for t in results if t.hourly_rate_usd >= min_hourly]

        if country and country not in ("Global", "all"):
            c = country.upper()
            results = [
                t for t in results
                if "GLOBAL" in [x.upper() for x in t.eligible_countries]
                or c in [x.upper() for x in t.eligible_countries]
            ]

        if verified_only:
            results = [t for t in results if t.verified]

        results.sort(key=lambda x: x.hourly_rate_usd, reverse=True)
        return results

    @classmethod
    def get_platforms(cls, country: Optional[str] = None) -> List[Platform]:
        return PLATFORMS_DIRECTORY

    @classmethod
    async def inspect_url(cls, url: str):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        extracted_text = ""
        page_title = ""
        try:
            async with httpx.AsyncClient(timeout=8.0, follow_redirects=True) as client:
                resp = await client.get(url, headers=headers)
                if resp.status_code == 200:
                    soup = BeautifulSoup(resp.text, "html.parser")
                    page_title = soup.title.string.strip() if soup.title else ""
                    text_parts = [p.get_text() for p in soup.find_all(["h1","h2","h3","p","li"])]
                    extracted_text = " ".join(text_parts)[:4000]
        except Exception as e:
            extracted_text = f"Could not fetch URL ({str(e)}). Analyzing domain structure only."

        return TrustEngine.analyze_content(text=f"{page_title} {extracted_text}", url=url)
