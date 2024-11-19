from django.urls import path
from . import views
from .views import ComplaintDetailView
from .views import HomeView
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',HomeView.as_view(),name='home'),
    path('about/',views.about,name='about'),
    path('services',views.services,name='services'),
    path('add_service',views.add_service,name='add_service'),
    path('register',views.register,name='register'),
    path('login/', views.login_page, name='login'),
    path('accounts/login/',views.login_page,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('complaint',views.complaint,name='complaint'),
    path('all_complaints',views.all_complaints,name='all_complaints'),
    path('user/complaints',views.user_complaints,name='user_complaints'),
    path('queries',views.queries,name='queries'),
    path('employee/login',views.employee_login,name='employee_login'),
    path('employee/dashboard',views.emp_main,name='emp_main'),
    path('new/complaints',views.new_complaints,name='new_complaints'),
    path('pending/complaints',views.pending_complaints,name='pending_complaints'),
    path('solved/complaints',views.solved_complaints,name='solved_complaints'),
    path('update/new/complaints/<str:pk>',views.update_new_complaints,name='update_new_complaints'),
    path('update/pending/complaints/<str:pk>',views.update_pending_complaints,name='update_pending_complaints'),
    path('update/solved/complaints/<str:pk>',views.update_solved_complaints,name='update_solved_complaints'),
    path('check/status',views.check_status,name='check_status'),
    path('add/green_initiative/', views.add_green_initiative, name='add_green_initiative'),
    path('green_initiatives/', views.green_initiatives, name='green_initiatives'),
    path('green_initiative/<int:pk>/', views.green_initiative_detail, name='green_initiative_detail'),
    path('green_initiatives/', views.green_initiatives, name='green_initiatives'),
    path('feedback/', views.feedback, name='feedback'),
    path('search/', views.search_results, name='search_results'),
    path('complaint/<int:pk>/', ComplaintDetailView.as_view(), name='complaint_detail'),
    path('query/', views.query_view, name='query_form'),
    path('complaint/<int:complaint_id>/thumbs-up/', views.thumbs_up_complaint, name='thumbs_up_complaint'),
    path('manage_employees/', views.add_employee, name="manage_employees"),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

]