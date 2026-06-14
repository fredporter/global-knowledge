# Device Library

> **uDos SonicScrewdriver - Global Device Database**
> Shared catalogue of supported devices and drivers for the uDos ecosystem

---

## Overview

The Device Library is a shared, version-controlled database that all uDos components can access for:
- Device identification and capabilities
- Driver tracking and management
- Recovery procedures
- Reflash/firmware update methods
- Compatibility information

### Location
```
~/Vault/device-library/
```

### Structure
```
Vault/device-library/
├── catalogue.yaml      # Main device database
├── drivers.yaml        # Driver and firmware database
├── custom/             # User-added devices
│   └── *.yaml          # Custom device definitions
└── README.md           # This file
```

---

## Files

### `catalogue.yaml`
**Purpose:** Master list of all known/supported devices

**Schema:**
- `version`: Schema version (currently 1.0)
- `schema`: JSON schema URL
- `updated_at`: Last update timestamp (ISO 8601)
- `total_devices`: Count of devices
- `devices`: Map of device entries

**Device Entry Fields:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | ✅ | Unique identifier (lowercase, hyphen-separated) |
| `name` | string | ✅ | Human-readable name |
| `manufacturer` | string | ✅ | Manufacturer name |
| `type` | enum | ✅ | Device type: `sbc`, `ai_computer`, `laptop`, `desktop`, `server`, `other` |
| `category` | enum | ✅ | Classification: `fit_for_purpose`, `experimental`, `legacy`, `unsupported` |
| `description` | string | ✅ | Brief description |
| `capabilities` | list<string> | ✅ | List of capabilities (see below) |
| `firmware_version` | string | ❌ | Current firmware version |
| `last_updated` | string | ❌ | Last update date (YYYY-MM-DD) |
| `tags` | list<string> | ❌ | Search tags |
| `specifications` | map | ❌ | Hardware specifications |
| `reflash_methods` | list<map> | ❌ | Supported reflash methods |
| `boot_modes` | list<string> | ❌ | Supported boot modes |
| `connections` | list<map> | ❌ | Physical connections/ports |
| `known_good_os` | list<string> | ❌ | Tested/working operating systems |
| `recovery` | map | ❌ | Recovery options |

**Device Types:**
- `sbc` - Single Board Computer (Raspberry Pi, Orange Pi, etc.)
- `ai_computer` - AI/ML specialized computers (Jetson, etc.)
- `laptop` - Laptop computers
- `desktop` - Desktop computers
- `server` - Server hardware
- `other` - Other devices

**Categories:**
- `fit_for_purpose` - Production-ready, fully supported
- `experimental` - New/untested, may have unexpected behavior
- `legacy` - Older devices, maintained but not recommended for new deployments
- `unsupported` - Known devices that are not officially supported

**Capabilities:**
```yaml
# Boot & Storage
reflashable: Can have firmware/OS rewritten
bootable: Can boot from external media
network_boot: Supports PXE/iPXE network boot
usb_boot: Supports USB boot
storage: Has persistent storage

# Compute
compute: Can run applications/OS
headless: No display output (SSH/serial only)

# Graphics & Display
gpu: Has dedicated GPU
touchscreen: Has touch input

# Audio/Video
audio: Audio input/output
camera: Has camera interface

# Networking
wifi: Wireless networking
bluetooth: Bluetooth connectivity
ethernet: Wired networking

# Interfaces
serial: Serial/UART interface
jtag: JTAG debugging interface
spi: SPI interface
i2c: I2C interface
pcie: PCIe interface

# Special
vault: Can store uDos vault data
recovery: Has recovery mode/partition
```

### `drivers.yaml`
**Purpose:** Database of device drivers, firmware, and tools

**Schema:**
- `version`: Schema version (currently 1.0)
- `schema`: JSON schema URL
- `updated_at`: Last update timestamp (ISO 8601)
- `total_drivers`: Count of drivers
- `drivers`: Map of driver entries

**Driver Entry Fields:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | ✅ | Unique identifier |
| `name` | string | ✅ | Human-readable name |
| `description` | string | ✅ | Brief description |
| `platform` | enum | ✅ | Platform: `linux`, `windows`, `macos`, `firmware`, `bootloader`, `tool` |
| `source_type` | enum | ✅ | Source: `official`, `community`, `open_source`, `proprietary`, `third_party` |
| `version` | string | ✅ | Version string |
| `manufacturer` | string | ✅ | Manufacturer name |
| `device_ids` | list<string> | ✅ | List of compatible device IDs |
| `source_url` | string | ❌ | Download/source URL |
| `checksum` | string | ❌ | SHA256 checksum |
| `installed` | boolean | ❌ | Whether installed on current system |
| `last_checked` | string | ❌ | Last verification date |
| `status` | enum | ❌ | Status: `current`, `legacy`, `deprecated`, `experimental`, `broken` |
| `license` | string | ❌ | License type |
| `dependencies` | list<string> | ❌ | Required dependencies |
| `notes` | string | ❌ | Additional notes |
| `files` | list<string> | ❌ | Included files |
| `size` | string | ❌ | Download/package size |
| `binaries` | map | ❌ | Platform-specific binaries |

