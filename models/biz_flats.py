# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields,models,tools

class BizFlats(models.Model):

	_name = 'biz.flats'
	_inherit = ['mail.thread.cc','mail.activity.mixin']
	_description ='flats recods'

	name=fields.Char(string='Name',help="this is flat numbers")
	image = fields.Binary(string='Image')
	floor =fields.Char(string='Floor',help="this is floor")
	flattype= fields.Selection([('first','1BHK'),('second','2BHK'),('third','3BHK'),('four','4BHK'),('five','5BHK'),('six','Duplex')],string="FlatType")
	maintenance_charge = fields.Char(string='Maintenance Charge')