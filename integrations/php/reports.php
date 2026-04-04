<?php
/**
 * AIP-HSD Legacy Reporting Portal Stub (PHP)
 * Used for compatibility with older web-based SOC interfaces.
 */

class LegacyReporter {
    private $version = "2.4.1";

    public function generateReport($data) {
        return json_encode([
            "portal" => "Legacy SOC Web Interface",
            "version" => $this->version,
            "timestamp" => date('Y-m-d H:i:s'),
            "report_data" => $data,
            "status" => "COMPATIBILITY_MODE_ACTIVE"
        ]);
    }
}

$reporter = new LegacyReporter();
$mockData = ["high_priority_alerts" => 5, "last_sync" => "2024-04-04"];
echo $reporter->generateReport($mockData);
?>
