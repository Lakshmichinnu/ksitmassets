import frappe
from frappe.model.document import Document

class AssetReturn(Document):
    pass


@frappe.whitelist()
def get_issued_assets(employee_id):
    """Return all assets issued to a specific employee from Asset Movement."""
    issued_assets = []

    # Get all submitted Asset Movements with purpose 'Issue'
    movements = frappe.get_all(
        "Asset Movement",
        filters={"docstatus": 1, "purpose": "Issue"},
        fields=["name"]
    )

    # Loop through child table to find assets linked to that employee
    for m in movements:
        child_assets = frappe.get_all(
            "Asset Movement Item",
            filters={"parent": m.name, "to_employee": employee_id},
            fields=["asset", "asset_name"]
        )
        for a in child_assets:
            issued_assets.append({
                "asset_id": a.asset,
                "asset_name": a.asset_name
            })

    return issued_assets
