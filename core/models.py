from django.db import models
from django.contrib.auth.models import User
from datetime import date

# 1. New category class
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    description = models.TextField(blank=True, null=True) # All information of books
    image = models.ImageField(upload_to='book_covers/', blank=True, null=True) # Book's Image
    total_copies = models.IntegerField(default=1) # Total copies
    available_copies = models.IntegerField(default=1) # Available copies
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class IssueBook(models.Model):
    # Status options
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Returned', 'Returned'),
    ]
    
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True) # This date can be empty while making the request
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending') # New status column
    
    def save(self, *args, **kwargs):
        if self.pk: # If this is an old request (i.e., the admin is changing the status)
            old_issue = IssueBook.objects.get(pk=self.pk)
            
            # 1. If the admin changes the request status from "Pending" to "Approved":
            if old_issue.status != 'Approved' and self.status == 'Approved':
                if self.book.available_copies > 0:
                    self.book.available_copies -= 1 # Reduce one book
                    if self.book.available_copies == 0:
                        self.book.is_available = False # If it becomes zero, mark it as Out of Stock
                    self.book.save()
            
            # 2. If the book is marked as "Returned":
            elif old_issue.status == 'Approved' and self.status == 'Returned':
                self.book.available_copies += 1 # Increase one book
                self.book.is_available = True # Make it available again
                self.book.save()
                
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.student.username} - {self.book.title}"

    @property
    def calculate_fine(self):
        if self.status == 'Approved' and self.return_date and date.today() > self.return_date:
            overdue_days = (date.today() - self.return_date).days
            return overdue_days * 5
        return 0