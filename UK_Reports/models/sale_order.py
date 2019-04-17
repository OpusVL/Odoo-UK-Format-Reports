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


class SaleOrder(models.Model):
	_inherit = "sale.order"

	@api.multi
	def print_quotation(self):
		"""
		Redirect to use the UK report formatted sales order
		"""
		super(SaleOrder, self).print_quotation()
		return self.env['report'].get_action(self, 'UK_Reports.uk_salesorder')


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
		return integer_or_float(self.product_uom_qty)
