# dq-rule-config-api
Data Quality Rule Configuration API which handles the actual onboarding logic (Persisting Rule in the Target DB).

This project uses uv for lightning-fast dependency management.

# Step 1. Install uv :

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Step 2. Project Setup :

# Once uv is installed, clone the repo, navigate to the project directory and initialize your environment:

# Clone and enter the repo
git clone <repository-url>

cd dq-rule-config-api

# Create a virtual environment (.venv)
uv venv

# Activate the environment
# Windows:
.venv\Scripts\activate

# macOS/Linux:
source .venv/bin/activate

# Sync dependencies from pyproject.toml
uv sync

# Step -3 Start that service:
uv run python main.py
