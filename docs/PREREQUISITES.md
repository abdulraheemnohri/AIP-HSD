# 🛠️ AIP-HSD // System Prerequisites & Toolchains

To run the full-spectrum **AIP-HSD** platform, your system must have the following tools and runtimes installed. Due to the project's hyper-polyglot nature, we recommend using the Dockerized deployment to avoid manual environment setup.

## 🐍 Primary Core
- **Python 3.12+**: Required for Backend (FastAPI), AI Logic, and SOAR engine.
- **Node.js 18+ (LTS)**: Required for React-TS/Next.js frontends and Node.js backend.
- **Go 1.21+**: Required for native agents and Blockchain audit chain.
- **Rust 1.75+ (Cargo)**: Required for Performance Core (PQC/HE/Malware Analysis).

## 🔬 Scientific & Specialized
- **Julia 1.9+**: Required for Risk Forecasting module.
- **Zig 0.11+**: Required for high-speed Packet Parser agent.
- **Elixir 1.15+ / OTP 26+**: Required for Real-time Alert Hub.
- **R 4.3+**: Required for Statistical Threat Modeling.
- **Gfortran 11+**: Required for Monte Carlo Risk Simulator.
- **.NET 6.0 SDK (F#)**: Required for Risk Validator module.

## 🏛️ Legacy & Logic
- **OpenCOBOL (GnuCOBOL)**: Required for Mainframe Security Monitor.
- **Perl 5.30+**: Required for Legacy Log Forensics.
- **Ruby 3.0+**: Required for Platform Maintenance tools.
- **PHP 8.1+**: Required for Legacy Reporting Portal.
- **Clojure CLI / Leiningen**: Required for Logic Rule Engine.
- **GHC (Haskell)**: Required for Formal Policy Verifier.

## 🕸️ Web3 & Kernel
- **Solc (Solidity Compiler)**: Required for Smart Contract Auditor.
- **Clang/LLVM & Libbpf**: Required for eBPF Deep Observability agent.
- **AssemblyScript (asc)**: Required for Wasm Edge Monitor.

## 📱 Mobile & UI
- **Flutter SDK (Dart)**: Required for Mobile Sentinel Dashboard.
- **Xcode (macOS)**: For iOS notification service compilation.
- **Android Studio / SDK**: For Android notification handler.

## 🏗️ Infrastructure
- **Docker & Docker Compose**: Recommended for all-in-one deployment.
- **Terraform 1.5+**: For cloud resource provisioning.
- **Ansible 2.14+**: For automated server configuration.
- **Inno Setup (Windows)**: For generating the Universal .exe Installer.

---
*If you lack these tools, use `docker-compose up` to run the pre-configured environment.*
