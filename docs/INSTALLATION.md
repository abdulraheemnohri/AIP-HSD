# ⚙️ AIP-HSD // Installation & Environment Setup

This guide provides step-by-step instructions for deploying the **AIP-HSD** platform across its various language implementations.

## 1. Fast Track (Docker)
The easiest way to get started is using Docker Compose.
```bash
docker-compose -f docker/docker-compose.yml up --build
```

## 2. Manual Backend Setup (Choose Your Language)

### 🐍 Python (FastAPI)
```bash
cd backend/python
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 🟢 Node.js (Express)
```bash
cd backend/nodejs
npm install
node src/index.js
```

### 🐹 Go (Gin)
```bash
cd backend/go
go run cmd/main.go
```

### 🦀 Rust (Axum)
```bash
cd backend/rust_server
cargo run --release
```

## 3. Manual Frontend Setup

### ⚛️ React-TS
```bash
cd frontend/react-ts
npm install
# Then run: npm start
```

### ⏭️ Next.js
```bash
cd frontend/nextjs
npm install
# Then run: npm run dev
```

## 4. Building Specialized Agents

### ⚡ Zig Parser
```bash
cd agents/zig
zig build-exe parser.zig
```

### 🔵 Go Native Collector
```bash
cd agents/go
go build -o collector
```

## 5. Running Simulations
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/backend/python:$(pwd)
python3 ai_module/orchestrator.py
```

---
*For troubleshooting, please refer to the specific language sub-directories.*
