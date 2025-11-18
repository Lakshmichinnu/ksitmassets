# ksitm_assets/doctype/asset_movement/asset_movement.py






import frappe
from frappe import _
from frappe.model.document import Document

def validate_asset_movement(doc, method):
    """
    Validate asset movement workflow:
    Ensure assets can only be issued to a new employee
    after being received from the current employee
    """
    purpose = (doc.purpose or "").lower().strip()
    
    # Validate for Issue and Transfer and Issue purposes
    if purpose in ["issue", "transfer and issue"]:
        validate_issue_to_employee(doc)
    
    # Validate Receipt
    elif purpose == "receipt":
        validate_receipt_from_employee(doc)


def after_submit_asset_movement(doc, method):
    """
    After Receipt is submitted, clear the custodian from Asset
    so it can be issued to a new employee
    """
    purpose = (doc.purpose or "").lower().strip()
    
    # Clear custodian after Receipt
    if purpose == "receipt":
        clear_asset_custodian_on_receipt(doc)


def clear_asset_custodian_on_receipt(doc):
    """Clear custodian from all assets when receipt is posted"""
    for row in doc.assets or []:
        asset_doc = frappe.get_doc("Asset", row.asset)
        asset_doc.custodian = None  # Clear the custodian
        asset_doc.save()
        frappe.db.commit()


def validate_issue_to_employee(doc):
    """Block issue if asset is with a different employee"""
    blocked_assets = []
    msg_lines = []
    
    for row in doc.assets or []:
        to_employee = row.to_employee
        
        if not to_employee:
            continue
        
        # Get current asset state
        asset_state = frappe.db.get_value(
            "Asset",
            row.asset,
            ["custodian", "location"],
            as_dict=True
        )
        
        if not asset_state:
            continue
        
        current_custodian = (asset_state.custodian or "").strip() if asset_state.custodian else ""
        
        # Block if asset is with a different employee
        if current_custodian and current_custodian != to_employee:
            blocked_assets.append(row.asset)
            msg_lines.append(
                f"- Asset {row.asset_name}: currently with {current_custodian}, cannot issue to {to_employee} without Receipt first"
            )
    
    if blocked_assets:
        detail = "\n".join(msg_lines)
        frappe.throw(
            _("Cannot issue. Asset must be taken back (Receipt) from current employee first:\n{0}").format(detail)
        )


def validate_receipt_from_employee(doc):
    """Validate receipt matches current custodian"""
    mismatched_assets = []
    msg_lines = []
    
    for row in doc.assets or []:
        from_employee = row.from_employee
        
        if not from_employee:
            continue
        
        # Get current asset state
        asset_state = frappe.db.get_value(
            "Asset",
            row.asset,
            ["custodian", "location"],
            as_dict=True
        )
        
        if not asset_state:
            continue
        
        current_custodian = (asset_state.custodian or "").strip() if asset_state.custodian else ""
        
        # Check if receiving from different employee than recorded
        if current_custodian and current_custodian != from_employee:
            mismatched_assets.append(row.asset)
            msg_lines.append(
                f"- Asset {row.asset_name}: expected from {from_employee}, but currently with {current_custodian}"
            )
    
    if mismatched_assets:
        detail = "\n".join(msg_lines)
        frappe.throw(
            _("Receipt mismatch. Asset custodian does not match expected source:\n{0}").format(detail)
        )
