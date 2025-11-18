// Copyright (c) 2025, lakshmir and contributors
// For license information, please see license.txt


frappe.query_reports["AMC_Warranty_report"] = {
    formatter: function (value, row, column, data, default_formatter) {
        value = default_formatter(value, row, column, data);

        if (!data) return value;

        // Warranty Days Left
        if (column.fieldname === "warranty_days_left" && data.warranty_days_left !== null) {
            const days = data.warranty_days_left;
            let color = "green";

            if (days < 0) color = "red";
            else if (days <= 15) color = "orange";
            else if (days <= 30) color = "gold";

            return `<span style="color:${color}; font-weight:bold;">${value}</span>`;
        }

        // AMC Days Left
        if (column.fieldname === "amc_days_left" && data.amc_days_left !== null) {
            const days = data.amc_days_left;
            let color = "green";

            if (days < 0) color = "red";
            else if (days <= 15) color = "orange";
            else if (days <= 30) color = "gold";

            return `<span style="color:${color}; font-weight:bold;">${value}</span>`;
        }

        // Expiry Type
        if (column.fieldname === "expiry_type") {
            if (value === "Warranty") {
                return `<span style="color:blue; font-weight:bold;">${value}</span>`;
            }
            if (value === "AMC") {
                return `<span style="color:purple; font-weight:bold;">${value}</span>`;
            }
        }

        return value;
    }
};
