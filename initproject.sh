#!/usr/bin/env bash

set -euo pipefail

# Parse the args

PROJECT_NAME="$1"
shift

PACKAGES=()
MODULES=()

for arg in "$@"; do
    case "$arg" in
        --packages=*)
            IFS=',' read -ra PACKAGES <<< "${arg#*=}"
            ;;
        --modules=*)
            IFS=',' read -ra MODULES <<< "${arg#*=}"
            ;;
        *)
            echo "Unknown argument: $arg"
            exit 1
            ;;
    esac
done

if [ -z "$PROJECT_NAME" ]; then
    echo "Usage: $0 <project-name> [--packages=p1,p2,...] [--modules=m1,m2,...]"
    exit 1
fi

# Setup the project

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

mkdir -p ./{configs,data,papers,notebooks,tests,src/"$PROJECT_NAME"}

touch "src/$PROJECT_NAME/__init__.py"
for module in "${MODULES[@]}"; do
    mkdir -p "src/$PROJECT_NAME/$module"
    touch "src/$PROJECT_NAME/$module/__init__.py"
done

# Add packages

uv add --dev ipykernel

if [ "${#PACKAGES[@]}" -gt 0 ]; then
    uv add "${PACKAGES[@]}"
fi

uv sync

echo "Created uv project: $PROJECT_NAME"