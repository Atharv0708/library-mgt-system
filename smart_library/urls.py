from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.book_list, name='book_list'),
    
    # New Links
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('request_book/<int:book_id>/', views.request_book, name='request_book'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('change-password/', views.change_password, name='change_password'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)