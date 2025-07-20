#!/bin/bash
set -e

echo "[install.sh] Building Docker image..."
docker build -t hr-backend .

echo "[install.sh] Starting Docker container..."
CONTAINER_ID=$(docker run -d -p 8000:8000 hr-backend)

echo "[install.sh] Container started with ID: $CONTAINER_ID"
echo "[install.sh] Waiting for the server to start..."
sleep 3

echo "[install.sh] Install complete. API running on http://localhost:8000"
