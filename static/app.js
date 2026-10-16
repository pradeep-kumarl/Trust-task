// TrustTask Frontend Application Logic
let allTasks = [];
let allPlatforms = [];

document.addEventListener("DOMContentLoaded", () => {
    lucide.createIcons();
    initApp();
});

async function initApp() {
    setupEventListeners();
    await Promise.all([loadStats(), loadTasks(), loadPlatforms()]);
}

function setupEventListeners() {
    const searchInput = document.getElementById("searchInput");
    const categorySelect = document.getElementById("categorySelect");
    const countrySelect = document.getElementById("countrySelect");
    const minHourlySelect = document.getElementById("minHourlySelect");

    searchInput.addEventListener("input", debounce(filterTasks, 250));
    categorySelect.addEventListener("change", filterTasks);
    countrySelect.addEventListener("change", filterTasks);
    minHourlySelect.addEventListener("change", filterTasks);
}

function debounce(func, wait) {
    let timeout;
    return (...args) => {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), wait);
    };
}

// ---------------- TAB NAVIGATION ----------------
function switchTab(tabId) {
    document.querySelectorAll(".tab-btn").forEach(btn => {
        btn.classList.remove("bg-emerald-600", "text-white");
        btn.classList.add("text-slate-400");
    });

    const activeBtn = document.getElementById(`tab-${tabId}`);
    if (activeBtn) {
        activeBtn.classList.remove("text-slate-400");
        activeBtn.classList.add("bg-emerald-600", "text-white");
    }

    document.getElementById("view-tasks").classList.add("hidden");
    document.getElementById("view-analyzer").classList.add("hidden");
    document.getElementById("view-platforms").classList.add("hidden");

    document.getElementById(`view-${tabId}`).classList.remove("hidden");
    lucide.createIcons();
}

// ---------------- LOAD & RENDER TASKS ----------------
async function loadTasks() {
    try {
        const res = await fetch("/api/tasks");
        allTasks = await res.json();
        renderTasks(allTasks);
    } catch (err) {
        console.error("Failed to load tasks:", err);
    }
}

async function loadStats() {
    try {
        const res = await fetch("/api/stats");
        const data = await res.json();
        document.getElementById("stat-tasks").innerText = data.active_genuine_tasks;
        document.getElementById("stat-rate").innerText = `$${data.avg_hourly_compensation_usd.toFixed(2)}/hr`;
        document.getElementById("stat-platforms").innerText = data.verified_platforms;
    } catch (err) {
        console.error("Failed to load stats:", err);
    }
}

function filterTasks() {
    const query = document.getElementById("searchInput").value.toLowerCase().trim();
    const category = document.getElementById("categorySelect").value;
    const country = document.getElementById("countrySelect").value;
    const minHourly = parseFloat(document.getElementById("minHourlySelect").value) || 0;

    const filtered = allTasks.filter(task => {
        const matchesQuery = !query || 
            task.title.toLowerCase().includes(query) || 
            task.platform.toLowerCase().includes(query) ||
            task.description.toLowerCase().includes(query);

        const matchesCategory = category === "all" || task.category.toLowerCase() === category.toLowerCase();
        const matchesHourly = task.hourly_rate_usd >= minHourly;
        const matchesCountry = country === "Global" || 
            task.eligible_countries.includes("Global") || 
            task.eligible_countries.includes(country);

        return matchesQuery && matchesCategory && matchesHourly && matchesCountry;
    });

    renderTasks(filtered);
}

