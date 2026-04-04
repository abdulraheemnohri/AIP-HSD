import datetime
import logging
from typing import Optional

class AuditService:
    def __init__(self, log_file: str = "audit_log.txt"):
        self.logger = logging.getLogger("AIP-HSD-Audit")
        self.logger.setLevel(logging.INFO)

        # Simple file handler for initial implementation
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_action(self, user: str, action: str, resource: str, status: str = "SUCCESS", details: Optional[str] = None):
        """Records a security-relevant action in the audit log."""
        log_msg = f"USER: {user} | ACTION: {action} | RESOURCE: {resource} | STATUS: {status} | DETAILS: {details or 'N/A'}"
        self.logger.info(log_msg)
        print(f"[AUDIT] {log_msg}") # Echo to console for visibility

audit_service = AuditService()

if __name__ == "__main__":
    audit_service.log_action("admin", "LOGIN", "API_AUTH_TOKEN", "SUCCESS")
    audit_service.log_action("analyst", "QUERY", "AI_SENTINEL", "SUCCESS", "Anomalous traffic in Sector 7")
