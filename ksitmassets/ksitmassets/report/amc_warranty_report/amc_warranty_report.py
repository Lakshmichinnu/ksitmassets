import frappe
from frappe.utils import add_days, today, date_diff, getdate

def execute(filters=None):
    if not filters:
        filters = {}

    days = filters.get("days") or 60
    target_date = getdate(add_days(today(), days))

    columns = get_columns()
    data = get_data(target_date)

    return columns, data


def get_columns():
    return [
        {"label": "Asset", "fieldname": "name", "fieldtype": "Link", "options": "Asset", "width": 140},
        {"label": "Asset Name", "fieldname": "asset_name", "fieldtype": "Data", "width": 160},

        {"label": "Warranty End", "fieldname": "warranty_end", "fieldtype": "Date", "width": 120},
        {"label": "Warranty Days Left", "fieldname": "warranty_days_left", "fieldtype": "Int", "width": 160},

        {"label": "AMC End", "fieldname": "amc_end", "fieldtype": "Date", "width": 120},
        {"label": "AMC Days Left", "fieldname": "amc_days_left", "fieldtype": "Int", "width": 160},

        {"label": "Nearest Expiry Date", "fieldname": "expiry_date", "fieldtype": "Date", "width": 150},
        {"label": "Expiry Type", "fieldname": "expiry_type", "fieldtype": "Data", "width": 120},
    ]


def get_data(target_date):
    assets = frappe.db.get_all(
        "Asset",
        fields=[
            "name",
            "asset_name",
            "custom_warranty_end_date",
            "custom_amc_end_dtae",
        ]
    )

    result = []

    for a in assets:
        # Extract dates
        warranty_end = getdate(a.custom_warranty_end_date) if a.custom_warranty_end_date else None
        amc_end = getdate(a.custom_amc_end_dtae) if a.custom_amc_end_dtae else None

        # Must have both dates
        if not (warranty_end and amc_end):
            continue

        # Calculate days left
        warranty_days_left = date_diff(warranty_end, today())
        amc_days_left = date_diff(amc_end, today())

        # Both must be within 0–60 days
        if not (0 <= warranty_days_left <= 60 and 0 <= amc_days_left <= 60):
            continue

        # Determine nearest expiry
        if warranty_end < amc_end:
            expiry_type = "Warranty"
            expiry_date = warranty_end
        else:
            expiry_type = "AMC"
            expiry_date = amc_end

        result.append({
            "name": a.name,
            "asset_name": a.asset_name,

            "warranty_end": warranty_end,
            "warranty_days_left": warranty_days_left,

            "amc_end": amc_end,
            "amc_days_left": amc_days_left,

            "expiry_type": expiry_type,
            "expiry_date": expiry_date,
        })

    return result
