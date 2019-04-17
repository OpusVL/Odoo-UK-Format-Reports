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
from helpers import integer_or_float


class AccountInvoice(models.Model):
	_inherit = "account.invoice"

	@api.multi
	def invoice_print(self):
		"""
		Print the invoice and mark it as sent, so that we can see more
		easily the next step of the workflow
		"""
		self.sent = True
		self.ensure_one()
		return self.env['report'].get_action(self, 'UK_Reports.uk_invoice')

	def your_reference_format(self):
		return self.name or '(Not provided)'

	def sale_payment_term(self):
		return self.get_sale_order().payment_term_id.name or '(Not provided)'

	def sale_number(self):
		return self.get_sale_order().name or '(Not provided)'

	def get_sale_order(self):
		return self.env['sale.order'].search([]).filtered(
			lambda x: self.id in x.invoice_ids.ids)


class AccountInvoiceLine(models.Model):
	_inherit = "account.invoice.line"

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


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
