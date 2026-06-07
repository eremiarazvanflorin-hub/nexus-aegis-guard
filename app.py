from flask import Flask, render_template_string, jsonify
import random

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NEXUS - AEGIS GUARD COMMAND</title>
    <style>
        body { background: #060a12; color: #00f2fe; font-family: 'Segoe UI', monospace; text-align: center; padding: 20px; margin: 0; }
        .dashboard { border: 2px solid #00f2fe; border-radius: 12px; padding: 25px; display: inline-block; background: #0d1527; box-shadow: 0 0 25px rgba(0,242,254,0.3); width: 90%; max-width: 800px; margin-top: 10px; }
        h1 { color: #fff; text-shadow: 0 0 10px #00f2fe; font-size: 1.5em; letter-spacing: 3px; margin-bottom: 5px; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 20px 0; text-align: left; }
        .card { background: #13223f; padding: 12px; border-radius: 6px; border-left: 5px solid #38bdf8; font-size: 0.9em; }
        .terminal { background: #020617; color: #34d399; padding: 15px; border-radius: 8px; text-align: left; font-family: monospace; font-size: 0.85em; height: 140px; overflow-y: auto; border: 1px solid #1e293b; margin-top: 15px; }
        .status { color: #34d399; font-weight: bold; animation: pulse 2s infinite; }
        @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.5; } }
        @media (max-width: 600px) { .grid { grid-template-columns: 1fr; } }
    </style>
</head>
<body>
    <div class="dashboard">
        <h1>🛡️ NEXUS AEGIS-GUARD SYSTEM</h1>
        <p>ESCORT AGENT: <span class="status">ONLINE (GEMINI BRAIN active)</span></p>
        <hr color="#00f2fe">

        <div class="grid">
            <div class="card">✈️ AIR CORRIDOR: <span id="coridor">SECURE</span></div>
            <div class="card">🚀 SFINX-01 SPEED: Mach <span id="viteza">5.10</span></div>
            <div class="card">🛰️ RADAR SCANNING: <span id="radar">0 targets</span></div>
            <div class="card">🔋 CORE STATUS: <span id="core">1.21</span> GW</div>
        </div>

        <div class="terminal" id="log-box">
            [System] Google Cloud Agent Builder initialized successfully.<br>
            [System] Model Context Protocol (MCP) connected to MongoDB Atlas.
        </div>
        
        <p style="margin-top: 20px; font-size: 0.75em; color: #475569;">Tactical Escort Mission Tracker | Encrypted Node: RazvanFlorin</p>
    </div>

    <script>
        setInterval(async () => {
            try {
                const res = await fetch('/api/secure-corridor');
                const data = await res.json();
                
                document.getElementById('viteza').innerText = data.speed;
                document.getElementById('core').innerText = data.core;
                document.getElementById('radar').innerText = data.radar;
                document.getElementById('coridor').innerText = data.coridor;
                
                const logBox = document.getElementById('log-box');
                logBox.innerHTML += `<br>${data.log}`;
                logBox.scrollTop = logBox.scrollHeight;
            } catch(e) { console.log(e); }
        }, 2500);
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/secure-corridor')
def secure_corridor():
    speed = round(random.uniform(5.08, 5.12), 2)
    core = round(random.uniform(1.208, 1.212), 3)
    targets = random.choice(["0 detected", "1 commercial (cleared)", "0 detected"])
    coridor_status = "ACTIVE ESCORT"
    
    logs = [
        "[Gemini Brain] Analyzing flight telemetry for team delegation.",
        "[MongoDB MCP] Querying allowed aircraft registry database.",
        "[Sfinx-01 AI] Core temperature stable at 40G containment.",
        "[MongoDB MCP] Logging secure flight corridor path variables.",
        "[Gemini Brain] All clear. Airspace protection optimized."
    ]
    
    return jsonify({
        "speed": speed,
        "core": core,
        "radar": targets,
        "coridor": coridor_status,
        "log": random.choice(logs)
    })
