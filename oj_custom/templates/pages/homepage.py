from __future__ import unicode_literals
import frappe
from erpnext.templates.pages.home import get_context as _get_context


def get_context(context):
    _get_context(context)
    context.explore_link = context.homepage.products_url