---

## Custom Devices

User-specific devices can be added in two ways:

### Method 1: Add to `catalogue.yaml`
Simply add a new entry under the `devices` key following the schema.

### Method 2: Separate File in `custom/`
Create a new YAML file in the `custom/` directory with the same structure as `catalogue.yaml`:

```yaml
# custom/my-device.yaml
version: 1.0
devices:
  my-device:
    id: my-device
    name: "My Custom Device"
    manufacturer: "My Company"
    type: sbc
    category: experimental
    description: "My custom SBC"
    capabilities:
      - reflashable
      - storage
```

SonicScrewdriver will automatically merge all YAML files in the directory.

---

## Usage

### With SonicScrewdriver CLI

```bash
# List all devices
sonic library list

# Show device details
sonic library show rpi4b

# Search for devices
sonic library list --type sbc --category fit_for_purpose

# Check driver status
sonic drivers list --installed

# Add custom device
sonic library import /path/to/custom-device.yaml
```

### Programmatic Access

```python
from pathlib import Path
import yaml

LIBRARY_PATH = Path.home() / "Vault" / "device-library"

def load_catalogue():
    with open(LIBRARY_PATH / "catalogue.yaml") as f:
        return yaml.safe_load(f)

def load_drivers():
    with open(LIBRARY_PATH / "drivers.yaml") as f:
        return yaml.safe_load(f)

def load_all_devices():
    """Load all devices including custom ones"""
    devices = {}
    
    # Load main catalogue
    catalogue = load_catalogue()
    devices.update(catalogue.get("devices", {}))
    
    # Load custom devices
    custom_dir = LIBRARY_PATH / "custom"
    if custom_dir.exists():
        for custom_file in custom_dir.glob("*.yaml"):
            with open(custom_file) as f:
                custom_data = yaml.safe_load(f)
                if "devices" in custom_data:
                    devices.update(custom_data["devices"])
    
    return devices
```

---

## Updating

### Manual Updates
Edit the YAML files directly and commit changes to the Vault git repository.

### Automated Updates
SonicScrewdriver can check for driver updates:

```bash
# Check for driver updates
sonic drivers check

# Update a specific driver
sonic drivers update rpi-wifi-bt-drivers
```

---

## Version History

| Date | Version | Changes |
|------|---------|---------|
| 2025-01-19 | 1.0 | Initial release with 12 devices and 45 drivers |

---

## Contributing

1. Fork the Vault repository
2. Add your device/driver entry
3. Test with `sonic library validate`
4. Submit a pull request

### Adding a New Device

When adding a new device:
1. Choose a unique `id` (lowercase, hyphen-separated)
2. Fill in all required fields
3. Add appropriate capabilities
4. Include reflash methods if applicable
5. List known good operating systems
6. Document recovery options

### Adding a New Driver

When adding a new driver:
1. Choose a unique `id` (lowercase, hyphen-separated)
2. Specify the platform
3. Link to compatible devices via `device_ids`
4. Include source URL and license
5. Set initial `status` appropriately

---

## License

The Device Library is licensed under **CC-BY-SA-4.0**.

Device and driver information is collected from public sources and manufacturer documentation.

---

## Related Components

- **[SonicScrewdriver](../sonic-screwdriver/)** - Device reflasher and USB tool
- **[api-central](uServer/api-central/)** - API Gateway and container management
- **[uDoUI](uDosGo/Connect/udoui/)** - User interface surfaces

---

## Schema Validation

JSON Schema definitions are available at:
- Device Catalogue: `https://udos.world/schemas/device-catalogue/v1.json`
- Drivers Database: `https://udos.world/schemas/device-drivers/v1.json`

Validate your entries using:
```bash
# Install jsonschema
pip install jsonschema pyyaml

# Validate catalogue.yaml
python -c "
import yaml, json, jsonschema
from jsonschema import validate

with open('catalogue.yaml') as f:
    data = yaml.safe_load(f)

# Load schema from URL or local file
# validate(instance=data, schema=schema)
"
```
