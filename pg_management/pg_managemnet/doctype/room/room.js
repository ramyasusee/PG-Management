// Copyright (c) 2024, Ramya Santhosh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Room", {
    refresh: function(frm) {
		frm.fields_dict['currently_staying_customers'].grid.wrapper.find('.grid-add-row').hide();
		frm.fields_dict['currently_staying_customers'].grid.wrapper.find('.grid-remove-rows').hide();
    },
	currently_staying_customers_on_form_rendered: function(frm,cdt,cdn){
		frm.fields_dict['currently_staying_customers'].grid.wrapper.find('.grid-delete-row').hide();
		frm.fields_dict['currently_staying_customers'].grid.wrapper.find('.grid-duplicate-row').hide();
		frm.fields_dict['currently_staying_customers'].grid.wrapper.find('.grid-move-row').hide();
		frm.fields_dict['currently_staying_customers'].grid.wrapper.find('.grid-append-row').hide();
		frm.fields_dict['currently_staying_customers'].grid.wrapper.find('.grid-insert-row-below').hide();
		frm.fields_dict['currently_staying_customers'].grid.wrapper.find('.grid-insert-row').hide();
	},
});
