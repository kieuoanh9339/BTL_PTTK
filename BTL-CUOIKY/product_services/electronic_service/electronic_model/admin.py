from django.contrib import admin

# Register your models here.
from electronic_model.models import Electronic

class ElectronicAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'inventory')
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Electronic, ElectronicAdmin)