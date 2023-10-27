import frappe

def create_default_buying_price(doc, method):
    if doc.default_buying_price:
        # Erstelle einen neuen Artikelpreis-Datensatz
        item_price = frappe.new_doc("Item Price")
        item_price.price_list = "Standard-Kauf"
        item_price.item_code = doc.name
        item_price.price_list_rate = doc.default_buying_price
        item_price.insert()