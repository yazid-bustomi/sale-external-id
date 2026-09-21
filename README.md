# Sale External ID Mapping

Small Odoo 18 addon that maps your own products to the item codes a specific
customer uses to refer to them — useful whenever purchase orders, packing
lists, or EDI files from a customer reference "their" code instead of yours.

> Built as part of a real Odoo sales implementation. Company-specific data
> has been removed; the business logic is unchanged.

## Why this module

In export/B2B manufacturing it's common for each customer to use their own
internal item numbering, completely unrelated to your own SKU. Without a
mapping table, matching "customer says code X" back to "our product Y"
becomes tribal knowledge. This module gives that mapping a proper home in
Odoo instead of a spreadsheet.

## Features

- A dedicated **Product External ID** list under **Sales > Products**.
- One record per **buyer + product** pair, so the same product can have a
  different code per customer.
- A **primary** external ID plus an optional **secondary ID** (for a
  legacy/alternate code some customers still use).
- A database-level uniqueness constraint prevents accidentally mapping the
  same buyer/product pair twice.

## Requirements

- Odoo **18.0**
- Standard `sale` app installed

## Installation

1. Copy this folder into your Odoo `addons` path:
   ```bash
   cp -r sale_external_id /path/to/odoo/addons/
   ```
2. Restart the server and update the apps list
   (`Settings > Apps > Update Apps List`, with developer mode enabled).
3. Search for **"Sale External ID Mapping"** and click **Install**.

## Usage

1. Go to **Sales > Products > Product External ID**.
2. Click **New** and fill in:
   - **Buyer** — the customer who uses this code.
   - **Product** — your internal product.
   - **External ID** — the code that customer uses for it.
   - **Secondary ID** *(optional)* — an alternate/legacy code.
3. Use this list as a lookup reference when processing documents from that
   customer, or query the `sale.id.external` model from your own
   integration/import code to resolve a customer code back to a product.

## Project structure

```
sale_external_id/
├── models/
│   └── id_external.py   # sale.id.external: buyer/product -> code mapping
├── views/                # list, form, search views + menu
└── security/             # access rights
```

## License

Licensed under [LGPL-3](LICENSE).

## Author

**Akhmad Yazid Bustomi**
GitHub: [github.com/yazid-bustomi](https://github.com/yazid-bustomi)
