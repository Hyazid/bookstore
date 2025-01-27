from django.contrib import admin
from .models import Book
# Register your models here.


class BookAdmin(admin.ModelAdmin):#specify wich field we also want to display
    list_display = ('title', 'author', 'price')
admin.site.register(Book,BookAdmin)

