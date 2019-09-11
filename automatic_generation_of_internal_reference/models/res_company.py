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

from odoo import models, fields, api


class ResCompany(models.Model):
	_inherit = "res.company"

	partner_ref_required = fields.Boolean("Customer Internal Ref Mandatory")
	partner_ref_sequential_gen = fields.Boolean("Sequentially Create Customer Internal Ref")
	product_code_required = fields.Boolean("Product Internal Ref Mandatory")
	product_code_sequential_gen = fields.Boolean("Sequentially Create Product Internal Ref")
