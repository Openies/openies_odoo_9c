# -*- coding: utf-8 -*-

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

# class ProcurementOrder(models.Model):
#     _inherit = "procurement.order"
#
#     @api.model
#     def create(self, vals):
#         print "\n\nvallssssssss----procureeeeee", vals
#         res = super(ProcurementOrder, self).create(vals)
#         return res


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
