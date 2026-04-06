import os
import yaml
from typing import Dict, Any

class GlobalConfigManager:
    """Manages platform-wide feature flags and polyglot settings."""

    def __init__(self, config_path: str = "config.yaml"):
        self.config_path = config_path
        self.default_config = {
            "features": {
                "enable_ai_remediation": True,
                "enable_blockchain_audit": True,
                "enable_wasm_edge": True,
                "enable_deception": True
            },
            "polyglot_ports": {
                "python": 8000,
                "nodejs": 8001,
                "go": 8002,
                "rust": 8003
            },
            "osint_settings": {
                "refresh_interval_hours": 1,
                "max_search_results": 10
            }
        }
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                return yaml.safe_load(f)
        return self.default_config

    def get_feature(self, feature_name: str) -> bool:
        return self.config.get("features", {}).get(feature_name, False)

    def update_config(self, new_config: Dict[str, Any]):
        self.config.update(new_config)
        with open(self.config_path, 'w') as f:
            yaml.dump(self.config, f)

global_config = GlobalConfigManager()

if __name__ == "__main__":
    print("Initial Feature Check (Blockchain):", global_config.get_feature("enable_blockchain_audit"))
