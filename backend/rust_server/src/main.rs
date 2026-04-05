use axum::{
    routing::{get, post},
    Json, Router,
};
use serde::{Deserialize, Serialize};
use tower_http::cors::CorsLayer;
use chrono::{DateTime, Utc};

#[derive(Serialize)]
struct Threat {
    id: u32,
    name: String,
    r#type: String,
    risk_score: f64,
    timestamp: DateTime<Utc>,
}

#[derive(Serialize)]
struct Settings {
    performance_mode: bool,
    auth_enabled: bool,
}

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/", get(|| async { Json(serde_json::json!({ "message": "AIP-HSD Rust Universal API is live." })) }))
        .route("/api/threats", get(get_threats))
        .route("/api/settings", get(get_settings))
        .route("/api/compliance/status", get(get_compliance))
        .layer(CorsLayer::permissive());

    let listener = tokio::net::TcpListener::bind("0.0.0.0:8000").await.unwrap();
    println!("Rust Backend running on 0.0.0.0:8000");
    axum::serve(listener, app).await.unwrap();
}

async fn get_threats() -> Json<Vec<Threat>> {
    Json(vec![
        Threat { id: 501, name: "Rust-ZeroDay".to_string(), r#type: "malware".to_string(), risk_score: 99.9, timestamp: Utc::now() },
    ])
}

async fn get_settings() -> Json<Settings> {
    Json(Settings { performance_mode: true, auth_enabled: true })
}

async fn get_compliance() -> Json<serde_json::Value> {
    Json(serde_json::json!({ "iso27001": "COMPLIANT", "pci": "VULNERABLE" }))
}
