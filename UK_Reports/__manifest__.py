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
	'version': '10.0.0.1',
	'category': 'Reporting',
	'description': """
		Customised reports for UK:
		- Sales order / Quotation
		- Account balance / overdue
		- Invoice print / credit note / pro forma
		- Purchase order / Quotation
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
		'data/report_paperformat.xml',

		'reports/account_invoice_report.xml',
		'reports/account_statement_report.xml',
		'reports/external_layouts.xml',
		'reports/generic_templates.xml',
		'reports/purchase_order_report.xml',
		'reports/sale_order_report.xml',

		'views/res_company_view.xml',
	],
	'demo_xml': [],
	'test': [],
	'license': 'AGPL-3',
	'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
