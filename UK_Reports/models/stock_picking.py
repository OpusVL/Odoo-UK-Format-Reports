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

from odoo import models


class StockPicking(models.Model):
	_inherit = "stock.picking"

	def total_qty_sent_format(self):
		total_qty_sent = sum(
			[x.qty_done for x in self.pack_operation_product_ids])
		if int(total_qty_sent) == float(total_qty_sent):
			return int(total_qty_sent)
		else:
			return total_qty_sent

	def total_qty_to_follow_format(self):
		total_qty_to_follow = sum(
			[x.product_qty - x.qty_done for x in self.pack_operation_product_ids])
		if int(total_qty_to_follow) == float(total_qty_to_follow):
			return int(total_qty_to_follow)
		else:
			return total_qty_to_follow


class StockPackOperation(models.Model):
	_inherit = "stock.pack.operation"

	def uk_report_description_format(self):
		return "[{}] {}".format(
			self.product_id._vendor_specific_code(self.picking_id.partner_id)
			or self.product_id.default_code,
			self.product_id.name
		)

	def qty_ordered_format(self):
		# Most companies don't sell 1.5x anything, so strip the `.0` if possible
		if int(self.product_qty) == float(self.product_qty):
			return int(self.product_qty)
		else:
			return self.product_qty

	def qty_sent_format(self):
		# Most companies don't sell 1.5x anything, so strip the `.0` if possible
		if int(self.qty_done) == float(self.qty_done):
			return int(self.qty_done)
		else:
			return self.qty_done

	def qty_to_follow_format(self):
		qty_to_follow = self.product_qty - self.qty_done
		if int(qty_to_follow) == float(qty_to_follow):
			return int(qty_to_follow)
		else:
			return qty_to_follow

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
