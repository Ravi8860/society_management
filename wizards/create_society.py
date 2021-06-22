# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,fields,api

class CreateSociety(models.TransientModel):
	_name = 'create.society'
	_description = 'wizards records' 

	flats_id = fields.Many2one('biz.flats',string="Flats")
	flats_date = fields.Date(string="Flats Date")