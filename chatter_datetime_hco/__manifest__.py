{
    'name': "Chatter Datetime",
    'version': '18.0.0.0.0',
    'summary': "Displays the exact date and time in the chatter instead of showing relative days.",
    'description': """
Chatter Datetime module enhances Odoo's messaging system by showing precise timestamps in the chatter. 
This helps users track messages with exact date and time, instead of relative time (like '2 days ago').

Features:
- Displays exact date and time in chatter messages
- Improves traceability of communication
- Compatible with Odoo 18
""",
    'author': "HCOdooTech",
    'website': "https://www.linkedin.com/in/hcodoo-tech-191311391",
    'category': 'Productivity',
    'images': ['static/description/banner.png'],
    'depends': ['mail'],
    'price': 3.99,
    'currency': 'USD',
    'assets': {
        'web.assets_backend': [
            'chatter_datetime_hco/static/src/core/common/message.xml',
        ]
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}

