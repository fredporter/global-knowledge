# 🗃️ uDos Vault

## Vault-First Documentation Architecture

This vault implements the **Vault-First Documentation** pattern to keep public repositories clean while maintaining comprehensive working documentation locally.

## 📁 Structure

```
vault/
├── README.md                    # This file
├── repos/                       # Mirror of repo documentation
│   ├── uDosHivemind/             # Hivemind docs
│   │   ├── docs/                 # API and guides
│   │   ├── roadmaps/             # Development roadmaps
│   │   └── dev-plans/            # Implementation plans
│   ├── uDosRe3ngine/             # Re3ngine docs
│   └── uDevFramework/            # Framework docs
├── @inbox/                      # Incoming briefs and tasks
├── @outbox/                     # Outgoing deliverables
├── feeds/                       # Reply and notification storage
├── backups/                     # Sync backups
├── tools/                       # Vault utilities
│   └── vault-sync.sh             # Sync script
└── personal/                    # Personal notes (optional)
```

## 🎯 Philosophy

**Public Repos = Scaffold Only**
- Only source code and build configuration
- Minimal README pointing to vault
- No working docs, plans, or summaries

**Vault = Working Documentation**
- All development artifacts
- Roadmaps, plans, summaries
- Feed data and replies
- Full freedom to iterate

## 🔄 Sync Configuration

Sync is configured in `~/.config/udos/sync.yaml` with three modes:

### 1. Vault → Repo (Publish)
```bash
# When docs are finalized and ready for GitHub
./vault/tools/vault-sync.sh
# Select "Vault → Repo"
```

### 2. Repo → Vault (Edit)
```bash
# Pull latest docs from repo to vault for editing
./vault/tools/vault-sync.sh
# Select "Repo → Vault"
```

### 3. Bidirectional (Merge)
```bash
# Two-way sync with backup (for collaborative editing)
./vault/tools/vault-sync.sh
# Select "Bidirectional"
```

## 📋 Workflow Examples

### Creating New Documentation

```bash
# 1. Create in vault (not in repo)
vim vault/repos/uDosHivemind/dev-plans/phase-3.md

# 2. Edit, review, iterate locally

# 3. When ready to publish
./vault/tools/vault-sync.sh  # Vault → Repo

# 4. Commit to GitHub
cd ~/code-vault/uDosHivemind
git add docs/
git commit -m "docs: add phase 3 dev plan"
git push
```

### Editing Existing Documentation

```bash
# 1. Pull latest from repo to vault
./vault/tools/vault-sync.sh  # Repo → Vault

# 2. Edit in vault
vim vault/repos/uDosHivemind/README.md

# 3. Push back to repo
./vault/tools/vault-sync.sh  # Vault → Repo

# 4. Commit changes
cd ~/code-vault/uDosHivemind
git commit -m "docs: update README"
git push
```

### Collaborative Editing

```bash
# 1. Create backup
./vault/tools/vault-sync.sh  # Bidirectional

# 2. Team edits in vault
# Team edits in repos

# 3. Merge changes with backup
./vault/tools/vault-sync.sh  # Bidirectional

# 4. Review backup at ~/vault/backups/backup-YYYYMMDD-HHMMSS/
```

## 🛡️ Benefits

| Concern | Solution |
|---------|----------|
| **Repo bloat** | Repos stay lean, only code + scaffold |
| **Project bleed** | Working docs never in public repos |
| **Editing freedom** | Use any MD editor on vault files |
| **Publishing control** | Sync vault→repo when docs are ready |
| **Backup** | Vault separate from code versioning |
| **Multi-device** | Sync vault across machines |

## 📊 Status

Run the sync tool to check current status:

```bash
./vault/tools/vault-sync.sh
# Select "Show Status"
```

## 🔧 Maintenance

### Adding New Repo

```bash
# 1. Create vault structure
mkdir -p vault/repos/new-repo/{docs,roadmaps,dev-plans}

# 2. Update sync config
vim ~/.config/udos/sync.yaml

# 3. Create minimal README in repo
```

### Backup Management

Backups are created in `~/vault/backups/` with timestamped directories.
Max 5 backups are kept (configurable in sync.yaml).

## 🎯 Best Practices

1. **Edit in Vault First**: Always create/edit docs in vault before publishing
2. **Sync Before Commit**: Pull latest changes before publishing
3. **Backup Before Merge**: Use bidirectional sync for collaborative work
4. **Keep Repos Clean**: Never commit working docs to public repos
5. **Document Everything**: Use vault for all development artifacts

## 🚀 Getting Started

```bash
# Navigate to vault
cd ~/vault

# Check status
./tools/vault-sync.sh

# Start editing
vim repos/uDosHivemind/dev-plans/new-feature.md

# Publish when ready
./tools/vault-sync.sh  # Vault → Repo
```

---

**Architecture**: Vault-First Documentation
**Status**: Operational
**Maintainer**: Fred Porter
**License**: MIT