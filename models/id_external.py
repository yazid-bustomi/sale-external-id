# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleIdExternal(models.Model):
    """A single (buyer, product) -> external code mapping.

    Lets a company record what code a specific customer uses for one of
    its products, independent of the product's own internal reference.
    """
    _name = 'sale.id.external'
    _description = 'Sale External Product ID'

    name = fields.Char(
        string="Name",
        copy=False,
        required=True,
        help="Free-form label for this mapping, e.g. 'Buyer - Product'.",
    )

    buyer = fields.Many2one(
        'res.partner',
        string="Buyer",
        copy=False,
        required=True,
        help="Customer who uses the external ID below to refer to this product.",
    )

    product = fields.Many2one(
        'product.template',
        string="Product",
        copy=False,
        required=True,
    )

    primary_id = fields.Char(
        string="External ID",
        copy=False,
        required=True,
        help="The buyer's own code/reference for this product.",
    )
    secondary_id = fields.Char(
        string="Secondary ID",
        copy=False,
        help="An alternate or legacy code, if the buyer uses more than one.",
    )

    _sql_constraints = [
        (
            'buyer_product_uniq',
            'unique(buyer, product)',
            'This buyer already has an external ID mapped to this product.',
        ),
    ]
