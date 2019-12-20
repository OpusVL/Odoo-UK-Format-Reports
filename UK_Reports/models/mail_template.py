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

class MailTemplate(models.Model):
	_inherit = "mail.template"

	# @api.model
	# def update_mail_templates(self):
	# 	self.env.ref('account.email_template_edi_invoice').write(dict(
	# 		report_template=self.env.ref('UK_Reports.uk_invoice_print').id))

	#Adding Remittance advice mail template in the action
	@api.model
	def create(self, vals):
		if 'name' in vals and vals['name'] == 'Remittance Advice':
			mail = super(MailTemplate, self).create(vals)
			mail.create_action()
			return mail
		else:
			return super(MailTemplate, self).create(vals)