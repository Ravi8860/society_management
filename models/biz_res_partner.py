# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields,models,tools

class ResPartnerInherit(models.Model):
    _inherit = "res.partner"
    _description = "partner Record"

    flat_no_id = fields.Many2one('biz.flats',string='Flat',help="this is Flat Id")
    flattype= fields.Selection([('first','1BHK'),('second','2BHK'),('third','3BHK'),('four','4BHK'),('five','5BHK'),('six','Duplex')],string="FlatType")
    block =fields.Selection([('a','A'),('b', 'B'), ('c','C'),('d', 'D'), ('e','E'), ('f','F'),('g', 'G'),('h','H'),('i', 'I'),('j', 'J'), ('k','K'),('l','L'),('m','M'),('n','N'),('o','O'),('p','P')],string='Block')

    @api.onchange('flat_no_id')
    def set_flattype(self):
        for rec in self:
            if rec.flat_no_id:
                rec.flattype = rec.flat_no_id.flattype