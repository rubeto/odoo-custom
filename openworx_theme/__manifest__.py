# -*- coding: utf-8 -*-
# Copyright 2016, 2019 Openworx - Mario Gielissen
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Openworx Material Backend",
    "summary": "Openworx Material Backend",
    "version": "12.0.0.1",
    "category": "Theme/Backend",
    "website": "http://www.openworx.nl",
	"description": """
		Openworx Material Backend theme for Odoo Community Edition.
    """,
	'images':[
        'images/screen.png'
	],
    "author": "Openworx",
    "license": "LGPL-3",
    "depends": [
        'web',
        'web_responsive',
    ],
    "data": [
        'views/assets.xml',
		'views/res_company_view.xml',
		'views/users.xml',
        'views/sidebar.xml',
		#'views/web.xml',
    ],
    "installable": True,
    "auto_install": True,
}

