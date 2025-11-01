app_name = "ksitmassets"
app_title = "ksitmassets"
app_publisher = "lakshmir"
app_description = "assets customizations"
app_email = "lakshmir@icfoss.org"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "ksitmassets",
# 		"logo": "/assets/ksitmassets/logo.png",
# 		"title": "ksitmassets",
# 		"route": "/ksitmassets",
# 		"has_permission": "ksitmassets.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ksitmassets/css/ksitmassets.css"
# app_include_js = "/assets/ksitmassets/js/ksitmassets.js"

# include js, css files in header of web template
# web_include_css = "/assets/ksitmassets/css/ksitmassets.css"
# web_include_js = "/assets/ksitmassets/js/ksitmassets.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ksitmassets/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "ksitmassets/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "ksitmassets.utils.jinja_methods",
# 	"filters": "ksitmassets.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ksitmassets.install.before_install"
# after_install = "ksitmassets.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ksitmassets.uninstall.before_uninstall"
# after_uninstall = "ksitmassets.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "ksitmassets.utils.before_app_install"
# after_app_install = "ksitmassets.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "ksitmassets.utils.before_app_uninstall"
# after_app_uninstall = "ksitmassets.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ksitmassets.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ksitmassets.tasks.all"
# 	],
# 	"daily": [
# 		"ksitmassets.tasks.daily"
# 	],
# 	"hourly": [
# 		"ksitmassets.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ksitmassets.tasks.weekly"
# 	],
# 	"monthly": [
# 		"ksitmassets.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "ksitmassets.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ksitmassets.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ksitmassets.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ksitmassets.utils.before_request"]
# after_request = ["ksitmassets.utils.after_request"]

# Job Events
# ----------
# before_job = ["ksitmassets.utils.before_job"]
# after_job = ["ksitmassets.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"ksitmassets.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

fixtures = [
    {
        "dt": "Custom Field",
        "filters": [
            ["name", "in", [
                "Asset-custom_serial_number",
                "Item-custom_serial_number",
                "Asset-custom_warranty_end_date",
                "Asset-custom_warranty_start_date",
                "Item-custom_makemodel",
                "Asset-custom_delivery_note",
                "Asset-custom_invoice_",
                "Asset-custom_warranty",
                "Asset-custom_warranty_certificate",
                "Asset-custom_condition",
                "Asset-custom_amc_start_date",
                "Purchase Receipt-custom_date_of_purchase",
                "Asset-custom_amc_end_dtae"
                "Item-custom_makemodel",
                "Item-custom_serial_number"
            ]]
        ]
    }
]
# fixtures for the workflow


fixtures = [
  {"doctype": "Workflow", "filters": [["name", "in", ["Asset Issue "]]]}
]
# fixtures for the client script

fixtures = [
    {
        "doctype": "Client Script",
        "filters": [
            ["name", "in", ["Asset Issue Requests"]]
        ]
    }
]
