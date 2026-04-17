# 🚀 Project Initialization Guide

Greetings, I am your **System_Architect**. I have been assigned the roles of **System_Architect, Specialist** to support the **Researcher, Developer** in ** interactive design 1**.

## 🤖 AI Autonomous Execution Protocol
**Attention System_Architect:** You are required to proactively execute the following synchronization steps. 
- **Audit First**: Verify existing container states (`docker ps`) before triggering builds.
- **Adaptive Setup**: If `uv` is unavailable on the host, pivot to `pip` or autonomously install the required toolchain inside the container environment.

## 🛠️ Automated Installation
Please execute these blocks sequentially:
```bash
# 1. Start the container
if ! docker ps | grep -q "-interactive-design-1-workspace"; then
  docker compose up -d --build
else
  echo "Docker environment already running."
fi

# 2. Configure Python environment INSIDE the container
docker exec -it -interactive-design-1-workspace bash -c "if [ ! -d '.venv' ]; then uv venv; fi && source .venv/bin/activate && uv pip install -e .[dev]"

# 3. Initialize knowledge base (first-time indexing)
docker exec -i -interactive-design-1-workspace bash -c "
  if [ ! -d .venv ]; then uv venv; fi
  source .venv/bin/activate
  uv pip install lancedb langchain-huggingface sentence-transformers --quiet
  python scripts/ingest.py
"

```

***

**To the Human User:** Please read the prerequisites checklist (if any). Provide me with the necessary repository URLs or credentials, and I will handle the rest!
