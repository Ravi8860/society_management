# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api,fields,models,tools

class Invoices(models.Model):
    _inherit = "account.move"
    _description = "account record"


    flat_no_id = fields.Many2one('biz.flats',string='Flat',help="this is Flat Id")
    flattype= fields.Selection([('first','1BHK'),('second','2BHK'),('third','3BHK'),('four','4BHK'),('five','5BHK'),('six','Duplex')],string="FlatType")


    @api.onchange('partner_id')
    def set_flat_no_id(self):
        for rec in self:
            if rec.partner_id:
                rec.flat_no_id = rec.partner_id.flat_no_id

    @api.onchange('partner_id')
    def set_flattype(self):
    	for rec in self:
    		if rec.partner_id:
    			rec.flattype = rec.partner_id.flattype