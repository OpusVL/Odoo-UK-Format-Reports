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


class ResPartner(models.Model):
	_inherit = "res.partner"

	company_partner_ref_required = fields.Boolean(
		related="company_id.partner_ref_required")
	company_partner_ref_sequential_gen = fields.Boolean(
		related="company_id.partner_ref_sequential_gen")
	statement_of_account_filtered_move_lines = fields.One2many(
		compute="_compute_statement_of_account_filtered_move_lines")

	@api.model
	def create(self, vals):
		sequential_gen = self.env.user.company_id.partner_ref_sequential_gen
		if sequential_gen and not vals.get('ref'):
			vals['ref'] = self.env['ir.sequence'].next_by_code('res.partner.ref')
		return super(ResPartner, self).create(vals)
