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


class IrActionsReportXml(models.Model):
	_inherit = "ir.actions.report.xml"

	@api.model
	def unlink_report_actions(self):
		report_ext_ids = [
			'purchase.action_report_purchase_order',
			'purchase.report_purchase_quotation',
			'sale.report_sale_order',
			'account.account_invoice_action_report_duplicate',
			'account.account_invoices',
			'stock.action_report_delivery',
			'stock.action_report_picking',
			'account.action_report_print_overdue',
		]
		for report_ext_id in report_ext_ids:
			self.env.ref(report_ext_id).unlink_action()
