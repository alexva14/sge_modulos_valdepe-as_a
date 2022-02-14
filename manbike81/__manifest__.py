# -*- coding: utf-8 -*-
{
    'name': "manbike81",

    'summary': """
        Modulo creado para llevar las bicicletas de un usuario""",

    'description': """
        Modulo creado para llevar las bicicletas de un usuario el cual nos ha sido pedido para la practica
    """,

    'author': "Alex Valdepeñas Andujar",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
