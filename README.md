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
