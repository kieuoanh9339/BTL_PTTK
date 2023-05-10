from django.contrib import admin

# Register your models here.
from book_model.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'inventory')
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Book, BookAdmin)