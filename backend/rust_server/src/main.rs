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
    source: String,
    risk_score: f64,
    location: String,
    description: String,
    timestamp: DateTime<Utc>,
}

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/", get(|| async { Json(serde_json::json!({ "message": "AIP-HSD Rust Universal API is live." })) }))
        .route("/api/threats", get(get_threats))
        .layer(CorsLayer::permissive());

    let listener = tokio::net::TcpListener::bind("0.0.0.0:8000").await.unwrap();
    println!("Rust Backend running on 0.0.0.0:8000");
    axum::serve(listener, app).await.unwrap();
}

async fn get_threats() -> Json<Vec<Threat>> {
    Json(vec![
        Threat {
            id: 501,
            name: "Rust-ZeroDay-Alpha".to_string(),
            r#type: "malware".to_string(),
            source: "RUST-INTEL".to_string(),
            risk_score: 99.9,
            location: "EMEA".to_string(),
            description: "High-performance Rust detection engine alert.".to_string(),
            timestamp: Utc::now()
        },
    ])
}
