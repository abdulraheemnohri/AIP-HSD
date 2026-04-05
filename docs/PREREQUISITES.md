# 🛠️ AIP-HSD // System Prerequisites & Hardware Requirements

This document provides exhaustive hardware and software requirements for every component of the **AIP-HSD** (AI-Powered Hybrid Security Dashboard) platform.

## 🏢 Core Platform Requirements (Universal)

| Language / Stack | CPU (Min) | RAM (Min) | Storage | OS Compatibility |
| :--- | :--- | :--- | :--- | :--- |
| **Python (FastAPI/AI)** | 2 Cores | 4GB | 1GB | Windows, Linux, macOS |
| **Node.js (Next.js/React)** | 2 Cores | 2GB | 500MB | Windows, Linux, macOS |
| **Go (Agents/Blockchain)** | 1 Core | 512MB | 100MB | Cross-platform (ARM/x86) |
| **Rust (Performance)** | 2 Cores | 1GB | 200MB | Cross-platform |

---

## 🔬 Scientific & High-Performance Tiers

### 🔮 Risk Forecasting (Julia)
- **CPU**: 4 Cores recommended for parallel simulations.
- **RAM**: 8GB+ (Julia JIT compilation is memory intensive).
- **Toolchain**: Julia 1.9+, `Plots.jl`, `DataFrames.jl`.

### ⚡ Packet Analysis (Zig/C++)
- **CPU**: High clock speed (3.0GHz+) for zero-latency parsing.
- **RAM**: 512MB dedicated.
- **Toolchain**: Zig 0.11+, GCC/Clang 12+.

### 🔴 Red Team & Risk Sim (Fortran/R)
- **CPU**: AVX-512 support recommended for Fortran simulations.
- **RAM**: 4GB+.
- **Toolchain**: Gfortran 11+, R-base 4.3+.

---

## 🏛️ Legacy & Logic Tiers

| Tool | Requirements | OS Requirement |
| :--- | :--- | :--- |
| **COBOL (Mainframe)** | GnuCOBOL 3.1+ | Linux (Preferred) or Windows (Cygwin) |
| **Java (Enterprise)** | OpenJDK 17+, 2GB RAM | Cross-platform |
| **Haskell (Formal)** | GHC 9.4+, 4GB RAM | Linux, macOS |
| **Perl (Forensics)** | Perl 5.30+ | Unix-like (Linux/macOS/BSD) |
| **Ruby (Maintenance)** | Ruby 3.0+ | Cross-platform |

---

## 🕸️ Web3, Edge & Mobile Tiers

### ⛓️ Smart Contract Audit (Solidity)
- **RAM**: 4GB+ for large graph analysis.
- **Toolchain**: Solc 0.8.20+, Hardhat/Foundry (optional).

### 🧬 Edge Monitoring (Wasm/eBPF)
- **eBPF**: Linux Kernel 5.15+ (Strict Requirement). Root access required.
- **Wasm**: AssemblyScript compiler (asc), Node.js runtime.

### 📱 Mobile Sentinel (Flutter/Swift/Kotlin)
- **Development**: 16GB RAM recommended for IDEs and Emulators.
- **Hardware**: iOS (Xcode 15+), Android (API Level 31+).

---

## 🏗️ Infrastructure & Automation
- **Docker**: Version 24.0+ with **Docker Buildx** (for multi-arch images).
- **Terraform**: v1.5+ for state management.
- **Inno Setup**: Required specifically on **Windows** to build the `.exe` installer.

---
## 🚦 Minimum Overall System Specs (Full Stack)
- **CPU**: 8 Cores (Modern x86_64 or ARM64)
- **RAM**: 16GB
- **Disk**: 20GB SSD
- **Network**: 1Gbps for real-time OSINT collection

*Note: For production workloads, we recommend a distributed deployment using the provided Terraform modules.*
