import datetime
import json
from typing import List, Dict
from ai_module.analyzer import SecurityAnalyzer
from ai_module.adversarial_shield import AdversarialAIDefense
from osint.rss_collector import RSSCollector
from agents.collector import SystemCollector
from backend.python.app.services.soar import soar_engine
from backend.python.app.services.sandbox import sandbox_service
from backend.python.app.services.deception import deception_service

class AIOrchestrator:
    def __init__(self):
        self.analyzer = SecurityAnalyzer()
        self.shield = AdversarialAIDefense()
        self.rss_collector = RSSCollector()
        self.system_collector = SystemCollector()
        self.last_run = None

    def execute_intelligence_cycle(self, tenant_id: str = "DEFAULT") -> Dict:
        """Coordinates the flow between all advanced services."""
        print(f"[{datetime.datetime.now()}] AI Orchestrator: Starting spectrum cycle for {tenant_id}...")

        # 1. Gather Global OSINT
        global_intel = self.rss_collector.fetch_latest()

        # 2. Gather Internal Telemetry
        internal_telemetry = self.system_collector.run_cycle()

        # 3. Analyze and Correlate
        findings = self.analyzer.autonomous_threat_hunter(
            internal_telemetry.get("logs", []),
            global_intel
        )

        # 4. Check Deception Decoys
        deception_hits = deception_service.check_decoy_alerts()
        if deception_hits:
            findings.extend(deception_hits)

        # 5. Trigger Automated SOAR Remediation
        remediation_results = []
        for finding in findings:
            if finding.get("severity") in ["HIGH", "CRITICAL"]:
                res = soar_engine.execute_playbook("RANSOMWARE_CONTAINMENT", finding, tenant_id)
                remediation_results.append(res)

        # 6. Final Summary
        summary = self.analyzer.generate_summary(findings)

        self.last_run = datetime.datetime.now()

        return {
            "timestamp": self.last_run.isoformat(),
            "tenant_id": tenant_id,
            "findings_count": len(findings),
            "remediation_status": remediation_results,
            "executive_summary": summary,
            "status": "FULL_SPECTRUM_ANALYSIS_COMPLETE"
        }

if __name__ == "__main__":
    orchestrator = AIOrchestrator()
    result = orchestrator.execute_intelligence_cycle("ALPHA-ORG")
    print(json.dumps(result, indent=2))
