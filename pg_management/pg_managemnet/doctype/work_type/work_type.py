# Copyright (c) 2024, Ramya Santhosh and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class WorkType(Document):
	def autoname(self):
		self.name = self.work_type
