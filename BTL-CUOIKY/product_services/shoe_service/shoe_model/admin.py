from django.contrib import admin

# Register your models here.
from shoe_model.models import Shoe

class ShoeAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'inventory')
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Shoe, ShoeAdmin)