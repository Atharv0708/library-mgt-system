from django.contrib.auth import update_session_auth_hash
from .forms import StudentRegistrationForm, StudentLoginForm, StudentPasswordChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import Book, IssueBook, Category
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Book

def book_list(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')
    # Get all Books
    book_list_data = Book.objects.all().order_by('-id')
    
    # If it is searched
    if query:
        book_list_data = book_list_data.filter(Q(title__icontains=query) | Q(author__icontains=query))
        
    # If it has been click on category
    if category_id:
        book_list_data = book_list_data.filter(category_id=category_id)
        
    paginator = Paginator(book_list_data, 12)
    page_number = request.GET.get('page')
    books = paginator.get_page(page_number)
    
    # To send all categories from the database to the page
    categories = Category.objects.all()
        
    return render(request, 'book_list.html', {
        'books': books, 
        'query': query, 
        'categories': categories, # New
        'selected_category': category_id # नNew
    })

# 2. New Student's Registration
def register_user(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save() # user will be saved in the database
            return redirect('login') # After registration, redirect to the login page
    else:
        form = StudentRegistrationForm()
    return render(request, 'register.html', {'form': form})

# 3. Student's login
def login_user(request):
    if request.method == 'POST':
        form = StudentLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user) # Log in the user
            return redirect('book_list') # After login redirect to books page
    else:
        form = StudentLoginForm()
    return render(request, 'login.html', {'form': form})

# 4. Logout
def logout_user(request):
    logout(request)
    return redirect('login')

# 5. Students own Dashboard
@login_required(login_url='login')
def student_dashboard(request):
    # Show only the requests of the logged-in student
    my_requests = IssueBook.objects.filter(student=request.user)
    return render(request, 'student_dashboard.html', {'my_requests': my_requests})

# 6. Request a book
@login_required(login_url='login')
def request_book(request, book_id):
    book = Book.objects.get(id=book_id)
    # Check whether a request has already been made
    existing_request = IssueBook.objects.filter(student=request.user, book=book, status__in=['Pending', 'Approved']).exists()
    
    if not existing_request and book.is_available:
        # Create a new pending request
        IssueBook.objects.create(student=request.user, book=book, status='Pending')
        
    return redirect('student_dashboard')

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book_detail.html', {'book': book})

@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = StudentPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            # To ensure the user is not automatically logged out after changing the password:
            update_session_auth_hash(request, form.user) 
            return redirect('student_dashboard') # On success, redirect to the dashboard
    else:
        form = StudentPasswordChangeForm(user=request.user)
    
    return render(request, 'change_password.html', {'form': form})