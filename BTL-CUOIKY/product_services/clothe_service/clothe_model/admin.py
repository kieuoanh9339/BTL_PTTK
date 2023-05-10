from django.contrib import admin

# Register your models here.
from clothe_model.models import Clothe

class ClotheAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'inventory')
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Clothe, ClotheAdmin)