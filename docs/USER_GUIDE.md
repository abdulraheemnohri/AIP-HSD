# 📘 AIP-HSD // Functional User Guide

Welcome to the **AIP-HSD** command center. This guide explains how to navigate and utilize the platform's core security intelligence features.

## 1. Dashboard Overview
The main HUD is divided into tactical zones:
- **Global Sentinel Map**: Interactive 3D/2D world map showing threat hotspots. Hover over regions for detailed risk metrics.
- **Risk Cards**: Real-time KPIs for Global/Internal threat levels and overall network health.
- **Live Feed**: A synchronized stream of global OSINT alerts and internal system anomalies.

## 2. AI Intelligence System
### 🤖 Natural Language Query
Use the search bar at the bottom to "Ask the AI."
*   *Example*: "Show all ransomware activity in the last 24 hours."
*   *Example*: "Explain the recent port scan on srv-web-01."

### 🧠 Explainable AI (XAI)
When viewing critical alerts, click on "View Reasoning" to see the XAI breakdown. This report explains the telemetry, correlation paths, and confidence scores behind the AI's decision.

## 3. Autonomous Modules
### 🏹 Threat Hunter
The AI Hunter runs in the background, matching global intelligence with your system's telemetry. Correlated threats appear in the **Threat Correlation Graph**.

### 🧪 Malware Sandbox
Submit suspicious files for analysis. The sandbox generates a detailed behavioral report including:
- Risk score and classification.
- MITRE ATT&CK mapping.
- Automated remediation recommendations.

## 4. Response & Remediation (SOAR)
### 🕹️ War Room (HITL)
High-severity remediation tasks (e.g., "Isolate Endpoint") require manual authorization in the **War Room**. Review the AI's suggestion and click **APPROVE** to execute the SOAR playbook.

## 5. Security & Settings
- **Auth**: Use the profile icon to manage JWT-based sessions.
- **Policies**: Navigate to the Settings icon to enable/disable autonomous remediation and manage RBAC roles.

---
*For technical API documentation, please access the `/docs` endpoint on your chosen backend.*
