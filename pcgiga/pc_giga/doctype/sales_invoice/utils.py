import frappe

@frappe.whitelist()
def get_unique_timesheets(doc):
    """Returns a list of unique timesheet ids from a sales invoice.

    Args:
        doc (frappe.model.document.Document): The sales invoice document.

    Returns:
        list: A list of unique timesheets.
    """
    unique_ids = set()
    unique_timesheets = []
    for ts in doc.timesheets:
        if ts.time_sheet not in unique_ids:
            unique_ids.add(ts.time_sheet)
            unique_timesheets.append(ts)
    return unique_timesheets
