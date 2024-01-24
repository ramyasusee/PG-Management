// Copyright (c) 2024, Ramya Santhosh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Customer", {
	refresh(frm) {
        // if(frm.is_new()){
        //     frm.set_value("status", "Currently Staying");
        // }

        frm.set_query("room", function (doc) {
			return {
				filters: {
					"is_available": 1
				}
			};
		});
	},
});
