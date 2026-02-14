# Info Changer

A Python toolkit for managing and changing MAC addresses on Windows systems.

## Features

- 🔄 **MAC Address Changer**: Change network adapter MAC addresses on Windows
- 🎲 **Random MAC Generator**: Generate random MAC addresses using real vendor OUIs
- 📋 **Network Adapter Viewer**: List all network adapters from Windows registry
- 🖥️ **Simple Console UI**: Easy-to-use menu interface

## Installation

1. Clone the repository:
```bash
cd Mac-Changer
```

2. No additional dependencies required (uses Python standard library)

## Requirements

- Windows OS
- Python 3.x
- Administrator privileges (for MAC address changes)

## Usage

### Main Application (Recommended)
```bash
python main.py
```
Run as administrator for full functionality. Provides an interactive menu with all features.

### Individual Scripts

#### Change MAC Address
```bash
python Mac_Address.py
```
Edit the script to set your adapter name and desired MAC address.

#### Generate Random MAC
```bash
python randommac.py
```
Generates a MAC address using a random vendor OUI from `mac-vendor.txt`.

#### List Network Adapters
```bash
python Mac_OUI.py
```

## Files

- `main.py` - Main application with interactive menu
- `Mac_Address.py` - MAC address changer module
- `randommac.py` - Random MAC generator module
- `Mac_OUI.py` - Network adapter registry viewer
- `mac-vendor.txt` - Database of vendor OUI prefixes

## ⚠️ Important Notes

- **Administrator privileges required** for changing MAC addresses
- Right-click Command Prompt/PowerShell → "Run as administrator"
- Some network adapters may not support MAC address changes
- Changes take effect after adapter restart


## Disclaimer

This tool is for educational and legitimate network administration purposes only. Users are responsible for complying with local laws and regulations.
