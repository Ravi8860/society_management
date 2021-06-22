# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields,models,tools

class BizComplain(models.Model):
    _name = "biz.complain"
    _inherit = ['mail.thread.cc','mail.activity.mixin']
    _description = "complain Record"

    name = fields.Char(string='name')
    image = fields.Binary(string='Image')
    complain_type = fields.Selection([('a','Electrical Problem'),('b','Fire'),('c','Common Area'),('d','Lift'),('e','Parking'),('f','Events'),('g','Other')],string='Complain Type')
    complain_Description = fields.Text(string='Complain Description')