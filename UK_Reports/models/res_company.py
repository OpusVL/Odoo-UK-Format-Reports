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


class ResCompany(models.Model):
	_inherit = "res.company"

	accounts_dept_phone = fields.Char(
		help="Used in the headers of invoice related reports\n\
		(Invoice, Credit Note, and ProForma)"
	)
	accounts_dept_email = fields.Char(
		help="Used in the headers of invoice related reports\n\
		(Invoice, Credit Note, and ProForma)"
	)
	purchase_dept_phone = fields.Char(
		help="Used in the headers of purchase related reports\n\
		(Purchase Order, RFQ)"
	)
	purchase_dept_email = fields.Char(
		help="Used in the headers of purchase related reports\n\
		(Purchase Order, RFQ)"
	)
	sales_dept_phone = fields.Char(
		help="Used in the headers of sales related reports\n\
		(Quotation, Sales Order, Sales Delivery Order, Remittance Advice)"
	)
	sales_dept_email = fields.Char(
		help="Used in the headers of sales related reports\n\
		(Quotation, Sales Order, Sales Delivery Order, Remittance Advice)"
	)
	report_head_addrline1 = fields.Char(compute="_compute_report_head_addrline1")
	report_head_addrline2 = fields.Char(compute="_compute_report_head_addrline2")
	report_head_addrline3 = fields.Char(compute="_compute_report_head_addrline3")

	@api.multi
	def _compute_report_head_addrline1(self):
		for company in self:
			values = [company.street, company.street2]
			company.report_head_addrline1 = ", ".join(self.non_false_values(values))

	@api.multi
	def _compute_report_head_addrline2(self):
		for company in self:
			values = [company.city, company.state_id.name, company.zip]
			company.report_head_addrline2 = ", ".join(self.non_false_values(values))

	@api.multi
	def _compute_report_head_addrline3(self):
		for company in self:
			values = [company.company_registry, company.vat]
			company.report_head_addrline3 = ", ".join(self.non_false_values(values))

	def non_false_values(self, values):
		return [x for x in values if x is not False]
