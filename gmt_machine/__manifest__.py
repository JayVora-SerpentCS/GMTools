# See LICENSE file for full copyright and licensing details.

{
    'name': "GMT Tools",
    'version': '12.0.1.0.0',
    'summary': """
        A system to retain data of gmt machines""",
    'description': """
        A system to retain data of GMT machines
    """,
    'author': "Serpent Consulting Services Pvt. Ltd.",
    'website': "http://www.serpentcs.com",
    'category': 'product',
    'depends': ['product'],
    'data': [
          'security/ir.model.access.csv',
          'views/machine_view.xml',
          'views/machine_image_view.xml'
             ],
    'installable': True,
    'application':True,

}