# Copyright (c) 2024, Ramya Santhosh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class WorkLog(Document):
	def on_update(self):
		if self.status == "Assigned":
			emp = frappe.db.get_value("Employee", {"email_id": frappe.session.user}, ["name", "full_name"], as_dict=1)
			self.employee = emp.name
			self.employee_name = emp.full_name
			self.save()
