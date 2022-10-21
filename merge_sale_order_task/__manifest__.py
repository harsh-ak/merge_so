{
    'name': 'Merge Sale Order',
    'version': '1.0',
    'category': 'Extra Tools',
    'summary': 'This module shows exported sales',
    'description': """
   
    """,
    'sequence':-500,
    'depends': ['sale_management'],
    'data': [
    'views/merge_so_server_action.xml'

    ],
    'installable':True,
    'auto_install':False,
    'application':True,
    'license': 'LGPL-3',
}