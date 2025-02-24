from django.contrib import admin
from .models import (
    CustomUser,
    Currency,
    ProductsAvailable,
    ServicesAvailable, ImagesManage,
)

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Currency)
admin.site.register(ProductsAvailable)
admin.site.register(ServicesAvailable)
admin.site.register(ImagesManage)
