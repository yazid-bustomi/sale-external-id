# -*- coding: utf-8 -*-
# Part of sale_external_id. See LICENSE file for full copyright and licensing details.
{
    'name': 'Sale External ID Mapping',
    'version': '18.0.1.0.0',
    'category': 'Sales',
    'summary': 'Map your own products to the product codes/IDs used by a specific '
               'customer, so both sides can talk about the same item unambiguously.',
    'description': """
Sale External ID Mapping
=========================
Many B2B customers (especially in export/manufacturing) refer to your
products using **their own internal item codes**, which rarely match your
own SKUs. Purchase orders, packing lists, and shipping documents they send
you use their code; your ERP uses yours.

This module adds a simple lookup table, **Sales > Products > Product
External ID**, where you register:

* which **customer** (buyer) uses a code,
* which **product** it maps to,
* the customer's **primary external ID/code**, and
* an optional **secondary ID** (e.g. an alternate or legacy code).

This gives you a single place to look up "what does the customer call
this product" without cluttering the product form itself with
customer-specific codes, and lets other modules or integrations resolve a
customer's code back to your internal product.

Features
--------
* Dedicated list/form view under the Sales app's Catalog menu.
* One record per (buyer, product) combination, so a product can have a
  different external code per customer.
* Simple enough to extend: use it as a lookup source for import scripts,
  EDI integrations, or custom reports that need to print the customer's
  own code instead of yours.
""",
    'author': 'Akhmad Yazid Bustomi',
    'website': 'https://github.com/yazid-bustomi',
    'maintainer': 'Akhmad Yazid Bustomi',
    'license': 'LGPL-3',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/external_id_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
