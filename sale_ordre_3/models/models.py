from odoo import models, fields, api


class SaleOrderInherit(models.Model):
    _inherit = "sale.order"
    _description = "Sales Order3"

    test3 = fields.Char(string='test')