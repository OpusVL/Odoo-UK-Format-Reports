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


class AccountPayment(models.Model):
	_inherit = "account.payment"

	def get_amount_total(self):
		total = 0
		for invoice in self.reconciled_invoice_ids:
			total += invoice.amount_total_signed
		return total

	partner_invoice_address = fields.Many2one(
		'res.partner', compute="_compute_partner_invoice_address")

	@api.depends('partner_id.child_ids.type')
	def _compute_partner_invoice_address(self):
		for record in self:
			invoice_addresses = record.partner_id.child_ids.filtered(
				lambda contact: contact.type == 'invoice')
			if not invoice_addresses:
				record.partner_invoice_address = record.partner_id
			else:
				record.partner_invoice_address = invoice_addresses[0]


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
