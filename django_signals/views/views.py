from django.shortcuts import render, redirect
from .models import Product, Order, Category
from .forms import ProductForm, OrderForm, CategoryForm
from django.http import HttpResponse

from django.core.exceptions import *

from django.db.models import Count
from django.db.models import F

# this is used for apply a cache perview in project.
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import os
# from fpdf import FPDF
import csv
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView


# Create your views here.

def index(request):
    # questions = Question.objects.annotate(number_of_answers=Count('answer'))
    # products = Product.objects.annotate(number_of_product=Count('pname'))
        # print(products.count())
    return render(request, 'core/product_show.html')


# @cache_page(60 * 15)
def product(request):
    if request.user.is_authenticated:
        products = Product.objects.all().order_by('p_id')
        elc_prods = Product.objects.filter(category__cname="Electronic").order_by('p_id')
        pd = Product.objects.filter(pname__endswith="Shirts").annotate(num_clothe=Count('category'))
        categories = Category.objects.all()
        page = request.GET.get('page', 2)
        paginator = Paginator(products, 2)
        try:
            all_prods = paginator.page(page)
        except PageNotAnInteger:
            all_prods = paginator.page(1)
        except EmptyPage:
            all_prods = paginator.page(paginator.num_pages)
        context = {
                'products':products ,
                'categories': categories,
                'pd': pd,
                'all_prods': all_prods,
                'elc_prods': elc_prods
            }
        return render(request, 'core/product_show.html', context)
        # return render(request, 'core/tableshow.html', context)
    else:
        return redirect('userlogin')

# here we do all action in product
# @cache_page(60 * 15)
@cache_page(60)
def productform(request):
    if request.user.is_authenticated:
        form = ProductForm()
        if request.method == "POST" and request.FILES:
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {
            'form': form,
        }
        return render(request, 'core/product_form.html', context)
    else:
        return redirect('userlogin')

def productedit(request, id):
    if request.user.is_authenticated:
        product = Product.objects.get(p_id=id)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            # here we delete the old uploaded image
            image_path = product.image.path
            if os.path.exists(image_path):
                os.remove(image_path)
            form.save()
            return redirect('product')
        context = {
            'product': product,
            'form': form
        }
        return render(request, 'core/edit_prodect.html', context)
    else:
        return redirect('userlogin')
    
def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('product')

# here we do all action in category

# @cache_page(60)
def addcategories(request):
    if request.user.is_authenticated:
        all_categories = Category.objects.all()
        form = CategoryForm()
        # print(Category.category_full_name)
        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('add_category')
        context = {
            'form': form,
            'all_categories': all_categories,
        }
        return render(request, 'core/category_form.html', context)
    else:
        return redirect('userlogin')


def edit_category(request, id):
    if request.user.is_authenticated:
        category = Category.objects.get(cat_id = id)
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('add_category')
        context = {
            'form': form,
            'category': category,
        }
        return render(request, 'core/edit_category.html', context)
    else:
        return redirect('userlogin')

def delete_category(request, cat_id):
    if request.user.is_authenticated:
        category_delete = Category.objects.get(cat_id=cat_id)
        category_delete.delete()
        return redirect('add_category')
    else:
        return redirect('userlogin')

# fetch the data from database in csv format.
def getfile(request): 
    if request.user.is_authenticated:
        response = HttpResponse(content_type='text/csv')  
        response['Content-Disposition'] = 'attachment; filename="product.csv"'  
        products = Product.objects.all()  
        writer = csv.writer(response)  
        for product in products:  
            writer.writerow([product.p_id,product.category,product.pname,product.ptitle, product.quantity,product.image])  
        return response
    else:
        return redirect('userlogin')


# Here we create function for generate a report in pdf format.

# from . models import User

class ProductListView(ListView):
    model = Product
    template_name = 'core/main.html'

