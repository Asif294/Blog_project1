from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/', views.register,name='register'),
    # path('login/', views.userlogin,name='userlogin'),
    path('login/', views.userloginview.as_view(), name='userlogin'),
    path('profile/', views.profile, name='profile'),
    path('Edit/profile/', views.edit_profile,name='edit_profile'),
    path('profile/edit/change_pass',views.change_pass,name='change_pass'),
    path('user_logout',views.user_logout,name='user_logout'),
    # path('user_logout',views.LogoutV.as_view(),name='user_logout'),
    
   
]