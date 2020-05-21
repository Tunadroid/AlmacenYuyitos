from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User_account)
admin.site.register(Administrator)
admin.site.register(Seller)
admin.site.register(Debt)
admin.site.register(Client)
admin.site.register(Debt_payment)
admin.site.register(Provider)
admin.site.register(Order)
admin.site.register(Product_type)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Product_On_Sale)

