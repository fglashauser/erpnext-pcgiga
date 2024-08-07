import frappe

def on_submit(doc, method):
    """
    Close Sales Order when Sales Invoice is submitted and the option "Nach Rechnung schließen" is checked
    """
    if doc.docstatus == 1:
        sales_orders = doc.items
        for item in sales_orders:
            if item.sales_order:
                sales_order = frappe.get_doc("Sales Order", item.sales_order)
                if sales_order.status != 'Closed' and sales_order.autoclose_after_invoice == 1:
                    sales_order.update_status('Closed')
                    sales_order.save()
                    print('Sales Order {0} has been closed'.format(sales_order.name))