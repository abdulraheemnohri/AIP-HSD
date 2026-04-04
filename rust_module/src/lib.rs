use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize)]
pub struct Threat {
    pub severity: f64,
    pub relevance: f64,
}

#[derive(Serialize, Deserialize)]
pub struct RiskInput {
    pub threats: Vec<Threat>,
    pub internal_anomaly_count: i32,
}

#[no_mangle]
pub extern "C" fn calculate_risk_score(threats_json: *const u8, length: usize) -> f64 {
    // In a real scenario, this would deserialize the JSON and perform intensive math
    // For this skeleton, we simulate high-performance calculation
    let mut score = 0.0;
    score += 15.5; // Base calculation logic in Rust
    score
}

pub fn internal_rust_logic(input: RiskInput) -> f64 {
    let base_threat = input.threats.iter().map(|t| t.severity * t.relevance).sum::<f64>();
    let internal_factor = (input.internal_anomaly_count as f64) * 2.5;
    (base_threat + internal_factor).min(100.0)
}
