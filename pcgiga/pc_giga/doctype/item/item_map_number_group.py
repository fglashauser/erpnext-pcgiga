import frappe

def item_map_number_group(doc, method):
    if doc.item_group:
        root_group = get_root_item_group(doc.item_group)
        naming_series_mapping = {
            "Dienstleistung": "DL-.#####",
            "Hardware": "HW-.#####",
            "PV": "PV-.#####",
            "Software": "SW-.#####",
            "Sonstiges": "ART-.#####"
        }

        if root_group in naming_series_mapping:
            doc.naming_series = naming_series_mapping[root_group]

def get_root_item_group(item_group_name):
    item_group = frappe.get_doc("Item Group", item_group_name)
    if item_group.parent_item_group and item_group.parent_item_group != 'Alle Artikelgruppen':
        return get_root_item_group(item_group.parent_item_group)
    else:
        return item_group_name