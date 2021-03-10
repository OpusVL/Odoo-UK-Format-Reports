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

from odoo import models, api, fields
from datetime import date


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    statement_account_overdue = fields.Float(compute="_compute_statement_account_values")
    statement_account_value = fields.Float(compute="_compute_statement_account_values")

    @api.depends('date_maturity', 'debit', 'credit')
    def _compute_statement_account_values(self):
        def is_overdue(moveline, on_this_date):
            if moveline.date_maturity:
                return on_this_date > moveline.date_maturity
            else:
                # No commercial agreement was in place
                return False
        todays_date = date.today()
        for record in self:
            record.statement_account_value = (record.debit - record.credit)
            if is_overdue(moveline=record, on_this_date=todays_date):
                record.statement_account_overdue = record.statement_account_value
            else:
                record.statement_account_overdue = 0
