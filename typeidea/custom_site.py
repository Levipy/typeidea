from django.contrib.admin import AdminSite
class Custom_site(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea管理后台'
    index_title = '首页'

custom_site = Custom_site(name='cus_admin')