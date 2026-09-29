import json
from pathlib import Path

DATA_FILE = Path("assets.json")

ASSET_TYPES = ["Workstation", "Server", "Router", "Switch", "Application"]
RISK_LEVELS = ["Low", "Medium", "High", "Critical"]
SECURITY_STATUSES = ["Secure", "Warning", "Vulnerable"]


def load_assets():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_assets(assets):
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(assets, f, indent=4)


def choose_option(prompt, options):
    while True:
        print(f"\n{prompt}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        choice = input("Enter choice: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print("Invalid choice. Please try again.")


def get_asset_details(existing=None):
    existing = existing or {}

    def get_text(label, old=""):
        while True:
            value = input(f"{label}{f' [{old}]' if old else ''}: ").strip()
            if value:
                return value
            if old:
                return old
            print("This field cannot be empty.")

    asset = {
        "asset_id": get_text("Asset ID", existing.get("asset_id", "")),
        "asset_name": get_text("Asset Name", existing.get("asset_name", "")),
        "asset_type": choose_option("Asset Type", ASSET_TYPES),
        "ip_address": get_text("IP Address", existing.get("ip_address", "")),
        "operating_system": get_text("Operating System", existing.get("operating_system", "")),
        "department": get_text("Owner/Department", existing.get("department", "")),
        "risk_level": choose_option("Risk Level", RISK_LEVELS),
        "security_status": choose_option("Security Status", SECURITY_STATUSES),
    }
    return asset


def display_asset(asset):
    print("-" * 55)
    print(f"Asset ID       : {asset['asset_id']}")
    print(f"Asset Name     : {asset['asset_name']}")
    print(f"Asset Type     : {asset['asset_type']}")
    print(f"IP Address     : {asset['ip_address']}")
    print(f"OS             : {asset['operating_system']}")
    print(f"Department     : {asset['department']}")
    print(f"Risk Level     : {asset['risk_level']}")
    print(f"Status         : {asset['security_status']}")


def display_all(assets):
    print("\n" + "=" * 55)
    print("           CYBERSECURITY ASSET INVENTORY")
    print("=" * 55)

    if not assets:
        print("No assets found.")
        return

    for asset in assets:
        display_asset(asset)

    print("-" * 55)
    print(f"Total Assets      : {len(assets)}")
    print(f"Critical Assets   : {sum(a['risk_level'] == 'Critical' for a in assets)}")
    print(f"High Risk Assets  : {sum(a['risk_level'] == 'High' for a in assets)}")
    print(f"Medium Risk Assets: {sum(a['risk_level'] == 'Medium' for a in assets)}")
    print(f"Vulnerable Assets : {sum(a['security_status'] == 'Vulnerable' for a in assets)}")
    print("=" * 55)


def add_asset(assets):
    print("\n--- ADD ASSET ---")
    asset_id = input("Asset ID: ").strip()
    if any(a["asset_id"].lower() == asset_id.lower() for a in assets):
        print("Asset ID already exists.")
        return

    asset = get_asset_details({"asset_id": asset_id})
    assets.append(asset)
    save_assets(assets)
    print("Asset added successfully.")


def search_assets(assets):
    keyword = input("\nEnter Asset ID, name, type, IP, or department: ").strip().lower()
    results = [
        a for a in assets
        if any(keyword in str(a[field]).lower() for field in
               ["asset_id", "asset_name", "asset_type", "ip_address", "department"])
    ]

    if not results:
        print("No matching assets found.")
        return

    print(f"\nFound {len(results)} asset(s):")
    for asset in results:
        display_asset(asset)


def update_asset(assets):
    asset_id = input("\nEnter Asset ID to update: ").strip()
    index = next((i for i, a in enumerate(assets)
                  if a["asset_id"].lower() == asset_id.lower()), None)

    if index is None:
        print("Asset not found.")
        return

    print("Enter new values. Existing values are shown in brackets.")
    updated = get_asset_details(assets[index])
    updated["asset_id"] = assets[index]["asset_id"]
    assets[index] = updated
    save_assets(assets)
    print("Asset updated successfully.")


def delete_asset(assets):
    asset_id = input("\nEnter Asset ID to delete: ").strip()
    index = next((i for i, a in enumerate(assets)
                  if a["asset_id"].lower() == asset_id.lower()), None)

    if index is None:
        print("Asset not found.")
        return

    removed = assets.pop(index)
    save_assets(assets)
    print(f"Asset {removed['asset_id']} deleted successfully.")


def main():
    assets = load_assets()

    while True:
        print("\n" + "=" * 55)
        print("      CYBERSECURITY ASSET INVENTORY SYSTEM")
        print("=" * 55)
        print("1. Add Asset")
        print("2. Search Asset")
        print("3. Update Asset")
        print("4. Delete Asset")
        print("5. Display All Assets")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_asset(assets)
        elif choice == "2":
            search_assets(assets)
        elif choice == "3":
            update_asset(assets)
        elif choice == "4":
            delete_asset(assets)
        elif choice == "5":
            display_all(assets)
        elif choice == "6":
            print("Thank you for using the Cybersecurity Asset Inventory System.")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
