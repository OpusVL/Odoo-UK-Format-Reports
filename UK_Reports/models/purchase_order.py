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

from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
	_inherit = "purchase.order.line"

	uk_report_description_format = fields.Char(
		compute="_compute_uk_report_description_format"
	)

	@api.depends(
		'product_id.default_code',
		'product_id.seller_ids.product_code',
		'name',
	)
	@api.multi
	def _compute_uk_report_description_format(self):
		for line in self:
			seller_code = line.product_id._vendor_specific_code(
				line.order_id.partner_id)
			line.uk_report_description_format = "[{}] {}".format(
				seller_code or line.product_id.default_code, line.name)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
