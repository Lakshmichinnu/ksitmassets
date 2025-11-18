# Copyright (c) 2025, lakshmir and contributors
# For license information, please see license.txt

# import frappe


import frappe

def execute(filters=None):
    columns = [
        {"label": "Employee", "fieldname": "employee", "fieldtype": "Link", "options": "Employee", "width": 180},
        {"label": "Employee Name", "fieldname": "employee_name", "fieldtype": "Data", "width": 200},
        {"label": "Asset", "fieldname": "asset", "fieldtype": "Link", "options": "Asset", "width": 160},
        {"label": "Asset Name", "fieldname": "asset_name", "fieldtype": "Data", "width": 250},
        {"label": "Issued On", "fieldname": "issue_date", "fieldtype": "Date", "width": 120},
        {"label": "Movement", "fieldname": "movement", "fieldtype": "Link", "options": "Asset Movement", "width": 150},
    ]

    # Fetch all Issue records, but exclude those that were later returned
    data = frappe.db.sql("""
        SELECT
            ami.asset,
            ami.to_employee AS employee,
            emp.employee_name,
            asset.item_name AS asset_name,
            am.transaction_date AS issue_date,
            am.name AS movement
        FROM `tabAsset Movement Item` ami
        JOIN `tabAsset Movement` am ON am.name = ami.parent
        LEFT JOIN `tabEmployee` emp ON emp.name = ami.to_employee
        LEFT JOIN `tabAsset` asset ON asset.name = ami.asset
        WHERE am.docstatus = 1
        AND am.purpose = 'Issue'
        AND ami.to_employee IS NOT NULL
        AND NOT EXISTS (
            SELECT 1
            FROM `tabAsset Movement Item` ami2
            JOIN `tabAsset Movement` am2 ON am2.name = ami2.parent
            WHERE am2.docstatus = 1
            AND am2.purpose = 'Receipt'
            AND ami2.asset = ami.asset
            AND am2.transaction_date > am.transaction_date
        )
        ORDER BY emp.employee_name, am.transaction_date DESC
    """, as_dict=True)

    return columns, data
