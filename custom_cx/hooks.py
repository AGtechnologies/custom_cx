# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "custom_cx"
app_title = "CX3 Asia Pte Ltd"
app_publisher = "AG Technologies Pte Ltd"
app_description = "Customisation for CX3 Asia Pte Ltd"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@agtech.com.sg"
app_license = "MIT"

#fixtures = ["Custom Field"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/custom_cx/css/custom_cx.css"
# app_include_js = "/assets/custom_cx/js/custom_cx.js"

# include js, css files in header of web template
# web_include_css = "/assets/custom_cx/css/custom_cx.css"
# web_include_js = "/assets/custom_cx/js/custom_cx.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "custom_cx.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "custom_cx.install.before_install"
# after_install = "custom_cx.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "custom_cx.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"custom_cx.tasks.all"
# 	],
# 	"daily": [
# 		"custom_cx.tasks.daily"
# 	],
# 	"hourly": [
# 		"custom_cx.tasks.hourly"
# 	],
# 	"weekly": [
# 		"custom_cx.tasks.weekly"
# 	]
# 	"monthly": [
# 		"custom_cx.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "custom_cx.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "custom_cx.event.get_events"
# }

