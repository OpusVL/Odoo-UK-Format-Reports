# -*- coding: utf-8 -*-

##############################################################################
#
# Automatic generation of internal reference
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
	'name': 'Automatic generation of internal reference',
	'version': '10.0.1.0.1',
	'category': '',
	'description': """
		* Adds 4 new boolean fields to a company. 2 for company/individual, and 2 for product.
			- `X Mandatory`
			- `Sequentially create X`
		* Where X is, on res.partner - the `Internal Reference` field,
		and on product.template/product.product - the `Product Code` field.
		* The behaviour of the fields are as follows:
			- When `X Mandatory` is ticked alone, it will make the field mandatory at the form level.
			- When ticked in combination with `Sequentially create X` - it will make the field
		sequentially generate on create, and be readonly in the view.
			- When `Sequentially create X` is ticked alone - it will make the field
		sequentially generate on create (if no user specified code is provided)
		* The sequence records can be configured in Odoo to add padding, prefixes, and suffixes
		* For res.partner, the logic is simply generate a sequence number. No number will be generated for contacts
		* For product.template, the logic is simply generate a sequence number.
		* For product.product, the logic is to take the `product_tmpl_id` code,
		and append each attribute of the variant - separated by a `/` for each
		attribute name. The ordering of the appendage is by attribute name
		(not to be mistaken for attribute value name). This is to ensure the
		ordering of all variant codes are consistent.
	""",
	'author': 'OpusVL',
	'website': 'http://opusvl.com',
	'depends': [
		'base',
		'purchase',
	],
	'data': [
		'views/res_company_view.xml',
		'views/res_partner_view.xml',
		'views/product_views.xml',

		'data/ir_sequence.xml',
	],
	'demo_xml': [],
	'test': [],
	'license': 'AGPL-3',
	'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
