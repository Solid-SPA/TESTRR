# -*- coding: utf-8 -*-
{
    'name' : 'Website Servicios de Mantenimiento de Autos',
    'version' : '1.0',
    'summary': 'Website Servicios de Mantenimiento de Autos ',
    'sequence': 1,
    'description': """
        ====================
        Website 
    """,
    'category': 'Sales',
    'website':"https://www.solidconsult.cl",
    'author': 'Rafael E Requena G For Solid Consult',
    'images' : [''],
    'depends' : ['base','website'],
    'data': [
        'views/home.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
            'web._assets_primary_variables': [
        ],
        'web.assets_backend': [
        ],
        'web.assets_frontend': [
        ],
        'web.assets_tests': [
        ],
        'web.qunit_suite_tests': [
        ],
        'web.assets_qweb': [
            
        ],
    },
    'external_dependencies': {
        'python': [
                    ],
                }
}

