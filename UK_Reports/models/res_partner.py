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
		'account.move.line',
		compute="_compute_statement_of_account_filtered_move_lines")
	total_statement_account_value = fields.Float(compute="_compute_total_statement_values")
	total_statement_account_overdue = fields.Float(compute="_compute_total_statement_values")

	@api.multi
	@api.depends(
		'statement_of_account_filtered_move_lines.statement_account_overdue',
		'statement_of_account_filtered_move_lines.statement_account_value')
	def _compute_total_statement_values(self):
		for record in self:
			value_sum = 0
			overdue_sum = 0
			for line in record.statement_of_account_filtered_move_lines:
				value_sum += line.statement_account_value
				import pdb;pdb.set_trace()
				overdue_sum += line.statement_account_overdue
			record.total_statement_account_value = value_sum
			record.total_statement_account_overdue = overdue_sum

	@api.multi
	def _compute_statement_of_account_filtered_move_lines(self):
		for record in self:
			account_ids = record.company_id.statement_of_accounts_account_filter.ids
			domain = [
				('partner_id', 'child_of', record.ids),
				('account_id', 'in', account_ids)]
			moves = self.env['account.move.line'].search(domain)
			record.statement_of_account_filtered_move_lines = [[6, 0, moves.ids]]

	@api.model
	def create(self, vals):
		sequential_gen = self.env.user.company_id.partner_ref_sequential_gen
		if sequential_gen and not vals.get('ref'):
			vals['ref'] = self.env['ir.sequence'].next_by_code('res.partner.ref')
		return super(ResPartner, self).create(vals)
