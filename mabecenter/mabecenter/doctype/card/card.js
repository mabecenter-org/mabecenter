// Copyright (c) 2024, Dante Devenir and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Card", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Card', {
    refresh: function(frm) {
        // Si el documento ya ha sido guardado (no es nuevo), hacer que card_name sea read-only
        if (!frm.is_new()) {
            frm.set_df_property('card_number', 'read_only', 1);
        }
    }
});
