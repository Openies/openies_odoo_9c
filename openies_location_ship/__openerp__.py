# -*- coding: utf-8 -*-

{
    'name': 'Openies Location ship',
    'version': '9.0.0.1.0',
    'summary': """
        Odoo Shipment Location on sale order
        """,
    'description': """
        Choose location on sale order and make shipment from selected location
    """,
    'category': 'Sale',
    'depends': ['sale','sale_stock'],
    'author': 'Openies Services',
    'website': 'http://www.openies.com',
    'data': [
        'views/sale_view.xml',
    ],
    'license': 'Other proprietary',
    'price': 0,
    'currency': 'EUR',
    'images': ['static/description/Openies_location_ship.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
