# -*- coding: utf-8 -*-
{
    'name': 'Update POS Payment Line',
    'category': 'Sales/Point of Sale',
    'summary': (
        'Automatically reset unpaid POS payment lines when order details change'
    ),
    'version': '17.0.1.0.0',
    'author': "HCOdooTech",
    'website': "https://www.linkedin.com/in/hcodoo-tech-191311391",
    'images': ['static/description/banner.png'],
    'description': """
        POS Payment Line Update
        ======================
        
        This module enhances the **Odoo Point of Sale** experience by ensuring
        payment accuracy whenever a POS order is modified.
        
        In standard Odoo POS behavior, payment lines may remain partially applied
        even after changes to the order. This can lead to incorrect totals, cashier
        confusion, and potential accounting inconsistencies.
        
        **POS Payment Line Update** automatically clears unpaid payment lines as soon
        as the order is changed, ensuring the payment process always reflects the
        latest order state.
        
        Key Features
        ------------
        • Automatically clears unpaid payment lines when:
          - Products are added or removed
          - Product quantities are changed
          - Prices are modified
          - Discounts are applied or updated
        
        • Prevents incorrect or outdated payment amounts  
        • Improves cashier workflow and reduces POS errors  
        • Ensures accurate order totals before validation  
        • Works seamlessly without extra configuration  
        
        Benefits
        --------
        ✔ Eliminates payment mismatches  
        ✔ Reduces cashier mistakes  
        ✔ Improves POS reliability and accuracy  
        ✔ Fully compatible with Odoo 17 POS  
        
        Technical Details
        -----------------
        • Lightweight and performance-optimized  
        • Uses POS model extensions (JavaScript)  
        • No impact on backend accounting logic  
        • Safe to install on existing POS setups  
        
        This module is ideal for retail stores, restaurants, and high-volume POS
        environments where orders are frequently modified before payment validation.
    """,
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'update_pos_payment_line/static/src/js/models.js',
        ],
    },
    'price': 8.99,
    'currency': 'USD',
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'OPL-1',
}
