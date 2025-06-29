# -*- coding: utf-8 -*-
{
    'name': "Boom CRM",

    'summary': "Extensión del módulo nativo de Ventas CRM para la prueba técnica.",

    'description': """
        Este módulo extiende el modelo 'crm.lead' para agregar campos adicionales
        y funcionalidades requeridas en la prueba técnica de Boom Solutions Odoo V18 CRM.
    """,

    'author': "Vladimir Cabrera",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/CRM',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
        'views/crm_order_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}

