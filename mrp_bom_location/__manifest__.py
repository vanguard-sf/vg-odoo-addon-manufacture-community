# Copyright 2017-20 ForgeFlow S.L. (https://www.forgeflow.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    "name": "MRP BOM Location",
    "summary": "Adds location field to Bill of Materials and its components.",
    "version": "16.0.1.1.1",
    "category": "Manufacture",
    "website": "https://github.com/OCA/manufacture",
    "author": "ForgeFlow, Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "application": False,
    "depends": ["mrp"],
    "data": ["views/mrp_view.xml", "views/report_mrpbomstructure.xml"],
    "assets": {
        "web.assets_backend": [
            "mrp_bom_location/static/src/xml/mrp_bom_overview_location.xml",
        ],
    },
    "installable": True,
}
