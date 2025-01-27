from django.contrib import admin
from .models import Book,Review
# Register your models here.

class ReviewInline(admin.TabularInline):
    model = Review
class BookAdmin(admin.ModelAdmin):#specify wich field we also want to display
    list_display = ('title', 'author', 'price')
    inlines = [
        ReviewInline,  # Display the reviews inline with the book
    ]
admin.site.register(Book,BookAdmin)

