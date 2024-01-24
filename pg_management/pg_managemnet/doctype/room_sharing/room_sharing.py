# Copyright (c) 2024, Ramya Santhosh and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RoomSharing(Document):
	def autoname(self):
		self.name = self.sharing_name
