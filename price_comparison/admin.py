from django.contrib import admin


from main .models import Product_Database
from main .models import Customer
from main .models import Category
from main .models import Product



# Register your models here.
class AccountA(admin.ModelAdmin):
    model=Product_Database
    list_display=['id','name','email','product_name','price','link']
admin.site.register(Product_Database,AccountA)

class AccountB(admin.ModelAdmin):
    model=Customer
    list_display=['id','first_name','last_name','email','phone','password']
admin.site.register(Customer,AccountB)

class AccountC(admin.ModelAdmin):
    model=Category
    list_display=['category_name']
admin.site.register(Category,AccountC)

class AccountD(admin.ModelAdmin):
    model=Product
    list_display=['product_name','product_price','product_link']
admin.site.register(Product,AccountD)





