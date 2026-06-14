#!/bin/bash

# uDos Vault Sync Tool
# Manual synchronization between repos and vault

set -e

# Configuration
CONFIG_FILE="$HOME/.config/udos/sync.yaml"
BACKUP_DIR="$HOME/vault/backups"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo "🔄 uDos Vault Sync Tool v1.0"
echo "============================"
echo ""

# Check if config exists
if [ ! -f "$CONFIG_FILE" ]; then
    echo "${RED}❌ Configuration file not found: $CONFIG_FILE${NC}"
    echo "Create config file first or run 'udos-sync init'"
    exit 1
fi

# Create backup directory
mkdir -p "$BACKUP_DIR"

# Show menu
PS3="Select sync operation: "
options=(
    "Vault → Repo (Publish docs to repo)"
    "Repo → Vault (Edit docs in vault)"
    "Bidirectional (Merge changes)"
    "Show Status"
    "Exit"
)

select opt in "${options[@]}"; do
    case $opt in
        "Vault → Repo (Publish docs to repo)")
            echo "${BLUE}📤 Syncing from vault to repos...${NC}"
            sync_vault_to_repo
            break
            ;;
        "Repo → Vault (Edit docs in vault)")
            echo "${BLUE}📥 Syncing from repos to vault...${NC}"
            sync_repo_to_vault
            break
            ;;
        "Bidirectional (Merge changes)")
            echo "${BLUE}🔄 Bidirectional sync (merge)...${NC}"
            sync_bidirectional
            break
            ;;
        "Show Status")
            show_status
            ;;
        "Exit")
            echo "${YELLOW}👋 Goodbye!${NC}"
            exit 0
            ;;
        *)
            echo "${RED}❌ Invalid option: $REPLY${NC}"
            ;;
    esac
done

sync_vault_to_repo() {
    # Sync uDosHivemind
    echo "Syncing uDosHivemind..."
    rsync -avh --progress \
        "$HOME/vault/repos/uDosHivemind/" \
        "/Users/fredbook/code-vault/uDosHivemind/" \
        --exclude='.git/' \
        --exclude='node_modules/'
    
    # Sync uDosRe3ngine
    echo "Syncing uDosRe3ngine..."
    rsync -avh --progress \
        "$HOME/vault/repos/uDosRe3ngine/" \
        "/Users/fredbook/code-vault/uDosRe3ngine/" \
        --exclude='.git/' \
        --exclude='node_modules/'
    
    # Sync uDevFramework
    echo "Syncing uDevFramework..."
    rsync -avh --progress \
        "$HOME/vault/repos/uDevFramework/" \
        "/Users/fredbook/code-vault/uDevFramework/" \
        --exclude='.git/' \
        --exclude='node_modules/'
    
    echo "${GREEN}✅ Vault → Repo sync complete${NC}"
}

sync_repo_to_vault() {
    # Sync uDosHivemind
    echo "Syncing uDosHivemind..."
    rsync -avh --progress \
        "/Users/fredbook/code-vault/uDosHivemind/" \
        "$HOME/vault/repos/uDosHivemind/" \
        --exclude='.git/' \
        --exclude='node_modules/'
    
    # Sync uDosRe3ngine
    echo "Syncing uDosRe3ngine..."
    rsync -avh --progress \
        "/Users/fredbook/code-vault/uDosRe3ngine/" \
        "$HOME/vault/repos/uDosRe3ngine/" \
        --exclude='.git/' \
        --exclude='node_modules/'
    
    # Sync uDevFramework
    echo "Syncing uDevFramework..."
    rsync -avh --progress \
        "/Users/fredbook/code-vault/uDevFramework/" \
        "$HOME/vault/repos/uDevFramework/" \
        --exclude='.git/' \
        --exclude='node_modules/'
    
    echo "${GREEN}✅ Repo → Vault sync complete${NC}"
}

sync_bidirectional() {
    echo "${YELLOW}⚠️  Bidirectional sync creates backups first...${NC}"
    
    # Create timestamped backup
    BACKUP_NAME="backup-$(date +%Y%m%d-%H%M%S)"
    mkdir -p "$BACKUP_DIR/$BACKUP_NAME"
    
    echo "Creating backup..."
    cp -r "$HOME/vault/repos/" "$BACKUP_DIR/$BACKUP_NAME/"
    
    # Sync in both directions
    echo "Syncing vault to repos..."
    sync_vault_to_repo
    
    echo "Syncing repos to vault..."
    sync_repo_to_vault
    
    echo "${GREEN}✅ Bidirectional sync complete${NC}"
    echo "Backup created at: $BACKUP_DIR/$BACKUP_NAME/"
}

show_status() {
    echo "${BLUE}📊 Vault Sync Status${NC}"
    echo "===================="
    
    # Check vault structure
    if [ -d "$HOME/vault/repos/uDosHivemind" ]; then
        echo "✅ uDosHivemind vault: $(find "$HOME/vault/repos/uDosHivemind" -type f | wc -l) files"
    else
        echo "❌ uDosHivemind vault: Not found"
    fi
    
    if [ -d "$HOME/vault/repos/uDosRe3ngine" ]; then
        echo "✅ uDosRe3ngine vault: $(find "$HOME/vault/repos/uDosRe3ngine" -type f | wc -l) files"
    else
        echo "❌ uDosRe3ngine vault: Not found"
    fi
    
    if [ -d "$HOME/vault/repos/uDevFramework" ]; then
        echo "✅ uDevFramework vault: $(find "$HOME/vault/repos/uDevFramework" -type f | wc -l) files"
    else
        echo "❌ uDevFramework vault: Not found"
    fi
    
    # Check backups
    if [ -d "$BACKUP_DIR" ]; then
        echo "✅ Backups: $(find "$BACKUP_DIR" -mindepth 1 -maxdepth 1 -type d | wc -l) available"
    else
        echo "❌ Backups: None"
    fi
    
    echo ""
}

# Run the selected operation
case $opt in
    "Vault → Repo (Publish docs to repo)") sync_vault_to_repo ;;
    "Repo → Vault (Edit docs in vault)") sync_repo_to_vault ;;
    "Bidirectional (Merge changes)") sync_bidirectional ;;
    "Show Status") show_status ;;
esac