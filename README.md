# AI-Powered Hybrid Security Dashboard (AIP-HSD)

## 🚀 Overview
AIP-HSD is an enterprise-grade, AI-driven hybrid security intelligence platform. It integrates internal system monitoring with global threat intelligence to provide real-time insights, automated threat hunting, and SOC-level analytics.

## 🛠 Features
- **Global Threat Architecture**: Interactive map correlating global OSINT with internal telemetry.
- **Internal Network Monitoring**: Real-time health and risk status of servers, endpoints, and devices.
- **AI Autonomous Threat Hunter**: Correlates internal anomalies with global events for proactive defense.
- **AI Malware Sandbox**: Automated AI analysis and risk reporting for suspicious files.
- **Natural Language Query**: "Ask the AI" about specific threats, devices, or regional security trends.
- **Multi-Arch Deployment**: Dockerized stack and standalone binaries for Windows, Linux, and macOS.

## 🏗 Project Structure
- `backend/`: FastAPI-based REST API with modular routers and SQLAlchemy models.
- `frontend/`: React dashboard using Material UI and the "CyberSentinel Pro" design system.
- `ai_module/`: Core AI logic for risk scoring, summarization, and threat hunting.
- `osint/`: Intelligence collectors for RSS feeds, web scraping, and hidden browser extraction.
- `agents/`: Lightweight system telemetry collectors for endpoints.
- `.github/workflows/`: Automated CI/CD for multi-arch builds and releases.
- `docker/`: Containerization configuration for the entire stack.

## 🚦 Getting Started
1. **Docker Compose**:
   ```bash
   docker-compose -f docker/docker-compose.yml up --build
   ```
2. **Local Development (Backend)**:
   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```
3. **Local Development (Frontend)**:
   ```bash
   cd frontend
   npm install
   # Run npm start to begin development
   ```

## 🛡 Security & Compliance
- JWT-based authentication for all API endpoints.
- Role-based access control (RBAC).
- Full audit logging and compliance monitoring.

---
*Created by Jules, Powered by AI Intelligence.*
