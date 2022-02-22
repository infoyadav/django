from django.urls import path
from users import views

urlpatterns = [
    path('', views.userlogin, name='userlogin'),
    path('userlogout/', views.userlogout, name='logout'),
    path('showuser/', views.alluser, name="showuser"),
    path('userregister/', views.user_register, name='userregister'),
    path('sortdata/', views.sort_user, name="sortdata"),
    path('searchuser/', views.search_user, name='searchuser'),
    path("profile/", views.profile, name="profile")
]
