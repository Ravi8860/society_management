# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields,models,tools

class SaleReport(models.Model):
    _inherit = "sale.order"
    _description = "sale report record"


    flat_no_id = fields.Many2one('biz.flats',string='Flat',help="this is Flat Id")
    flattype= fields.Selection([('first','1BHK'),('second','2BHK'),('third','3BHK'),('four','4BHK'),('five','5BHK'),('six','Duplex')],string="FlatType")
    block =fields.Selection([('a','A'),('b', 'B'), ('c','C'),('d', 'D'), ('e','E'), ('f','F'),('g', 'G'),('h','H'),('i', 'I'),('j', 'J'), ('k','K'),('l','L'),('m','M'),('n','N'),('o','O'),('p','P')],string='Block')
