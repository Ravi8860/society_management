# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details
{
	'name':'Society Management',
	'version':'13.0.0.0',
	'sequence':5,

	'description':"society management model",
	'website':'https://www.bizople.com/',
	'depends':['base','web','sale',],
	'data':[

		'security/ir.model.access.csv',
		'views/maintenance_bill_views.xml',
		'wizards/create_society.xml',
		'views/flats_views.xml',
		'views/allotment_views.xml',
		'views/complain_views.xml',
		'views/visitor_views.xml',
		'views/res_partner_views.xml',
		'views/sale_orders_views.xml',
		'views/sale_report_views.xml',
		'views/invoices_views.xml',
		
		
		
	
	],
	
	'author':'ravi',
	'installable':True,
	'application':True, 	
	'auto_install':False,
	'license':'OPL-1',
}
