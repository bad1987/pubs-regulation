# Create permissions
permission_data = [
    {'name': "Acl_product_read", 'description': "This user read all products", 'mode': "R", 'model_name': "product"},
    {'name': "Acl_product_update", 'description': "This user update all products", 'mode': "W", 'model_name': "product"},
    {'name': "Acl_product_delete", 'description': "This user delete all products", 'mode': "D", 'model_name': "product"},
    
    {'name': "Acl_order_read", 'description': "This user read all orders", 'mode': "R", 'model_name': "order"},
    {'name': "Acl_order_update", 'description': "This user update all orders", 'mode': "W", 'model_name': "order"},
    {'name': "Acl_order_delete", 'description': "This user delete all orders", 'mode': "D", 'model_name': "order"},
    
    {'name': "Acl_setting_read", 'description': "This user read all settings", 'mode': "R", 'model_name': "setting"},
    {'name': "Acl_setting_update", 'description': "This user update all settings", 'mode': "W", 'model_name': "setting"},
    {'name': "Acl_setting_delete", 'description': "This user delete all settings", 'mode': "D", 'model_name': "setting"},
    
    {'name': "Acl_vendor_read", 'description': "This user read all vendors", 'mode': "R", 'model_name': "user"},
    {'name': "Acl_vendor_update", 'description': "This user update all vendors", 'mode': "W", 'model_name': "user"},
    {'name': "Acl_vendor_delete", 'description': "This user delete all vendors", 'mode': "D", 'model_name': "user"},
    
    {'name': "Acl_admin_read", 'description': "This admin read all admins", 'mode': "R", 'model_name': "user"},
    {'name': "Acl_admin_update", 'description': "This admin update all admins", 'mode': "W", 'model_name': "user"},
    {'name': "Acl_admin_delete", 'description': "This admin delete all admins", 'mode': "D", 'model_name': "user"},
    
]

data_payment_method = [
    {"name": "PayPal", "processor_id": "122"},
    {"name": "PayPal plus", "processor_id": "132"},
    {"name": "Klarna", "processor_id": "134"}
]