function renderTasks(tasks) {
    const grid = document.getElementById("tasksGrid");
    const noTasksMsg = document.getElementById("noTasksMsg");
    grid.innerHTML = "";

    if (!tasks || tasks.length === 0) {
        noTasksMsg.classList.remove("hidden");
        return;
    }
    noTasksMsg.classList.add("hidden");

    tasks.forEach(task => {
        const card = document.createElement("div");
        card.className = "bg-slate-800/80 border border-slate-700/80 hover:border-emerald-500/60 rounded-2xl p-5 flex flex-col justify-between transition-all duration-200 hover:-translate-y-1 hover:shadow-xl hover:shadow-emerald-950/20";

        card.innerHTML = `
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold px-2.5 py-1 rounded-full bg-slate-900 border border-slate-700 text-slate-300">
                        ${task.platform}
                    </span>
                    <div class="flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-emerald-950/70 border border-emerald-800 text-emerald-400 text-xs font-semibold">
                        <i data-lucide="shield-check" class="w-3.5 h-3.5"></i>
                        <span>${task.trust_score}% Genuine</span>
                    </div>
                </div>

                <h3 class="font-bold text-base text-slate-100 line-clamp-2">${escapeHtml(task.title)}</h3>
                <p class="text-xs text-slate-400 line-clamp-2 leading-relaxed">${escapeHtml(task.description)}</p>

                <!-- Payout Box -->
                <div class="bg-slate-900/90 rounded-xl p-3 border border-slate-700/60 flex items-center justify-between">
                    <div>
                        <div class="text-xs text-slate-400">Task Reward</div>
                        <div class="text-lg font-bold text-emerald-400">
                            ${task.currency === "GBP" ? "£" : "$"}${task.reward_amount.toFixed(2)}
                            <span class="text-xs font-normal text-slate-400">/ ~${task.estimated_minutes}m</span>
                        </div>
                    </div>
                    <div class="text-right">
                        <div class="text-xs text-slate-400">Est. Hourly Pay</div>
                        <div class="text-base font-extrabold text-teal-300">
                            $${task.hourly_rate_usd.toFixed(2)}<span class="text-xs font-normal text-slate-400">/hr</span>
                        </div>
                    </div>
                </div>

                <!-- Tags -->
                <div class="flex flex-wrap gap-1.5 pt-1">
                    <span class="text-[10px] bg-slate-900 px-2 py-0.5 rounded text-slate-400 border border-slate-800">
                        ${task.category.replace('_', ' ').toUpperCase()}
                    </span>
                    <span class="text-[10px] bg-slate-900 px-2 py-0.5 rounded text-slate-400 border border-slate-800">
                        ${task.eligible_countries.slice(0, 3).join(", ")}
                    </span>
                    <span class="text-[10px] bg-slate-900 px-2 py-0.5 rounded text-emerald-400/90 border border-emerald-900/50">
                        ${task.payment_methods.join(", ")}
                    </span>
                </div>
            </div>

            <div class="mt-5 pt-4 border-t border-slate-700/60 flex items-center gap-2">
                <button onclick="openModal('${task.id}')" class="flex-1 py-2 rounded-xl text-xs font-semibold bg-slate-700 hover:bg-slate-600 text-slate-200 transition">
                    Safety & Details
                </button>
                <a href="${task.direct_apply_url}" target="_blank" rel="noopener noreferrer" class="flex-1 py-2 rounded-xl text-xs font-semibold bg-emerald-600 hover:bg-emerald-500 text-white text-center transition flex items-center justify-center gap-1">
                    Open Task <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
                </a>
            </div>
        `;

        grid.appendChild(card);
    });

    lucide.createIcons();
}

// ---------------- LOAD & RENDER PLATFORMS ----------------
async function loadPlatforms() {
    try {
        const res = await fetch("/api/platforms");
        allPlatforms = await res.json();
        renderPlatforms(allPlatforms);
    } catch (err) {
        console.error("Failed to load platforms:", err);
    }
}

