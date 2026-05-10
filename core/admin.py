from django.contrib import admin
from .models import Book, IssueBook, Category

# कॅटेगरी रजिस्टर केली
admin.site.register(Category)

# पुस्तकांचे टेबल डिझाईन
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'isbn', 'available_copies', 'is_available')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('is_available', 'category')

# Design of Issue Book's table
class IssueBookAdmin(admin.ModelAdmin):
    list_display = ('student', 'book', 'issue_date', 'return_date', 'status')
    list_filter = ('status', 'issue_date')
    search_fields = ('student__username', 'book__title')

admin.site.register(Book, BookAdmin)
admin.site.register(IssueBook, IssueBookAdmin)