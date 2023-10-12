# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name" : "All In One Debranding Odoo | Odoo Website Debranding | Odoo Point Of Sale Debranding | Odoo Backend Debranding",
    "author" : "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",  
    "category": "Extra Tools",
    "license": "OPL-1",
    "summary": "Hide Odoo From Website Remove Odoo From Login Page Replace Odoo Bot Replace Odoo Image Replace Odoo From Chatter Replace Odoo From Everywhere In Website Odoo Backend Debranding Odoo Branding Delete Odoo",
    "description": """"Odoo Backend Debranding" module helps to enhance your brand. Odoo Debranding plays an important role. This module removes odoo references to customize company details. You can change the organization detail like logo, title, popup, website anytime.It hides odoo and promotes your organization. Hurray!""",   
    "version":"16.0.1",
    "depends" : ["base_setup","web","mail","portal","point_of_sale","website"],
    "application" : True,
    "data" : [
            # Base 
            "sh_base_debranding/security/app_security.xml",
            "sh_base_debranding/security/ir.model.access.csv",
            "sh_base_debranding/data/sh_configuraion_data.xml",
           
            # Backend
            "sh_backend_debranding/views/views.xml",
            "sh_backend_debranding/views/fevicon.xml",
            "sh_backend_debranding/views/mail_template_views.xml",
            "sh_backend_debranding/views/res_config_setting_views.xml",

            # Pos
            'sh_pos_debranding/views/pos_inherit.xml',

            # Website
            "sh_website_debranding/views/tmpl_views.xml",
    ],

    'assets': {        
        'web.assets_backend': [            
            # Backend
            'sh_all_in_one_debranding/sh_backend_debranding/static/src/js/system_name.js',
            'sh_all_in_one_debranding/sh_backend_debranding/static/src/js/error.js',
            'sh_all_in_one_debranding/sh_backend_debranding/static/src/js/dialogue.js',
            'sh_all_in_one_debranding/sh_backend_debranding/static/src/js/customize_user.js',
            'sh_all_in_one_debranding/sh_backend_debranding/static/src/js/avatar.js',   
            'sh_all_in_one_debranding/sh_backend_debranding/static/src/xml/mail_bot.xml',         
        ],
        'point_of_sale.assets': [
            'sh_all_in_one_debranding/sh_pos_debranding/static/src/js/pos.js', 
            'sh_all_in_one_debranding/sh_pos_debranding/static/src/xml/pos.xml',
        ],
        'web.assets_frontend': [
            'sh_all_in_one_debranding/sh_base_debranding/static/src/scss/style.scss',
        ],
    },
    "images": ["static/description/background.png",],  
    "auto_install":False,
    'post_init_hook': 'post_init_hook',
    "installable" : True,
    "price": 150,
    "currency": "EUR"
}
