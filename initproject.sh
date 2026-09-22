#!/usr/bin/env bash

set -euo pipefail

# Setup the project

PROJECT_NAME="$1"
shift

if [ -z "$PROJECT_NAME" ]; then
    echo "Usage: $0 <project-name>"
    exit 1
fi

uv init "$PROJECT_NAME" --python 3.12

cd "$PROJECT_NAME"

rm main.py

cat >> pyproject.toml <<'EOF'

[build-system]
requires = ["uv_build>=0.9,<0.10"]
build-backend = "uv_build"

[tool.uv.sources]
torch = {index="pytorch-cu132", marker="sys_platform=='win32'"}

[[tool.uv.index]]
name = "pytorch-cu132"
url = "https://download.pytorch.org/whl/cu132"
explicit = true
EOF

# Setup the dir structure

mkdir -p ./{configs,data,papers,notebooks,src/"$PROJECT_NAME",tests}

touch src/"$PROJECT_NAME"/__init__.py

# Add packages

uv add --dev ipykernel

if [ "$#" -gt 0 ]; then
    uv add "$@"
fi

uv sync

echo "Created uv project: $PROJECT_NAME"