# Cybersecurity Asset Inventory System

## Week 1 Mini Project

A simple Python-based **Cybersecurity Asset Inventory System** for managing an organization's IT assets.

The project is based on the Week 1 mini-project requirements: an administrator can add, search, update, delete, and display IT assets, while each asset is classified by asset type, risk level, and security status.

## Features

- Add a new IT asset
- Search assets by:
  - Asset ID
  - Asset name
  - Asset type
  - IP address
  - Department
- Update asset information
- Delete an asset
- Display all assets
- Classify assets by:
  - Workstation
  - Server
  - Router
  - Switch
  - Application
- Risk levels:
  - Low
  - Medium
  - High
  - Critical
- Security status:
  - Secure
  - Warning
  - Vulnerable
- Automatic summary:
  - Total assets
  - Critical assets
  - High-risk assets
  - Medium-risk assets
  - Vulnerable assets
- JSON file storage so data remains available after the program closes

## Asset Information

Each asset contains:

| Field | Description |
|---|---|
| Asset ID | Unique identifier |
| Asset Name | Name of the asset |
| Asset Type | Type of IT asset |
| IP Address | Network address |
| Operating System | OS used by the asset |
| Owner/Department | Responsible department |
| Risk Level | Low/Medium/High/Critical |
| Security Status | Secure/Warning/Vulnerable |

## Requirements

- Python 3.8 or newer
- No external Python packages are required

## How to Run

1. Install Python.
2. Clone this repository:

```bash
git clone https://github.com/YOUR-USERNAME/cybersecurity-asset-inventory.git
cd cybersecurity-asset-inventory
```

3. Run:

```bash
python main.py
```

The program automatically creates `assets.json` when an asset is added.

## Sample Data

The project specification provides examples such as:

- A101 - HR-PC-01 - Workstation - Medium - Secure
- A102 - Web-Server - Server - Critical - Vulnerable
- A103 - Core-Router - Router - High - Warning

## Project Structure

```text
cybersecurity-asset-inventory/
├── main.py
├── assets.json
├── README.md
├── .gitignore
└── LICENSE
```

## Learning Outcomes

This project demonstrates:

- Python functions
- Lists and dictionaries
- File handling
- JSON data storage
- CRUD operations
- Input validation
- Searching and filtering
- Basic cybersecurity asset classification

## Future Improvements

- GUI using Tkinter
- SQLite/MySQL database
- Login and role-based access
- IP address validation
- Export to CSV/PDF
- Risk-based dashboard
- Authentication and audit logs

## Author

**Sudar Mani S**

Cybersecurity Student
