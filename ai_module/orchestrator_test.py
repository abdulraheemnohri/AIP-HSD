import datetime
from ai_module.orchestrator import AIOrchestrator

def test_remediation_trigger():
    orchestrator = AIOrchestrator()
    # Mocking findings to trigger remediation
    findings = [
        {
            "severity": "CRITICAL",
            "actions": [{"action": "ISOLATE", "task": "Isolate Cluster Alpha"}]
        }
    ]
    for finding in findings:
        res = orchestrator.trigger_remediation(finding)
        print(f"Test Result: {res}")

if __name__ == "__main__":
    test_remediation_trigger()
