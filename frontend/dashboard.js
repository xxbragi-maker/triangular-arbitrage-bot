async function loadStats() {
    try {
        const response = await fetch("/stats");
        const data = await response.json();

        document.getElementById("status").innerText = data.status ?? "-";
        document.getElementById("profit").innerText = data.profit ?? 0;
        document.getElementById("trades").innerText = data.trades ?? 0;
        document.getElementById("exchange1").innerText = data.exchange_1 ?? "-";
        document.getElementById("exchange2").innerText = data.exchange_2 ?? "-";
    } catch (error) {
        document.getElementById("status").innerText = "API error";
    }
}

loadStats();
setInterval(loadStats, 3000);
