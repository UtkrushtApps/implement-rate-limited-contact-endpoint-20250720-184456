#!/bin/bash
set -e

bash install.sh

echo "[run.sh] API container started. To check status, run: docker ps"
echo "[run.sh] Try: curl http://localhost:8000/employees"
