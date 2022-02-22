from django.urls import path
from dashb import views

urlpatterns = [

    # category urls.
    path("searchcategory/", views.search_category, name="searchcategory"),
    path("addcategory/", views.add_category, name="add_category"),
    path('editcategory/<int:id>/', views.edit_category, name='editcategory'),
    path('delete_category/<int:cat_id>/', views.delete_category, name='editcategory'),

    # product urls.
    path("", views.show_product, name="product"),
    path("addcategory/", views.add_Product, name="create_product"),
    path('updateProduct/<int:p_id>/', views.update_product, name='editproduct'),
    path('deleteProduct/<int:id>/', views.delete_product, name='deleteproduct'),

    # for order urls
    path('order/', views.order_graph, name="orders"),

]
