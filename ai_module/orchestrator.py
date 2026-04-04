import datetime
from typing import List, Dict
from ai_module.analyzer import SecurityAnalyzer
from osint.rss_collector import RSSCollector
from agents.collector import SystemCollector

class AIOrchestrator:
    def __init__(self):
        self.analyzer = SecurityAnalyzer()
        self.rss_collector = RSSCollector()
        self.system_collector = SystemCollector()
        self.last_run = None

    def execute_intelligence_cycle(self) -> Dict:
        """Coordinates the flow between OSINT, Agents, and AI analysis."""
        print(f"[{datetime.datetime.now()}] AI Orchestrator: Starting full-spectrum cycle...")

        # 1. Gather Global OSINT
        global_intel = self.rss_collector.fetch_latest()

        # 2. Gather Internal Telemetry
        internal_telemetry = self.system_collector.run_cycle()

        # 3. Analyze and Correlate
        findings = self.analyzer.autonomous_threat_hunter(
            internal_telemetry.get("logs", []),
            global_intel
        )

        # 4. Update Risk Scores (Simulated Rust call)
        risk_score = self.analyzer.calculate_risk_score(findings, internal_telemetry.get("logs", []))

        # 5. Generate Summary
        summary = self.analyzer.generate_summary(findings)

        self.last_run = datetime.datetime.now()

        return {
            "timestamp": self.last_run.isoformat(),
            "findings": findings,
            "overall_risk_score": risk_score,
            "executive_summary": summary,
            "status": "ANALYSIS_COMPLETE"
        }

if __name__ == "__main__":
    orchestrator = AIOrchestrator()
    result = orchestrator.execute_intelligence_cycle()
    import json
    print(json.dumps(result, indent=2))
