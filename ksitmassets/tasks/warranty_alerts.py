import frappe
from frappe.utils import today, getdate

def send_warranty_expiry_alerts():
    """Send warranty expiry alerts 60, 30, and 7 days before expiry"""

    today_date = getdate(today())

    # Fetch all assets with warranty end date set
    assets = frappe.get_all(
        "Asset",
        filters=[["custom_warranty_end_date", "is", "set"]],
        fields=["name", "asset_name", "custom_warranty_end_date"]
    )

    for asset in assets:
        warranty_end = getdate(asset.custom_warranty_end_date)
        days_left = (warranty_end - today_date).days

        # Trigger alerts 60, 30, and 7 days before expiration
        if days_left in (60, 30, 7):
            subject = f"Warranty Expiry Alert: {asset.asset_name}"
            message = f"""
                <p>Dear User,</p>
                <p>The warranty for the asset <b>{asset.asset_name}</b> (<b>{asset.name}</b>) 
                will expire in <b>{days_left} days</b> on <b>{asset.custom_warranty_end_date}</b>.</p>
                <p>Please take the necessary action if renewal or service is required.</p>
            """

            # ---- System Notification (Bell Icon) ----
            for user in ["Administrator", "lakshmir@icfoss.org"]:
                frappe.get_doc({
                    "doctype": "Notification Log",
                    "subject": subject,
                    "email_content": message,
                    "for_user": user,
                    "type": "Alert",
                    "document_type": "Asset",
                    "document_name": asset.name,
                }).insert(ignore_permissions=True)

    frappe.db.commit()