function renderPlatforms(platforms) {
    const grid = document.getElementById("platformsGrid");
    grid.innerHTML = "";

    platforms.forEach(plat => {
        const card = document.createElement("div");
        card.className = "bg-slate-800/80 border border-slate-700 rounded-2xl p-6 flex flex-col justify-between shadow-xl";

        card.innerHTML = `
            <div class="space-y-4">
                <div class="flex items-center justify-between">
                    <div>
                        <h3 class="text-xl font-bold text-white">${escapeHtml(plat.name)}</h3>
                        <span class="text-xs text-emerald-400">${escapeHtml(plat.category)}</span>
                    </div>
                    <div class="px-3 py-1 rounded-full bg-emerald-950 border border-emerald-800 text-emerald-400 text-xs font-bold">
                        ${plat.trust_score}% Trust
                    </div>
                </div>

                <p class="text-xs text-slate-300 leading-relaxed">${escapeHtml(plat.reputation)}</p>

                <div class="grid grid-cols-2 gap-2 text-xs bg-slate-900/80 p-3 rounded-xl border border-slate-700/60">
                    <div>
                        <div class="text-slate-400">Avg Earnings:</div>
                        <div class="font-semibold text-teal-400">${plat.avg_hourly_pay}</div>
                    </div>
                    <div>
                        <div class="text-slate-400">Min Payout:</div>
                        <div class="font-semibold text-slate-200">${plat.min_payout}</div>
                    </div>
                </div>

                <div class="space-y-2 text-xs">
                    <div class="text-emerald-400 font-semibold flex items-center gap-1">
                        <i data-lucide="check-circle" class="w-3.5 h-3.5"></i> Pros:
                    </div>
                    <ul class="list-disc list-inside text-slate-400 space-y-0.5">
                        ${plat.pros.map(p => `<li>${escapeHtml(p)}</li>`).join("")}
                    </ul>
                </div>
            </div>

            <div class="mt-6 pt-4 border-t border-slate-700">
                <a href="${plat.website}" target="_blank" rel="noopener noreferrer" class="w-full py-2.5 rounded-xl text-xs font-semibold bg-emerald-600 hover:bg-emerald-500 text-white text-center transition flex items-center justify-center gap-1.5">
                    Visit Official Portal <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
                </a>
            </div>
        `;
        grid.appendChild(card);
    });

    lucide.createIcons();
}

// ---------------- SCAM DETECTOR TOOL ----------------
async function runScamAnalysis() {
    const url = document.getElementById("analyzerUrl").value.trim();
    const text = document.getElementById("analyzerText").value.trim();
    const btn = document.getElementById("btnAnalyze");
    const resultBox = document.getElementById("analyzerResult");

    if (!url && !text) {
        alert("Please enter a website link or paste text from the offer to analyze.");
        return;
    }

    btn.disabled = true;
    btn.innerHTML = `<i data-lucide="loader-2" class="w-5 h-5 animate-spin"></i> Running Deep Scan...`;
    lucide.createIcons();

    try {
        const res = await fetch("/api/check-url", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url: url || null, text_content: text || null })
        });
        const data = await res.json();
        displayAnalysisResult(data);
    } catch (err) {
        alert("Error analyzing content: " + err.message);
    } finally {
        btn.disabled = false;
        btn.innerHTML = `<i data-lucide="radar" class="w-5 h-5"></i> Analyze Legitimacy & Safety`;
        lucide.createIcons();
    }
}

function displayAnalysisResult(data) {
    const box = document.getElementById("analyzerResult");
    box.classList.remove("hidden");

    let borderColor = "border-emerald-600 bg-emerald-950/20";
    let badgeColor = "bg-emerald-900/60 text-emerald-400 border-emerald-700";
    let icon = "shield-check";

    if (data.risk_level === "caution") {
        borderColor = "border-amber-600 bg-amber-950/20";
        badgeColor = "bg-amber-900/60 text-amber-400 border-amber-700";
        icon = "alert-triangle";
    } else if (data.risk_level === "danger") {
        borderColor = "border-rose-600 bg-rose-950/20";
        badgeColor = "bg-rose-900/60 text-rose-400 border-rose-700";
        icon = "shield-x";
    }

    box.className = `mt-8 p-6 rounded-2xl border ${borderColor} space-y-4 animate-fade-in`;

    box.innerHTML = `
        <div class="flex items-center justify-between">
            <div class="flex items-center gap-3">
                <div class="p-2.5 rounded-xl border ${badgeColor}">
                    <i data-lucide="${icon}" class="w-6 h-6"></i>
                </div>
                <div>
                    <h4 class="text-lg font-bold text-white">${data.verdict}</h4>
                    <p class="text-xs text-slate-400">Domain: ${data.analysis_details.domain || "Text Evaluation"}</p>
                </div>
            </div>
            <div class="text-right">
                <div class="text-3xl font-extrabold ${data.score >= 80 ? 'text-emerald-400' : (data.score >= 50 ? 'text-amber-400' : 'text-rose-400')}">
                    ${data.score}/100
                </div>
                <div class="text-[10px] uppercase font-bold text-slate-400 tracking-wider">Safety Score</div>
            </div>
        </div>

        <div class="p-3 bg-slate-900/80 rounded-xl border border-slate-700/60 text-xs text-slate-300">
            <strong>Advisory:</strong> ${escapeHtml(data.recommendation)}
        </div>

        ${data.detected_red_flags.length > 0 ? `
            <div class="space-y-1">
                <div class="text-xs font-bold text-rose-400 flex items-center gap-1.5">
                    <i data-lucide="x-circle" class="w-4 h-4"></i> Red Flags Detected:
                </div>
                <ul class="list-disc list-inside text-xs text-slate-300 space-y-1 pl-1">
                    ${data.detected_red_flags.map(f => `<li class="text-rose-300">${escapeHtml(f)}</li>`).join("")}
                </ul>
            </div>
        ` : ''}

        ${data.trust_signals.length > 0 ? `
            <div class="space-y-1">
                <div class="text-xs font-bold text-emerald-400 flex items-center gap-1.5">
                    <i data-lucide="check-circle" class="w-4 h-4"></i> Trust Signals Verified:
                </div>
                <ul class="list-disc list-inside text-xs text-slate-300 space-y-1 pl-1">
                    ${data.trust_signals.map(s => `<li class="text-emerald-300">${escapeHtml(s)}</li>`).join("")}
                </ul>
            </div>
        ` : ''}
    `;

    lucide.createIcons();
}

