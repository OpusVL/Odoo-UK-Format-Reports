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

from openerp import models, api, exceptions


class Report(models.Model):
	_inherit = 'report'

	@api.multi
	def render(self, template, values=None):
		if template == 'UK_Reports.uk_delivery_note':
			if values.get('docs'):
				self.validate_delivery_note(values)
		return super(Report, self).render(template, values)

	def validate_delivery_note(self, values):
		if any(state != 'done' for state in values.get('docs').mapped('state')):
			raise exceptions.Warning(
				"You cannot print a delivery note on an unfinished picking")
