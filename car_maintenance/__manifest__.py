# -*- coding: utf-8 -*-
{
    'name' : 'Servicios de Mantenimiento de Autos',
    'version' : '1.0',
    'summary': 'Registration, reporting and sale of services performed on vehicles. ',
    'sequence': 1,
    'description': """
        ====================
        Registration, reporting and sale of services performed on vehicles. 

    """,
    'category': 'Sales',
    'website':"https://www.solidconsult.cl",
    'author': 'Rafael E Requena G For Solid Consult',
    'images' : [''],
    'depends' : ['base','sale','point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'security/car_maintenance_security.xml',
        'data/car_services_data.xml',
        'views/car_maintenance_view.xml',
        'wizards/wz_car_maintenance_view.xml',
    ],
    'demo': [
        'demo/car_maintenance_demo.xml'
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
        'python': ['xlsxwriter','xlrd'
                    ],
                }
}

