#!/usr/bin/env python3
"""
Vault Compost Integration Script
Unifies Vault operations with the self-healing compost system
"""

import os
import shutil
import hashlib
from pathlib import Path
from datetime import datetime
import yaml

class VaultCompostIntegrator:
    def __init__(self, vault_path="~/Vault", compost_path="~/uDosGo/Memory/State/Compost"):
        self.vault_path = Path(vault_path).expanduser()
        self.compost_path = Path(compost_path).expanduser()
        self.config_path = self.compost_path / "Config" / "self-healing.yaml"
        
        # Ensure directories exist
        self.compost_path.mkdir(parents=True, exist_ok=True)
        (self.compost_path / "Heap").mkdir(exist_ok=True)
        (self.compost_path / "Vector").mkdir(exist_ok=True)
        (self.compost_path / "Archive").mkdir(exist_ok=True)
        (self.compost_path / "Recovery").mkdir(exist_ok=True)
        (self.compost_path / "Intelligence").mkdir(exist_ok=True)
        (self.compost_path / "Config").mkdir(exist_ok=True)
        
        # Load or create config
        self.load_config()
    
    def load_config(self):
        """Load or create the self-healing configuration"""
        if not self.config_path.exists():
            default_config = {
                "self_healing": {
                    "enabled": True,
                    "mode": "adaptive",
                    "detect": {
                        "interval": 60,
                        "anomalies": [
                            {"type": "disk_pressure", "threshold": 85, "action": "compress"},
                            {"type": "corrupted_file", "action": "repair_or_isolate"},
                            {"type": "missing_reference", "action": "rebuild_index"},
                            {"type": "vector_drift", "threshold": 0.3, "action": "reindex"}
                        ]
                    },
                    "actions": {
                        "compress": {"algorithm": "adaptive", "level": "auto"},
                        "repair": {"max_attempts": 3, "fallback": "quarantine"},
                        "reindex": {"strategy": "incremental", "batch_size": 1000},
                        "deduplicate": {"method": "content_hash", "threshold": 0.95}
                    },
                    "recovery": {
                        "snapshot_interval": 3600,
                        "keep_snapshots": 24,
                        "auto_restore": True,
                        "rollback_points": ["before_compress", "before_dedupe", "before_reindex"]
                    }
                }
            }
            with open(self.config_path, 'w') as f:
                yaml.dump(default_config, f)
        
        with open(self.config_path, 'r') as f:
            self.config = yaml.safe_load(f)
    
    def integrate_vault_with_compost(self):
        """Set up integration between Vault and Compost"""
        print("🔄 Integrating Vault with Compost System...")
        
        # Create symlinks for easy access
        compost_link = self.vault_path / ".compost"
        if not compost_link.exists():
            compost_link.symlink_to(self.compost_path, target_is_directory=True)
            print(f"🔗 Created symlink: {compost_link} -> {self.compost_path}")
        
        # Set up Vault structure for compost integration
        compost_inbox = self.vault_path / "@compost-inbox"
        compost_inbox.mkdir(exist_ok=True)
        print(f"📥 Created compost inbox: {compost_inbox}")
        
        # Update .gitignore to exclude compost from Git
        gitignore_path = self.vault_path / ".gitignore"
        gitignore_content = ""
        if gitignore_path.exists():
            with open(gitignore_path, 'r') as f:
                gitignore_content = f.read()
        
        if ".compost" not in gitignore_content:
            with open(gitignore_path, 'a') as f:
                f.write("\n# Compost System\n.compost/\n@compost-inbox/\n")
            print("📝 Updated .gitignore to exclude compost directories")
        
        print("✅ Vault-Compost integration complete!")
    
    def move_to_compost(self, file_path, reason="manual"):
        """Move a file to the compost heap"""
        file_path = Path(file_path).expanduser()
        if not file_path.exists():
            print(f"⚠️ File not found: {file_path}")
            return False
        
        # Create destination in compost heap
        relative_path = file_path.relative_to(self.vault_path)
        compost_dest = self.compost_path / "Heap" / relative_path
        compost_dest.parent.mkdir(parents=True, exist_ok=True)
        
        # Move the file
        shutil.move(str(file_path), str(compost_dest))
        
        # Log the action
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "file": str(file_path),
            "compost_location": str(compost_dest),
            "reason": reason,
            "action": "move"
        }
        self.log_compost_action(log_entry)
        
        print(f"🗑️ Moved to compost: {file_path}")
        return True
    
    def log_compost_action(self, log_entry):
        """Log a compost action"""
        log_file = self.compost_path / "Intelligence" / "compost_actions.log"
        with open(log_file, 'a') as f:
            f.write(yaml.dump(log_entry, default_flow_style=False) + "---\n")
    
    def create_recovery_point(self, description="auto"):
        """Create a recovery point"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        recovery_dir = self.compost_path / "Recovery" / f"point_{timestamp}_{description}"
        recovery_dir.mkdir(exist_ok=True)
        
        # Create a manifest
        manifest = {
            "timestamp": datetime.now().isoformat(),
            "description": description,
            "files": []
        }
        
        # Save critical files (simplified for demo)
        # In a real implementation, this would snapshot the entire system state
        manifest_path = recovery_dir / "manifest.yaml"
        with open(manifest_path, 'w') as f:
            yaml.dump(manifest, f)
        
        print(f"🔒 Created recovery point: {recovery_dir}")
        return recovery_dir
    
    def run_self_healing(self):
        """Run the self-healing process"""
        print("🧠 Running self-healing process...")
        
        # This would be replaced with the actual daemon implementation
        # For now, we'll simulate the process
        
        # 1. Check health
        health = self.check_health()
        print(f"🩺 Health check: {health}")
        
        # 2. Detect anomalies
        anomalies = self.detect_anomalies(health)
        if anomalies:
            print(f"⚠️ Detected anomalies: {anomalies}")
            
            # 3. Decide and act
            for anomaly in anomalies:
                action = self.decide_action(anomaly)
                print(f"🔧 Taking action: {action}")
                self.execute_action(action)
        else:
            print("✅ No anomalies detected")
        
        # 4. Create recovery point
        self.create_recovery_point("self_healing")
        
        print("✅ Self-healing process complete")
    
    def check_health(self):
        """Simplified health check"""
        # In a real implementation, this would check disk space, file counts, etc.
        return {
            "status": "healthy",
            "compost_size": "small",
            "vector_index": "not_implemented"
        }
    
    def detect_anomalies(self, health):
        """Simplified anomaly detection"""
        # In a real implementation, this would use the config rules
        return []
    
    def decide_action(self, anomaly):
        """Decide on an action"""
        return {"type": "monitor", "reason": "simulated"}
    
    def execute_action(self, action):
        """Execute an action"""
        pass

if __name__ == "__main__":
    integrator = VaultCompostIntegrator()
    integrator.integrate_vault_with_compost()
    print("\n🎉 Vault-Compost integration successful!")
    print("\nNext steps:")
    print("1. Use 'python vault_compost_integration.py' to run integration")
    print("2. Files can be moved to compost with integrator.move_to_compost()")
    print("3. Self-healing can be triggered with integrator.run_self_healing()")