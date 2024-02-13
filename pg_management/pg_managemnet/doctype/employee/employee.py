# Copyright (c) 2024, Ramya Santhosh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Employee(Document):
    def before_insert(self):
        if not frappe.db.exists("User",self.email_id):
            user_doc = frappe.new_doc("User")
            user_doc.email = self.email_id
            user_doc.first_name = self.full_name
            user_doc.phone = self.contact_no
            user_doc.send_welcome_email = 0
            user_doc.flags.ignore_mandatory = True
            user_doc.flags.ignore_permissions = True
            # user_doc.save()
            user_doc.add_roles("PG Employee", "Translator")
            user_prof = frappe.get_doc("User",self.email_id)
            user_prof.new_password = "test"
            modules = [{"module": "Core"},{"module": "Email"},{"module": "Desk"},{"module": "Contacts"},{"module": "Event Streaming"},{"module": "Website"},{"module": "Custom"},{"module": "Integrations"},{"module": "Social"},{"module": "Workflow"},{"module": "Geo"},{"module": "Printing"},{"module": "Automation"}]
            for row in modules:
                user_prof.append("block_modules",
                        {"module": row.get('module')}
                    )
            user_prof.flags.ignore_password_policy = True
            user_prof.save(ignore_permissions = True)
            # frappe.db.commit()
            self.create_user_permission()
            self.append_user_in_worklog_ass_rule()


    def create_user_permission(self):
        if not frappe.db.exists("User Permission",{"allow":"Employee","user":self.email_id,"for_value": self.name}):
            user_perm = frappe.new_doc("User Permission")
            user_perm.user = self.email_id
            user_perm.allow = self.doctype
            user_perm.for_value = self.name
            user_perm.flags.ignore_mandatory = True
            user_perm.save(ignore_permissions = True)

    def append_user_in_worklog_ass_rule(self):
        wl_ass_rule = frappe.get_doc("Assignment Rule", {"document_type": "Work Log"})
        wl_ass_rule.append("users",{
            "user": self.email_id
        })
        wl_ass_rule.save(ignore_permissions=True)
