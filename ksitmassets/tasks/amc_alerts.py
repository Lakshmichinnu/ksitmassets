
# ksitmassets/tasks/amc_alerts.py
import frappe
from frappe.utils import today, getdate

RECIPIENTS = ["lakshmir@icfoss.org"]  # add more user emails if needed

def send_amc_expiry_alerts():
    """Create Notification Log entries when AMC is 30 or 7 days from expiry."""
    today_date = getdate(today())

    assets = frappe.get_all(
        "Asset",
        filters={
            "maintenance_required": 1,
        },
        fields=["name", "asset_name", "custom_amc_end_dtae"]
    )

    for asset in assets:
        if not asset.custom_amc_end_dtae:
            continue

        amc_end = getdate(asset.custom_amc_end_dtae)
        days_left = (amc_end - today_date).days

        if days_left in (30, 7):
            subject = f"AMC Expiry Alert: {asset.asset_name} ({days_left} days left)"
            message = (
                f"The AMC for <b>{asset.asset_name}</b> (<b>{asset.name}</b>) "
                f"expires in <b>{days_left} days</b> on <b>{asset.custom_amc_end_dtae}</b>."
            )

            for user_email in RECIPIENTS:
                # Create a Notification Log (shows under the bell icon)
                nl = frappe.get_doc({
                    "doctype": "Notification Log",
                    "subject": subject,
                    "for_user": user_email,            # must be a System User's email
                    "type": "Alert",
                    "document_type": "Asset",
                    "document_name": asset.name,
                    "email_content": message,
                })
                nl.insert(ignore_permissions=True)
