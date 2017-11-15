# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Springboard Customizations/Developments',
    'category': 'Sale',
    'summary': 'Custom',
    'version': '1.0',
    'description': """
Core workflow customizations/developments
        """,
    'depends': ['base','stock','product','sale','base_automation','point_of_sale'],
    'data': [
        'data/ir_model.xml',
        'data/ir_model_fields.xml',
        'data/ir_actions.xml',
        'data/ir_ui_views.xml',
        'data/ir_model_access.xml',
    ],
    'installable': True,

}
