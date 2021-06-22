# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields,models,tools

class BizVisitor(models.Model):

	_name = 'biz.visitor'
	_inherit = ['mail.thread.cc','mail.activity.mixin']
	_description ='visitor recods'

	visitor_name = fields.Char(string='Visitor Name',help='this is visitor')
	image = fields.Binary(string='Image')
	phone_no = fields.Char(string='Phone Number',help='this is phone numbers')
	address = fields.Text(string='Address',help='this is address')
	block =fields.Selection([('a','A'),('b', 'B'), ('c','C'),('d', 'D'), ('e','E'), ('f','F'),('g', 'G'),('h','H'),('i', 'I'),('j', 'J'), ('k','K'),('l','L'),('m','M'),('n','N'),('o','O'),('p','P')],string='Block')
	flat_numbers=fields.Selection([('a',101),('b',102),('c',103),('d',104),('e',105),('f',106),('g',107),('h',201)],string='Flat Number')
	whom_to_meet = fields.Char(string='Whom to Meet',help='this is whom to meet')
	reason_to_meet = fields.Char(string='Reason to meet')