def product_render_pdf_view(request, *args, **kwargs):
   pk = kwargs.get('pk')
   product = get_object_or_404(Product, pk=pk)

   template_path = 'core/generate_pdf.html'
   context = {
       'product': product,
    #    'url': static('images/black.jpeg')
    }

   # Create a Django response object, and specify content_type as pdf
   response = HttpResponse(content_type='application/pdf')

   # to directly download the pdf we need attachment 
   # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

   # to view on browser we can remove attachment 
   response['Content-Disposition'] = 'filename="report.pdf"'

   # find the template and render it.
   template = get_template(template_path)
   html = template.render(context)

   # create a pdf
   pisa_status = pisa.CreatePDF(html, dest=response)
   # if error then show some funy view
   if pisa_status.err:
      return HttpResponse('We had some errors <pre>' + html + '</pre>')
   return response

# this function is used for showing data in normal user window

def all_product(request):
    # product_list = Product.objects.all().order_by('p_id')
    # UnorderedObjectListWarning: Pagination may yield inconsistent results with an unordered object_list: <class 'dashb.models.Product'> QuerySet.
    # solutions
    product_list = Product.objects.all().order_by('p_id')
    # return render(request, 'core/tableshow.html', context)
    # product_list = Product.objects.filter(category__cname="Clothes").order_by('p_id')
    # product_list = Product.objects.filter().order_by('p_id')
    # pd = Product.objects.filter(category="").annotate(num_clothe=Count('category'))
    page = request.GET.get('page', 2)
    paginator = Paginator(product_list, 2)
    try:
        prod = paginator.page(page)
    except PageNotAnInteger:
        prod = paginator.page(1)
    except EmptyPage:
        prod = paginator.page(paginator.num_pages)
    context = {
                'prod': prod,
        }
    # return render(request, 'core/paginations.html', context)
    return render(request, 'core/tableshow.html', context)
    # return render(request, 'core/allproducts_data.html', context)

# now here we show the data category-wise
def categorywiseProduct(request):
    elc_prods = Product.objects.filter(category__cname="Electronic").order_by('p_id')
    print(elc_prods)
    page = request.GET.get('page', 2)
    paginator = Paginator(elc_prods, 2)
    try:
        elc_prods = paginator.page(page)
    except PageNotAnInteger:
        elc_prods = paginator.page(1)
    except EmptyPage:
        elc_prods = paginator.page(paginator.num_pages)
    context = {
                'elc_prods':elc_prods,
            }
    # return redirect('product', context)
    # return render(request, 'core/electronic.html', context)
    return render(request, 'core/allproducts_data.html', context)


# here we create a function for show all peoduct data in graph.
from .utils import get_plot

def viewProduct(request):
    qs = Product.objects.all()
    x = [x.ptitle for x in qs]
    y = [y.price for y in qs]
    chart = get_plot(x,y)
    context = {
        'chart': chart,
    }
    return render(request, 'core/main_chart.html',context)

# here we search the product and category.
def search_product(request):
    if request.method == "POST":
        product_search = Product.objects.get('ptitle')
        if product_search:
            product_search = Product.objects.filter(ptitle__icontains=product_search)
            context = {
                'product_search': product_search,
            }
            return render(request, 'core/search_product.html', context)
        else:
            return render(request, 'core/product_form.html')
    else:
        return render(request, 'core/product_form.html')
    # pass product_search



# search and show all category here.
def search_category(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            cate_search = request.POST.get('cate_search')
            cate_search_res = Category.objects.filter(cate_name__icontains=cate_search)
            return render(request, 'category/allcategory.html', {'categories': cate_search_res})
        else:
            all_categories = Category.objects.all()
            return render(request, 'category/allcategory.html', {'categories': all_categories})
    else:
        return redirect('userlogin')

# add category here.   
def addcategory(request):
    if request.user.is_authenticated:
        # form = CategoryForm()
        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('showcategory')
        else:
            form = CategoryForm()
        context = {
            'form': form,
        }
        return render(request, 'category/addcategory.html', context)
    else:
        return redirect('userlogin')


def edit_category(request, id):
    if request.user.is_authenticated:
        category = Category.objects.get(cat_id = id)
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('add_category')
        context = {
            'form': form,
            'category': category,
        }
        return render(request, 'category/updatecategory.html', context)
    else:
        return redirect('userlogin')

def delete_category(request, cat_id):
    if request.user.is_authenticated:
        category_delete = Category.objects.get(cat_id=cat_id)
        category_delete.delete()
        return redirect('add_category')
    else:
        return redirect('userlogin')