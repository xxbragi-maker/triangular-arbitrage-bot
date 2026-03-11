function formatOpportunity(opportunity) {
    if (!opportunity) return "-";
    return `${opportunity.route} | value: ${opportunity.value}`;
}

async function loadStats() {
    try {
        const response = await fetch("/stats");
        const data = await response.json();

        document.getElementById("status").innerText = data.status ?? "-";
        document.getElementById("profit").innerText = data.profit ?? 0;
        document.getElementById("trades").innerText = data.trades ?? 0;
        document.getElementById("exchange1").innerText = data.exchange_1 ?? "-";
        document.getElementById("exchange2").innerText = data.exchange_2 ?? "-";

        const pricesCountEl = document.getElementById("pricesCount");
        const lastOpportunityEl = document.getElementById("lastOpportunity");

        if (pricesCountEl) {
            pricesCountEl.innerText = data.prices_count ?? 0;
        }

        if (lastOpportunityEl) {
            lastOpportunityEl.innerText = formatOpportunity(data.last_opportunity);
        }
    } catch (error) {
        document.getElementById("status").innerText = "API error";
    }
}

loadStats();
setInterval(loadStats, 3000);