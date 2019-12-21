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

from odoo import models, api
from ..helpers import integer_or_float


class AccountMove(models.Model):
	_inherit = "account.move"

	# def invoice_print(self):
	# 	"""
	# 	Print the invoice and mark it as sent, so that we can see more
	# 	easily the next step of the workflow
	# 	"""
	# 	super(AccountMove, self).invoice_print()
	# 	return self.env['report'].get_action(self, 'UK_Reports.uk_invoice')

	def your_reference_format(self):
		return self.name or '(Not provided)'

	def sale_payment_term(self):
		return self.get_sale_order().payment_term_id.name or '(Not provided)'

	def sale_number(self):
		return ", ".join(so.name for so in self.get_sale_order()) or '(Not provided)'

	def get_sale_order(self):
		return self.env['sale.order'].search([]).filtered(
			lambda x: self.id in x.invoice_ids.ids)


class AccountMoveLine(models.Model):
	_inherit = "account.move.line"

	def uk_report_description_format(self):
		if self.product_id.default_code:
			return "[{}] {}".format(
				self.product_id.default_code,
				self.product_id.name
			)
		else:
			return self.product_id.name

	def qty_format(self):
		return integer_or_float(self.quantity)

	def tax_codes_string(self):
		return ','.join(self.invoice_line_tax_ids.mapped('description')) or ''

	# Used a function to in odoo12 to calculate price total of an invoice line
	def get_price_total(self):
		currency = self.move_id and self.move_id.currency_id or None
		price = self.price_unit * (1 - (self.discount or 0.0) / 100.0)
		taxes = False
		if self.tax_ids:
			taxes = self.tax_ids.compute_all(price, currency, self.quantity, product=self.product_id,
				partner=self.move_id.partner_id)
		price_subtotal = taxes['total_excluded'] if taxes else self.quantity * price
		price_total = taxes['total_included'] if taxes else price_subtotal
		return price_total

	def total_gross_format(self):
		price_total = self.get_price_total()
		return integer_or_float(price_total)

	def total_tax_format(self):
		price_total = self.get_price_total()
		return integer_or_float(price_total - self.price_subtotal)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
