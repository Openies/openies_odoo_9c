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
