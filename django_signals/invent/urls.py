"""invent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dashb import views
# from users import views as users_views

from user1 import views as user_views


# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", include('dashb.urls'), name=""),
    path('', include('users.urls')),
    

    # here category related all urls with authenticated.
    path('product/', views.show_product, name="product"),
    path("product_list/", views.all_product, name="productlist"),
    path('create_product/', views.add_Product, name="create_product"),
    path('edit_product/<int:p_id>/', views.update_product, name='editproduct'),
    path('deleteproduct/<int:id>/', views.delete_product, name='deleteproduct'),
    path("viewProduct/", views.viewProduct, name="viewProduct"),
    path('order/', views.order_graph, name="order"),

    # category-wise product url
    path('cate-wise/', views.categorywiseProduct,name='cate-wise'),
    

    # here category related all urls.
    path("searchcategory/", views.search_category, name="searchcategory"),
    path("add_category/", views.add_category, name="add_category"),
    path('editcategory/<int:id>/', views.edit_category, name='editcategory'),
    path('deletecatgeory/<int:cat_id>/', views.delete_category, name="deletecatgeory"),

    path('downloadCsv/', views.getfile, name='download_file'),

    # this is for per items pdf download file.
    path('product_pdf/', views.ProductListView.as_view(), name='product_list_view'),
    path('pdf/<pk>/', views.product_render_pdf_view, name='product_pdf_view'),

    
    


] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)