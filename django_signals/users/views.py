from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from django.contrib import messages

from .forms import RegisterNewUser, EditUserProfileForm, EditAdminProfileForm
from .models import UserProfile

from django.db.models import Q

# Create your views here.

# Here we check user type means, superuser, staff, active.
# def userlogin(request):
#     if not request.user.is_authenticated :
#         if request.method == 'POST':
#             form = AuthenticationForm(request=request, data=request.POST)
#             if form.is_valid():
#                 username = form.cleaned_data.get('username')
#                 password = form.cleaned_data.get('password')
#                 user = authenticate(username=username, password=password)
#                 if user is not None:
#                     login(request, user)
#                     if request.user.is_superuser:
#                         return redirect("product")
#                     elif request.user.is_staff and request.user.is_active:
#                         return HttpResponse("You are not a super user.")
#                     else:
#                         pass
#                 else:
#                     pass
#             else:
#                 print(form.errors)
#         else:
#             form = AuthenticationForm()
#         return render(request, 'users/userlogin.html', {'form': form})
#     else:
#         return redirect('product')

def userlogin(request):
    if not request.user.is_authenticated:
    # form = AuthenticationForm()
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    # print(user)
                    # messages.success(request, 'Logged In Successfully...')
                    return redirect("product")
                else:
                    pass
            else:
                print(form.errors)
        else:
            # messages.info(request, f'account done not exit plz sign in')
            form = AuthenticationForm()
            # messages.error(request, 'Log-In Unuccessfully...')            
        return render(request, 'users/userlogin.html', {'form': form})
    else:
        return redirect('product')

def userlogout(request):
    logout(request)
    return redirect('userlogin')


def profile(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            # form = EditAdminProfileForm(instance=request.user)
            if request.method == 'POST':
                form = EditAdminProfileForm(request.POST, instance=request.user)
                if form.is_valid():
                    form.save()
            else:
                form = EditAdminProfileForm(instance=request.user)
            context = {
                'form': form,
            }
            return render(request, 'users/admindashboard.html', context)
        else:
            form = EditUserProfileForm(instance=request.user)
            if request.method == 'POST':
                form = EditUserProfileForm(request.POST, instance=request.user)
                if form.is_valid():
                    form.save()
            else:
                form = EditUserProfileForm(instance=request.user)
            context = {
                'form': form,
            }
            return render(request, 'users/userdashboard.html', { 'form': form })
    else:
        return redirect('userlogin')
        # del request.session['user_data']

# here we see all user
def alluser(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        if request.user.is_superuser:
           form = EditAdminProfileForm(instance=request.user)
        elif request.user.is_staff and request.user.is_active:
            form = EditUserProfileForm(instance=request.user)
        form = EditUserProfileForm(instance=request.user)
        context = {
            'users': users,
            'form': form,
        }
        return render(request, 'users/show_alluser.html', context)
    else:
        return redirect('userlogin')


def user_register(request):
    form = RegisterNewUser()
    if request.method == "POST" and request.FILES:
        form = RegisterNewUser(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = UserProfile.objects.filter(username=username).exists()
            return username
            # return messages.success(request, "User Created Successfully..")
    context = {
        'form': form
    }        
    return render(request, 'users/register_user.html', context)

def sort_user(request):
    sort_data = User.objects.order_by('-id')
    return redirect('showuser')
    # print(sort_data)
    # return sort_data
    # ContactModel.objects.all().order_by('-id')

def search_user(request):    
    if request.user.is_authenticated:
        if request.method == 'POST':
            username_search = request.POST.get('username_search')
            email_search = request.POST.get('email_search')
            firstname_search = request.POST.get('firstname_search')
            lastname_search = request.POST.get('lastname_search')
            if username_search:
                # username_search_res = User.objects.filter(Q(username__icontains=username_search) | Q(email_search_contains=email_search))
                username_search_res = User.objects.filter(username__icontains=username_search)
                return render(request, 'users/show_alluser.html', {'users': username_search_res})
            elif email_search :
                email_search_res = User.objects.filter(email__contains=email_search)
                return render(request, 'users/show_alluser.html', {'users': email_search_res})
            elif firstname_search :
                firstname_search_res = User.objects.filter(first_name__contains=firstname_search)
                return render(request, 'users/show_alluser.html', {'users': firstname_search_res})
            elif lastname_search :
                lastname_search_res = User.objects.filter(last_name__contains=lastname_search)
                return render(request, 'users/show_alluser.html', {'users': lastname_search_res})
            else:
                pass
        else:
                users = User.objects.all()
                return render(request, 'users/show_alluser.html', {'users': users})
    else:
        return redirect('userlogin')

def userdata(request):
    users = User.objects.all()
    
    return render(request, 'users/select_data.html')