from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_view, name='test'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('users/', views.get_all_users, name='users_list'),
    path('user/<str:email>/', views.get_user_by_email, name='user_detail'),
    path('update/<str:email>/', views.update_user, name='update_user'),
    path('delete/<str:email>/', views.delete_user, name='delete_user'),
]