from django.contrib import admin
from application1.models import products
class product_admin(admin.ModelAdmin):
    list_display=['pid','pname','price','company','M_date','E_date']
admin.site.register(products,product_admin)