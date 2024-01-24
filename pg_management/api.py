import frappe
from frappe.utils import today


@frappe.whitelist(allow_guest=True)
def get_available_rooms():
    avl_rooms = frappe.db.sql(""" SELECT name,sharing,room_rent 
                                    FROM `tabRoom`
                                    WHERE is_available=1""",as_dict=1)
    return avl_rooms



@frappe.whitelist()
def create_work_log():
    rooms = frappe.db.get_list("Room",fields=["name"])
    for rm in rooms:
        per_works = frappe.get_list("Work type", fields=["name"], filters={"is_periodic_maintenance": 1})
        for pw in per_works:
            wl_doc = frappe.new_doc("Work Log")
            wl_doc.update({
                "work_type": pw.name,
                "date": today(),
                "room": rm.name,
                "status": "Assigned"
            })
            wl_doc.save(ignore_permissions=True)
