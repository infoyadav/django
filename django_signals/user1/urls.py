from django.urls import path
from user1 import views 

urlpatterns = [
    # this urls for user1 app.
    path('user_pdf/', user_views.UserListView.as_view(), name='user_list_view'),
    path('user/pdf/<pk>/', user_views.users_render_pdf_view, name='user_pdf_view'),
    path("createuser/", user_views.createUser, name='createuser'),
    # path('user1/login/', user_views.userlogin, name='Userlogin'),
    # path('user1/dashboard', user_views.dashboard, name='dashboard'),
    # path("user1/logout", user_views.userlogout_request, name="logout"),
    # path('user1/viewstore', user_views.view_store, name='viewstore'),
]