from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from . models import User, Store
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import authenticate, login, logout

from .forms import UserForm, StoreForm


# Create your views here.

class UserListView(ListView):
    model = User
    template_name = 'user_temp/main.html'

def users_render_pdf_view(request, *args, **kwargs):
   pk = kwargs.get('pk')
   user = get_object_or_404(User, pk=pk)

   template_path = 'user_temp/generate_pdf.html'
   context = {'user': user}
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
   pisa_status = pisa.CreatePDF(
      html, dest=response)
   # if error then show some funy view
   if pisa_status.err:
      return HttpResponse('We had some errors <pre>' + html + '</pre>')
   return response



def createUser(request):
   sent = False
   if request.method == "POST":
      form = UserForm(request.POST)
      if form.is_valid():
         form.save()
         sent = True
   form = UserForm()
   return render(request, 'user_temp/user_create.html', {'form': form})


# from django.contrib.auth.models import Group
# from django.contrib.auth.decorators import permission_required, user_passes_test

# @user_passes_test(lambda u: Group.objects.get(name='Manager') in u.groups.all())
# def dashboard(request):
#    form = StoreForm()
#    if request.method == 'POST':
#       form = StoreForm(request.POST)
#       if form.is_valid():
#          form.save()
#          # return HttpResponse("Store Created Successfully !!!!!")
#    # return render(request, 'user_temp/create_store.html', {'form' : form})
#    return render(request, 'accounts/create_store.html', {'form' : form})

# # @user_passes_test(lambda u: Group.objects.get(name='Manager') in u.groups.all())
# from django.contrib.auth.decorators import permission_required

# @user_passes_test(lambda u: Group.objects.get(name='Customer') in u.groups.all(), login_url='user1/login/')
# def view_store(request):
#    if request.user.is_authenticate and user.has_perm("store.see_store"):
#       view_store = Store.objects.all()
#       context = {
#          'view_store': view_store,
#       }
#       return render(request, 'user_temp/viewStore.html', context)
#    else:
#       return redirect('Userlogin')

# def userlogin(request):
#     if not request.user.is_authenticated :
#     # form = AuthenticationForm()
#         if request.method == 'POST':
#             form = AuthenticationForm(request=request, data=request.POST)
#             if form.is_valid():
#                username = form.cleaned_data.get('username')
#                password = form.cleaned_data.get('password')
#                user = authenticate(username=username, password=password)
#                if user is not None:
#                   login(request, user)
#                   print(user)
#                   # messages.success(request, 'Logged In Successfully...')
#                   return redirect("dashboard")
#         else:
#             # messages.info(request, f'account done not exit plz sign in')
#             form = AuthenticationForm()
#             # messages.error(request, 'Log-In Unuccessfully...')
            
#       #   return render(request, 'user_temp/userlogin.html', {'form': form})
#         return render(request, 'accounts/login.html')
#     else:
#         return redirect('dashboard')
      
# def userlogout_request(request):
#    logout(request)
#    return redirect('Userlogin')

