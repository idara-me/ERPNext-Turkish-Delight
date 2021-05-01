# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe

__version__ = '1.210201.2'

def console(*data):
	frappe.publish_realtime('out_to_console', data, user=frappe.session.user)
