# NEXUS - AEGIS GUARD COMMAND

An advanced autonomous escort and tactical airspace security agent powered by **Google Cloud Agent Builder (Gemini 1.5 Pro)** and integrated with **MongoDB Atlas** via the Model Context Protocol (MCP).

## 🛡️ Project Overview
NEXUS Aegis-Guard acts as an autonomous mission control center for airspace security. The system monitors live flight data, logs critical telemetry, and uses Gemini's advanced reasoning capabilities to detect potential airspace threats, deploying the Sfinx-01 hyper-speed escort vehicle when necessary.

## ⚡ Real-World Challenge & Solution
- **The Challenge**: Managing rapid responses to unauthorized or unidentified flights in high-security air corridors requires instant data validation and multi-step tactical planning.
- **The Agent Solution**: NEXUS uses Google Cloud Agent Builder as its "brain." When a radar anomaly occurs, the agent reasons through the threat level, queries the aircraft registry, logs the incident permanently into MongoDB Atlas using MCP, and takes corrective action on the dashboard.

## 📊 Realistic Drone Detection & Communication Telemetry
When an intruder enters the airspace, the system autonomously identifies and logs the following tactical variables directly to the cloud cluster:
- **Target ID**: Unique military radar identifier (e.g., TG-4821)
- **Aircraft Classification**: Real-time signature analysis (Supersonic Drone, Stealth Fighter, Uncharted UAV)
- **Threat Level Evaluation**: AI-calculated risk profile (MEDIUM RISK / CRITICAL THREAT)
- **Live GPS Coordinates**: Precise latitude and longitude grids within the Romanian airspace corridor
- **Reactor Core Status**: Power output monitoring of the escort vessel in Gigawatts (GW)
## 📊 Update: Live System Simulation & Telemetry Data (June 2026)
To demonstrate the reasoning power of the Gemini agent and its connectivity with MongoDB Atlas, we extracted a live telemetry dataset saved during a simulated intercept mission:

```json
{
  "incident_id": "NEXUS-2026-06-08",
  "radar_telemetry": {
    "target_id": "TG-4821-X",
    "classification": "Supersonic Drone (Uncharted)",
    "speed": "Mach 3.2",
    "threat_level": "CRITICAL THREAT",
    "coordinates": {
      "lat": "44.4268",
      "long": "26.1025",
      "region": "Romanian Airspace Corridor East"
    }
  },
  "escort_response": {
    "vehicle": "Sfinx-01",
    "status": "DEPLOYED",
    "fusion_core_output": "1.21 GW",
    "containment_field_stability": "99.4%"
  },
  "mcp_log_status": "SUCCESSFULLY_SAVED_TO_MONGODB_ATLAS"
}
```
*Note: This dataset reflects the exact structured telemetry sent by our Flask backend to the cloud cluster when the AI agent identifies an airspace threat.*


## 🛠️ Tech Stack & Architecture
- **Backend & Interface**: Python, Flask, HTML5, CSS3 (Hosted on PythonAnywhere)
- **Database Storage**: MongoDB Atlas Cloud Cluster
- **AI Engine**: Google Cloud Agent Builder (Gemini 1.5 Pro)
- **Protocol**: Model Context Protocol (MCP) for secure database tools execution.

## 📂 Repository Structure
- `flask_app.py` - The core application file managing the live web panel and MongoDB connections.
- `requirements.txt` - Python dependencies for the production environment.
- `LICENSE` - Official MIT Open-Source License.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
