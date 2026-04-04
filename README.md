# 🛡️ AI-Powered Hybrid Security Dashboard (AIP-HSD)

![Version](https://img.shields.io/badge/version-v1.1.0-blue.svg)
![Status](https://img.shields.io/badge/status-enterprise--ready-brightgreen.svg)
![Build](https://img.shields.io/badge/CI--CD-modular-orange.svg)
![Release](https://img.shields.io/badge/deployment-GHCR--Native-blueviolet.svg)

**AIP-HSD** is an elite, self-evolving security intelligence ecosystem. It integrates real-time OSINT (Open Source Intelligence) with internal deep-telemetry to provide SOC-level insights, autonomous threat hunting, and automated remediation.

---

## 🖥️ Modern HUD Interface

### 🌐 Global Sentinel Map
High-precision, interactive world projection visualizing global threat vectors and regional hotspots.

![Main Dashboard](https://lh3.googleusercontent.com/aida/ADBb0uiEcp0V-9oDjzOxFO6vuLgPN8sb2bivNeWL5lIfJtxBmA3L0n63jvkfxBbLm5YIp9SudY-HTEI6ysy-XRohlwiQ3dXdMyFsuah4DrsmhSDV5GY93tEnnkHMwfyvTLjmfX3zZ_vmrqL85M91lSTzr5XA2sE1tfgsAX2viSOUMe7uaD_aBokj7PXgWBAKOEIfrwTVS2sq6gf1MamcSSmnBiu7-fQkMsZ1i-Bo7CvM5rHrqkVUfhc66ffwZpo)

### 🤖 AI Query & Malware Reports
Advanced natural language interface for deep intelligence extraction and detailed behavioral malware analysis.

![AI Query Results](https://lh3.googleusercontent.com/aida/ADBb0uhUfLKdpnEQdoJBYKnENYAmPvUL2Gn2DU559ZA8e_JQvwuLtDqmaMkuIj-VzcOfXdF54YciX89AYoVkOIbtGvD_GE7r1H_HKdSHYTNZMTo_Gkxr7QaKXphI2r1xG4gL15z6-dzwCtPgKa3FxmuJIZ53T3naYD4RjaVF41W4PipXyTMTzDc7Lz4GZcieFRexhTBinTHJeyAPkXY9B_b1E62DUDdAj2dfcrxAoRLN-FnM7YYgDMXRY3hGKk4)

---

## 🚀 Key Enterprise Features

- **🔄 GitHub Auto-Updater**: Automated platform lifecycle management via integrated GitHub Release API.
- **🏢 Multi-Tenant Core**: Strict data isolation for complex organizational hierarchies.
- **📈 Historical Trends**: D3.js powered visualization of long-term security metrics (30/90/365 days).
- **🧪 Malware Sandbox**: Behavioral analysis engine with MITRE ATT&CK mapping and risk scoring.
- **🛡️ Hardened Defense**: JWT-based authentication, RBAC, and centralized Audit Logging.
- **🧩 Polyglot Architecture**: High-performance core in **Rust**, native agents in **Go**, and AI logic in **Python**.

---

## ⚙️ Modular CI/CD Pipeline
Our GitHub Action workflows are segmented for maximum reliability and control:

| Workflow | Trigger | Description |
| :--- | :--- | :--- |
| **🚀 Windows Release** | Manual / Tag | Builds standalone `.exe` binaries with PyInstaller. |
| **🐧 Linux Release** | Manual / Tag | Generates statically-linked ELF binaries. |
| **🐳 Docker (GHCR)** | Manual / Tag | Pushes multi-arch images to GitHub Container Registry. |
| **🧪 Test Suite** | PR / Main | Executes full backend and intelligence functional tests. |

---

## 🚦 Deployment & Lifecycle

### 🏁 Quick Start
```bash
docker-compose -f docker/docker-compose.yml up --build
```

### 🆙 Auto-Update Logic
The platform includes an internal `GitHubAutoUpdater` module. To manually trigger an update to the latest release:
```bash
curl -X POST http://localhost:8000/api/updater/apply -H "Authorization: Bearer <TOKEN>"
```

---
*Architected by Jules // Powered by Global Security Intelligence.*
