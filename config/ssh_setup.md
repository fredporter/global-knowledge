# SSH Setup — Local Configuration

> **Source Machine:** wizard-server (192.168.20.11)
> **Last Updated:** 2026-04-20
> **Purpose:** SSH setup for connecting to other machines on the local network.

---

## SSH Key

| Field | Value |
|---|---|
| Algorithm | ED25519 |
| Public Key | `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINlBTh7l0lDxGkKz3EAee0YQ6DCyJFmZf2WN13pKX1nm` |
| Fingerprint | `SHA256:FloltrPEwzi/+jDKXnX8l8ye6TMVhGeo9xlx0pzKG4c` |
| Private Key | `~/.ssh/id_ed25519` |

## SSH Config File

Created at `~/.ssh/config` with these hosts:

| Host Alias | Target |
|---|---|
| `localhost` / `wizard-server` | 127.0.0.1 (this machine) |
| `other-machine` / `lan-other` | 192.168.20.7 (other computer) |
| `other-device` / `lan-device` | 192.168.20.13 (other device) |

## Connect Commands

```bash
ssh localhost           # self-test
ssh other-machine       # connect to .7
ssh other-device        # connect to .13
```

## Copy Key to Remote

On remote machine, add the public key:

```bash
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINlBTh7l0lDxGkKz3EAee0YQ6DCyJFmZf2WN13pKX1nm wizard@wizard-server" >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

Or from this machine:

```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub wizard@192.168.20.7
ssh-copy-id -i ~/.ssh/id_ed25519.pub wizard@192.168.20.13
```

## SSH Server (on this machine)

OpenSSH server is not installed. To enable incoming connections:

```bash
sudo apt-get install openssh-server
sudo systemctl enable --now sshd
```

## Network

```
192.168.20.0/24
 .1    Gateway (router)
 .7    Other machine
 .11   wizard-server (this machine)
 .13   Other device
```

---

*Stored in Vault — Vault-First Documentation pattern.*


## Update: SSH Server Now Running

✅ **OpenSSH server is installed and active on wizard-server**

| Detail | Value |
|---|---|
| Status | `active (running)` |
| Listen | 0.0.0.0:22 and [::]:22 |
| Auth | Public key (ED25519) + password |
| Self-test | `ssh localhost` — ✅ works |

Other machines (.7 and .13) are not yet running SSH servers.

---

*Updated: 2026-04-20 - SSH server enabled*

---

## 🏗️ Multi-Machine Dev Environment

### Machines
| Machine | IP | Hostname | Role |
|---------|-----|----------|------|
| **Ubuntu** (this) | 192.168.20.11 | wizard-server | Secret store + build worker + vault host |
| **macOS** | 192.168.20.7 | MacMini | Primary dev + release control |

### 🔐 Secret Server (Ubuntu → macOS)
- **Status:** ✅ Running on port 30001
- **Script:** `~/Code/DevStudio/scripts/secret-server.py`
- **Token:** Stored in `~/.local/token`
- **Secrets:** Stored encrypted in `~/.local/env/secrets.enc`
- **Available keys:** OPENROUTER_API_KEY, MISTRAL_API_KEY, DEEPSEEK_API_KEY, OPENAPI_KEY, ANTHROPIC_API_KEY, GEMINI_API_KEY, GITHUB_PAT

### 📡 How macOS Fetches Secrets
```bash
# On macOS, source the helper:
source ~/Code/DevStudio/config/ubuntu-secret-helper.sh

# Fetch any secret:
export OPENROUTER_API_KEY=$(get_secret OPENROUTER_API_KEY)
export GITHUB_TOKEN=$(get_secret GITHUB_PAT)
```

### 🚀 Release Pipeline
- **Release script:** `~/Code/DevStudio/config/release`
- **Usage:** `release all v1.0.0`
- **Fetching secrets:** Release script auto-sources ubuntu-secret-helper.sh

### 📚 DevStudio Ecosystem Docs
- `~/Code/DevStudio/docs/MULTI_MACHINE_SETUP.md` — architecture overview

### 🔄 Configuration Sync
```bash
# On macOS (source):
cd ~/Code/DevStudio && git add . && git commit -m "Update configs" && git push

# On Ubuntu:
cd ~/Code/DevStudio && git pull
```
