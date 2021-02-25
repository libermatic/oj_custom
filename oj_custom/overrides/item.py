from erpnext.stock.doctype.item.item import Item


class CustomItem(Item):
    website = frappe._dict(
        page_title_field="item_name",
        condition_field="show_in_website",
        template="templates/generators/custom_item.html",
        no_cache=1,
    )
