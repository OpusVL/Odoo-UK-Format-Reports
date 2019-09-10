# -*- coding: utf-8 -*-

##############################################################################
#
# UK Report Template
# Copyright (C) 2019 OpusVL (<http://opusvl.com/>)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
	'name': 'UK customised reports',
	'version': '10.0.1.0.1',
	'category': 'Reporting',
	'description': """
		Customised reports for UK:
		- Sales Order / Quotation
		- Invoice / Credit Note / Pro-Forma
		- Purchase Order / Quotation
		- Sales Delivery Note
	""",
	'author': 'OpusVL',
	'website': 'http://opusvl.com',
	'depends': [
		'account',
		'base',
		'purchase',
		'report',
		'sale',
	],
	'data': [
		'reports/account_invoice_report.xml',
		'reports/external_layouts.xml',
		'reports/generic_templates.xml',
		'reports/purchase_order_report.xml',
		'reports/sale_order_report.xml',
		'reports/stock_picking_report.xml',
		'reports/remittance_advice_report.xml',
		'reports/statement_of_account_report.xml',

		'views/res_company_view.xml',
		'views/res_partner_view.xml',
		'views/stock_picking_view.xml',
		'views/product_views.xml',

		'data/report_paperformat.xml',
		'data/ir_actions_report_xml.xml',
		'data/ir_sequence.xml',
		'data/mail_template.xml',

		'email/remittance_advice_send_by_email.xml',
	],
	'demo_xml': [],
	'test': [],
	'license': 'AGPL-3',
	'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
