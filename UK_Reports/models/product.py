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


class ProductProduct(models.Model):
	_inherit = "product.product"

	def _vendor_specific_code(self, vendor):
		"""
		@param vendor: `res.partner` recordset
		"""
		my_vendors = self.seller_ids.filtered(lambda seller: seller.name == vendor)
		if my_vendors:
			first_vendor = my_vendors.sorted(key=lambda r: r.sequence)[0]
			return first_vendor.product_code
		return False

	@api.multi
	def write(self, vals):
		res = super(ProductProduct, self).write(vals)
		for record in self:
			if not self.env.context.get('bypass_default_code_recursion'):
				if self.env.user.company_id.product_code_sequential_gen:
					custom_code = self._custom_generate_variant_code_onwrite(
						record.product_tmpl_id, record.attribute_value_ids)
					record.with_context(bypass_default_code_recursion=True).default_code = custom_code
		return res

	@api.model
	def create(self, vals):
		sequential_gen = self.env.user.company_id.product_code_sequential_gen
		template_id = vals.get('product_tmpl_id')
		attribute_values = vals.get('attribute_value_ids')
		if sequential_gen and not vals.get('default_code') and template_id:
			vals['default_code'] = self._custom_generate_variant_code(
				template_id, attribute_values)
		return super(ProductProduct, self).create(vals)

	def _custom_generate_variant_code_onwrite(self, template, attribute_values):
		variant_base_code = template.default_code
		value_names = []
		if variant_base_code:
			value_names.append(variant_base_code)
		for attribute_value in attribute_values:
			value_names.append(attribute_value.name)
		return '/'.join(value_names)

	def _custom_generate_variant_code(self, template_id, attribute_values):
		"""
		@template_id: <int> product.template id
		@attribute_values: <odoo m2m list> i.e [6,0,[1,2]]
		The code returned will be a '/' seperated string.
			First item is template code which is based off an ir.sequence record
			Any item thereafter is an attribute value name i.e 'Small', or 'Black'
		"""
		# Split after the /, because for some reason the template takes on the
		# default code of a variant during this transaction, but reverts itself afterwards???
		# variant_base_code = self.env['product.template'].browse(template_id).default_code.split('/')[0]
		variant_base_code = self.env['product.template'].browse(template_id).default_code
		value_names = []
		if variant_base_code:
			value_names.append(variant_base_code)
		if attribute_values:
			attr_value_obj = self.env['product.attribute.value']
			for attribute_value_id in attribute_values[0][2]:
				value_names.append(attr_value_obj.browse(attribute_value_id).name)
		return '/'.join(value_names)


class ProductTemplate(models.Model):
	_inherit = "product.template"

	company_product_code_required = fields.Boolean(
		compute="_compute_default_code_system_fields")
	company_product_code_sequential_gen = fields.Boolean(
		compute="_compute_default_code_system_fields")
	# Prevent odoo from recomputing the templates default_code
	default_code = fields.Char(compute=False)

	@api.multi
	@api.depends('company_id.product_code_required', 'company_id.product_code_sequential_gen')
	def _compute_default_code_system_fields(self):
		for record in self:
			record.company_product_code_required = record.company_id.product_code_required
			record.company_product_code_sequential_gen = record.company_id.product_code_sequential_gen

	@api.model
	def create(self, vals):
		sequential_gen = self.env.user.company_id.product_code_sequential_gen
		if sequential_gen and not vals.get('default_code'):
			vals['default_code'] = self.env['ir.sequence'].next_by_code('product.default_code')
		return super(ProductTemplate, self.with_context(from_create=True)).create(vals)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
