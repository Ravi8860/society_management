# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields
class AllotmentRecord(models.Model):
    _name = "biz.allotment"
    _inherit = ['mail.thread.cc','mail.activity.mixin']
    _description = "Allotment Record"
    
    name = fields.Char(string='Name')
    image=fields.Binary(string='Image')
    contact_no = fields.Char(string='Contact No',)
    flat_numbers=fields.Selection([('a',101),('b',102),('c',103),('d',104),('e',105),('f',106),('g',107),('h',201)],string='Flat Number')
    flattype= fields.Selection([('first','1BHK'),('second','2BHK'),('third','3BHK'),('four','4BHK'),('five','5BHK'),('six','Duplex')],string="FlatType")
    total_member = fields.Char(string='Total Member of Family')
    permanent_address = fields.Text(string='Permanent Address')
    allotment_date = fields.Date(string='Allotment Date')