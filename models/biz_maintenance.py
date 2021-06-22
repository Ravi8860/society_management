# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields,models,tools

class BizMaintenance(models.Model):

	_name = 'biz.maintenance'
	_inherit = ['mail.thread.cc','mail.activity.mixin']
	_description ='store maintenance bill recod'

	name = fields.Char(string='Name')
	flats_id = fields.Many2one('flats',string='Flats No')
	phone = fields.Char(string='Phone No')
	address = fields.Text(string='Address')
	water_charges= fields.Integer(string='Water Charges')
	elec_charges=fields.Char(string='Elec Charges')
	property_tax =fields.Char(string="Property Tax")
	parking_charges = fields.Char(string='Parking Charges')
	due_date=fields.Date(string='Due Date')
