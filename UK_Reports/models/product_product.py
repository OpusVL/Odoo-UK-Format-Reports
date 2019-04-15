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


class ProductProduct(models.Model):
	_inherit = "product.product"

	def _vendor_specific_code(self, vendor):
		my_vendors = self.seller_ids.filtered(lambda seller: seller.name == vendor)
		if my_vendors:
			first_vendor = my_vendors.sorted(key=lambda r: r.sequence)[0]
			return first_vendor.product_code
		return False

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
