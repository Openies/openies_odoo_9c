# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#    Copyright (C) 2014-2016 Openies Services(<http://openies.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import api, fields, models, _
from openerp.tools.translate import _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    @api.depends('warehouse_id')
    def _compute_stock_location_id(self):
        for order in self:
            order.lot_stock_id = order.warehouse_id.lot_stock_id.id

    location_id = fields.Many2one('stock.location', string='Location')
    lot_stock_id = fields.Many2one('stock.location', string='lot_stock_id',
                                   compute='_compute_stock_location_id',
                                   store=True)


class StockMove(models.Model):
    _inherit = "stock.move"

    @api.model
    def create(self, vals):
        if 'procurement_id' in vals:
            procurement_rec = self.env['procurement.order'].browse(vals.get('procurement_id'))
            location_id = procurement_rec.sale_line_id.order_id.location_id
        if location_id:
            vals.update({'location_id': location_id.id})
        else:
            return super(StockMove, self).create(vals)
        return super(StockMove, self).create(vals)


class ProductProduct(models.Model):

    _inherit = "product.product"

    @api.multi
    def _get_domain_locations(self):
        ctx = self._context.copy()
        if 'location' in ctx:
            location_rec = self.env['stock.location'].browse(ctx.get('location'))
            if location_rec:
                ctx.update({'location': location_rec.id})
        res = super(ProductProduct, self.with_context(ctx)).\
            _get_domain_locations()
        return res
