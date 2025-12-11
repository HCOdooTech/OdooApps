{
    'name': "Chatter Datetime",
    'summary': """
        Displays the exact date and time in the chatter instead of showing relative days.
        Helps users track messages with precise timestamps.
    """,
    'author': "HCOdooTech",
    'website': "https://www.linkedin.com/in/hcodoo-tech-191311391",
    'category': 'Productivity/Discuss',
    'images': ['static/description/banner.png'],
    'version': '18.0.0.0',
    'depends': ['mail'],
    'price': 3.99,
    'currency': 'USD',
    'assets': {
        'web.assets_backend': [
            'chatter_datetime_hco/static/src/core/common/message.xml',
        ]
    },
    'installable': True,
    'auto_install': False,
    'license': 'OPL-1',
}