# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api,fields,models,tools

class InvoicesReport(models.Model):
    _inherit = "account.move"
    _description = "invoices report record"
    
    flat_no_id = fields.Many2one('biz.flats',string='Flat',help="this is Flat Id")
