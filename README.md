# 🛡️ AI-Powered Hybrid Security Dashboard (AIP-HSD)

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/yourusername/aiphsd)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Stack](https://img.shields.io/badge/Stack-Polyglot-blue.svg)](#-the-polyglot-sentinel)
[![Architecture](https://img.shields.io/badge/Architecture-Hybrid--Intelligence-orange.svg)](#-architecture)

**AIP-HSD** is an enterprise-grade, self-learning security intelligence platform. It merges internal network telemetry with global OSINT (Open Source Intelligence) to provide real-time dashboards, automated threat correlation, and SOC-level predictive analytics.

---

## 🖥️ Modern Dashboard Interface

### 🌐 Global Threat Architecture
The "Digital Sentinel" HUD provides a high-precision, interactive view of global threat hotspots, synchronized with internal network health.

![Main Dashboard](https://lh3.googleusercontent.com/aida/ADBb0uiEcp0V-9oDjzOxFO6vuLgPN8sb2bivNeWL5lIfJtxBmA3L0n63jvkfxBbLm5YIp9SudY-HTEI6ysy-XRohlwiQ3dXdMyFsuah4DrsmhSDV5GY93tEnnkHMwfyvTLjmfX3zZ_vmrqL85M91lSTzr5XA2sE1tfgsAX2viSOUMe7uaD_aBokj7PXgWBAKOEIfrwTVS2sq6gf1MamcSSmnBiu7-fQkMsZ1i-Bo7CvM5rHrqkVUfhc66ffwZpo)

### 🤖 AI Core Insights & Queries
Analysts can query the intelligence system in plain English to receive deep-dive analysis, confidence-scored threat matrixes, and prioritized action items.

![AI Query Results](https://lh3.googleusercontent.com/aida/ADBb0uhUfLKdpnEQdoJBYKnENYAmPvUL2Gn2DU559ZA8e_JQvwuLtDqmaMkuIj-VzcOfXdF54YciX89AYoVkOIbtGvD_GE7r1H_HKdSHYTNZMTo_Gkxr7QaKXphI2r1xG4gL15z6-dzwCtPgKa3FxmuJIZ53T3naYD4RjaVF41W4PipXyTMTzDc7Lz4GZcieFRexhTBinTHJeyAPkXY9B_b1E62DUDdAj2dfcrxAoRLN-FnM7YYgDMXRY3hGKk4)

---

## 🛠️ Key Features & Functions

- **AI Autonomous Threat Hunter**: Correlation of global OSINT data with internal port and keyword anomalies using high-precision IOC matching.
- **Real-time Attack Map**: D3.js powered world map and force-directed internal network topology.
- **AI Malware Sandbox**: Statically analyze and execute suspicious samples with AI-generated risk scoring and capability reporting.
- **Polyglot Agent Architecture**: Multi-language monitoring agents (Go, C++, Python) for ultra-low latency telemetry.
- **Unified Risk Scoring**: High-performance Rust-based engine for intensive composite risk calculations.
- **Automated OSINT Pipelines**: Hourly collection from RSS, web scrapers, and dynamic hidden browser portals.

---

## 🧩 The Polyglot Sentinel
AIP-HSD leverages the best programming language for each critical security task:

| Language | Component | Role |
| :--- | :--- | :--- |
| **Python** | Backend & AI | FastAPI Orchestration, LLM Integration, OSINT Collection |
| **TypeScript** | Frontend | Enterprise-grade React HUD with Type Safety |
| **Rust** | Performance Core | Intensive Risk Scoring Engine & Static Malware Analysis |
| **Go** | Native Agent | Lightweight, statically-linked Endpoint Collector |
| **C++** | Low-level Monitoring | High-speed Network Packet Sniffer |
| **Java** | Integration Bridge | Legacy Mainframe & Corporate Log Ingestion |
| **Ruby** | Maintenance | Platform Health, Periodic Cleanup & Log Archiving |
| **PHP** | Legacy Web | Compatibility with older SOC Reporting Portals |
| **Swift/Kotlin** | Mobile Alerts | Native iOS/Android critical threat notifications |

---

## 🚀 Architecture
The platform is designed for massive scalability and real-time responsiveness.

1. **Collectors**: Multi-language agents push telemetry to the Backend API via JSON/REST.
2. **Aggregators**: Python-based scrapers pull global intelligence from the web.
3. **Analyzer**: The AI module correlates data and delegates heavy math to the **Rust Performance Core**.
4. **Dashboard**: The React/TypeScript HUD visualizes findings in real-time via WebSocket/Polling.

---

## 🚦 Getting Started

### 🐳 Docker Deployment
```bash
docker-compose -f docker/docker-compose.yml up --build
```

### 🏗️ Local Development
- **Backend**: `cd backend && pip install -r requirements.txt && uvicorn main:app --reload`
- **Frontend**: `cd frontend && npm install && npm start`
- **Rust Core**: `cd rust_module && cargo build --release`
- **Go Agent**: `cd agents/go && go build -o collector`

---
*Created by Jules, Powered by Hybrid Intelligence.*