// ---------------- MODAL LOGIC ----------------
function openModal(taskId) {
    const task = allTasks.find(t => t.id === taskId);
    if (!task) return;

    const modal = document.getElementById("taskModal");
    const content = document.getElementById("modalContent");

    content.innerHTML = `
        <div class="space-y-4">
            <div class="flex items-center gap-2">
                <span class="text-xs font-semibold px-2.5 py-1 rounded-full bg-slate-800 border border-slate-700 text-slate-300">
                    ${task.platform}
                </span>
                <span class="text-xs font-semibold px-2.5 py-1 rounded-full bg-emerald-950 border border-emerald-800 text-emerald-400">
                    Verified Genuine (${task.trust_score}%)
                </span>
            </div>

            <h2 class="text-xl font-bold text-white">${escapeHtml(task.title)}</h2>
            <p class="text-sm text-slate-300 leading-relaxed">${escapeHtml(task.description)}</p>

            <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 bg-slate-800/60 p-4 rounded-xl border border-slate-700 text-xs">
                <div>
                    <span class="text-slate-400 block">Reward Amount:</span>
                    <span class="text-emerald-400 font-bold text-sm">${task.currency === "GBP" ? "£" : "$"}${task.reward_amount.toFixed(2)}</span>
                </div>
                <div>
                    <span class="text-slate-400 block">Time to Complete:</span>
                    <span class="text-slate-200 font-bold text-sm">~${task.estimated_minutes} minutes</span>
                </div>
                <div>
                    <span class="text-slate-400 block">Calculated Hourly:</span>
                    <span class="text-teal-400 font-bold text-sm">$${task.hourly_rate_usd.toFixed(2)}/hr</span>
                </div>
            </div>

            <div class="space-y-2 text-xs">
                <h4 class="font-bold text-slate-200">Requirements & Equipment:</h4>
                <ul class="list-disc list-inside text-slate-400 space-y-1">
                    ${task.requirements.map(r => `<li>${escapeHtml(r)}</li>`).join("")}
                    <li>Minimum Age: ${task.min_age}+</li>
                </ul>
            </div>

            <div class="space-y-2 text-xs">
                <h4 class="font-bold text-slate-200">Payment & Country Eligibility:</h4>
                <p class="text-slate-400">Methods: <span class="text-emerald-400">${task.payment_methods.join(", ")}</span></p>
                <p class="text-slate-400">Eligible Regions: ${task.eligible_countries.join(", ")}</p>
            </div>

            <div class="pt-4 border-t border-slate-700 flex gap-3">
                <button onclick="closeModal()" class="w-1/3 py-2.5 rounded-xl text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-300">
                    Close
                </button>
                <a href="${task.direct_apply_url}" target="_blank" rel="noopener noreferrer" class="w-2/3 py-2.5 rounded-xl text-xs font-semibold bg-emerald-600 hover:bg-emerald-500 text-white text-center flex items-center justify-center gap-1.5">
                    Start Task on ${task.platform} <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
                </a>
            </div>
        </div>
    `;

    modal.classList.remove("hidden");
    lucide.createIcons();
}

function closeModal() {
    document.getElementById("taskModal").classList.add("hidden");
}

function escapeHtml(str) {
    if (!str) return "";
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}
