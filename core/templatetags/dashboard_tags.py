from django import template
from core.models import Book, IssueBook
from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag
def get_stats():
    return {
        'total_books': Book.objects.count(),
        'available_books': Book.objects.filter(is_available=True).count(),
        'issued_books': IssueBook.objects.filter(status='Approved').count(),
        'pending_requests': IssueBook.objects.filter(status='Pending').count(), 
        'returned_books': IssueBook.objects.filter(status='Returned').count(),
        'total_students': User.objects.filter(is_superuser=False).count(),
    }