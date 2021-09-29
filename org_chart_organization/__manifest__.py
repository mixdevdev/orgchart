# -*- coding: utf-8 -*-
{
	'name': "Product Chart Category",
	'summary': """Dynamic display of your Category Product""",
	'description': """Dynamic display of your Category Product""",
	'author': "Ranoa",
	'category': 'Human Resources',
	'version': '2.0',
	# 'license': 'AGPL-3',
	'depends': ['stock'],
	'data': ['views/org_chart_views.xml'],
	
	'qweb': [
        "static/src/xml/org_chart_category.xml",
    ],
	'installable': True,
	'application': True,
	'auto_install': False,
}
