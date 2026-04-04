#!/bin/bash
# AIP-HSD Build Script for Multi-Arch Binaries and Docker
VERSION="1.0.0"

echo "Building AIP-HSD v$VERSION..."

# 1. Install dependencies
pip install pyinstaller -r backend/requirements.txt

# 2. Build Multi-Arch Binaries (Example for x86_64)
echo "Generating x86_64 binaries with PyInstaller..."
pyinstaller --onefile --name hsod-linux-x86_64 backend/main.py

# 3. Build Docker Image
echo "Building multi-arch Docker images..."
# This requires docker buildx to be configured for multi-arch
# docker buildx build --platform linux/amd64,linux/arm64 -t yourusername/hsod:latest -f docker/Dockerfile . --push

echo "Build process complete."
