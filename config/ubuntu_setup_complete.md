# Ubuntu Machine Setup — Complete

> **Machine:** wizard-server (192.168.20.11)
> **Role:** Secret store + always-on server
> **Last Updated:** 2026-04-20

---

## ✅ Setup Summary

| Component | Status | Details |
|-----------|--------|---------|
| OpenSSH Server | ✅ Running | Port 22, ED25519 key |
| Secret Server | ✅ Running | Port 30001, systemd auto-start |
| DevStudio Repo | ✅ Synced | `~/Code/DevStudio` — latest pushed |
| Hivemind (Rust) | ✅ Cloned | `~/Code/OkAgentDigital/Hivemind` |
| OkGuide (Python/Node) | ✅ Cloned | `~/Code/OkAgentDigital/OkGuide` |
| Vault | ✅ Documented | This note |

## 🔐 Secret Server

**Endpoint:** `http://192.168.20.11:30001`
**Auth Header:** `X-Secret-Token: <token>`

### Secrets Available
- `OPENROUTER_API_KEY`
- `MISTRAL_API_KEY`
- `DEEPSEEK_API_KEY`
- `OPENAPI_KEY`
- `ANTHROPIC_API_KEY`
- `GEMINI_API_KEY`
- `GITHUB_PAT`

### Test Commands
```bash
# Health check
curl -s http://localhost:30001/health

# List secrets
curl -s http://localhost:30001/api/secrets

# Get a secret (with token)
TOKEN=$(cat ~/.local/token)
curl -s -H "X-Secret-Token: $TOKEN" http://localhost:30001/api/secrets/OPENROUTER_API_KEY
```

### Files
- **Script:** `~/Code/DevStudio/scripts/secret-server.py`
- **Systemd:** `~/.config/systemd/user/ubuntu-secret-server.service`
- **Token:** `~/.local/token`
- **Encrypted store:** `~/.local/env/secrets.enc`
- **Master key:** `~/.local/env/master.key`

## 📂 DevStudio Repo

**Path:** `~/Code/DevStudio`
**Remote:** `https://github.com/OkAgentDigital/DevStudio.git`

### Files Created (Ubuntu side)
| File | Purpose |
|------|---------|
| `scripts/secret-server.py` | HTTP secret server (stdlib) |
| `scripts/install-secret-server-service.sh` | One-command systemd installer |
| `config/ubuntu-secret-helper.sh` | Helper for macOS to fetch secrets |
| `config/release` | Unified release script (tag & push) |
| `docs/MULTI_MACHINE_SETUP.md` | Full architecture documentation |

## 🤖 OkGuide (Python/Node.js — Ollama Local)

**Path:** `~/Code/OkAgentDigital/OkGuide`

OkGuide is a **standalone** local LLM assistant. It is NOT dependent on Hivemind.

### Python TUI
```bash
cd ~/Code/OkAgentDigital/OkGuide
# Activate venv
source venv/bin/activate
# Run TUI
python agent.py
# Or with C64 mode
python agent.py --c64
# Or with a specific model
python agent.py --model deepseek-coder:1.3b
```

### Node.js API Server (OpenAI-compatible + MCP)
```bash
cd ~/Code/OkAgentDigital/OkGuide/src/api
# Requires Node.js and dependencies
node server.js
# Runs on port 30000 with MCP on port 3010
```

### Architecture
```
┌─────────────────────────────────────┐
│           OkGuide                    │
│                                     │
│  ┌─────────────┐  ┌──────────────┐  │
│  │ Python TUI  │  │ Node.js API  │  │
│  │ (agent.py)  │  │ (server.js)  │  │
│  └──────┬──────┘  └──────┬───────┘  │
│         │                │          │
│         └──────┬─────────┘          │
│                ▼                    │
│         ┌──────────┐               │
│         │  Ollama  │               │
│         │ (local)  │               │
│         └──────────┘               │
└─────────────────────────────────────┘
```

## 🔄 Hivemind (Rust — Orchestrator)

**Path:** `~/Code/OkAgentDigital/Hivemind`
**Config:** `~/.local/config/udos/hivemind.yaml`
**Port:** 30000 (OpenAI-compatible API)
**MCP Port:** Part of the same binary

### To Build
```bash
cd ~/Code/OkAgentDigital/Hivemind
cargo build --release
```

### To Run
```bash
./target/release/hivemind
# Loads config from ~/.local/config/udos/hivemind.yaml
```

## 📝 Quick Reference

### Daily Commands

```bash
# Check secret server
systemctl --user status ubuntu-secret-server

# View logs
journalctl --user -u ubuntu-secret-server -f

# Pull latest DevStudio configs
cd ~/Code/DevStudio && git pull

# Update Hivemind
cd ~/Code/OkAgentDigital/Hivemind && git pull

# Update OkGuide
cd ~/Code/OkAgentDigital/OkGuide && git pull

# Run OkGuide TUI
cd ~/Code/OkAgentDigital/OkGuide && source venv/bin/activate && python agent.py
```

### Network
```
192.168.20.0/24
 .1     Gateway (router)
 .7     macOS dev machine
 .11    ✦ Ubuntu server (this machine)
```

---

*Vault-First Documentation — Stored in ~/Vault/{system}/{config}/*
