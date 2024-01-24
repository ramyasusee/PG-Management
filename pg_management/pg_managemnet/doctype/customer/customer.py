# Copyright (c) 2024, Ramya Santhosh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Customer(Document):
	def validate(self):
		# room availability check
		if frappe.db.get_value("Room", self.room, "is_available") == False and self.status == "Currently Staying":
			frappe.throw("There is no vacancy in the selected room")

	def after_insert(self):
		if self.status == "Currently Staying" and not frappe.db.exists("Room Currently Staying Customer", {"parent": self.room, "customer": self.name}):
			room_doc = frappe.get_doc("Room", self.room)
			room_doc.append("currently_staying_customers",{
                        "customer": self.name,
                        "customer_name": self.full_name,
                        "mob_no": self.mob_no,
                        "emergency_contact": self.emergency_contact
                    })
			
			# mark room availabilty
			if room_doc.max_no_of_members == len(room_doc.currently_staying_customers):
				room_doc.is_available = 0
			room_doc.save(ignore_permissions=True)
			

	def on_submit(self):
			frappe.db.sql("DELETE from `tabRoom Currently Staying Customer` where parent = '{0}' AND customer='{1}'".format(self.room, self.name))
			frappe.db.set_value("Room", self.room, "is_available", 1)
