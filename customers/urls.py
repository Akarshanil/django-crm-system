from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    
    # Customer URLs
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.customer_add, name='customer_add'),
    path('customers/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customers/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('customers/bulk-upload/', views.bulk_upload, name='bulk_upload'),
    path('customers/download-sample/', views.download_sample_excel, name='download_sample_excel'),
    path('customers/export-pdf/', views.export_pdf, name='export_pdf'),
    
    # User URLs
    path('users/', views.user_list, name='user_list'),
    path('users/add/', views.user_add, name='user_add'),
    path('users/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('users/<int:pk>/', views.user_detail, name='user_detail'),
    
    # Profile & Authentication
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]