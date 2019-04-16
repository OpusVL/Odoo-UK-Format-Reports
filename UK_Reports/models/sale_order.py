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


class SaleOrder(models.Model):
	_inherit = "sale.order"

	@api.multi
	def print_quotation(self):
		'''
		This function prints the sales order and mark it as sent, so that we can see more easily the next step of the workflow
		'''
		self.signal_workflow('quotation_sent')
		self.ensure_one()
		return self.env['report'].get_action(self, 'sale.UK_SalesOrder')


class SaleOrderLine(models.Model):
	_inherit = "sale.order.line"

	def uk_report_description_format(self):
		if self.product_id.default_code:
			return "[{}] {}".format(
				self.product_id.default_code,
				self.product_id.name
			)
		else:
			return self.product_id.name

	def qty_format(self):
		# Most companies don't sell 1.5x anything, so strip the `.0` if possible
		if self.product_uom_qty.is_integer():
			return int(self.product_uom_qty)
		else:
			return self.product_uom_qty
