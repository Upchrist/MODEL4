from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, ProfileUpdateForm
from .models import UserProfile
from home.models import  Setting, Brand
from product.models import Product, Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def index(request):
    setting= Setting.objects.get(pk=1)
    profile= UserProfile.objects.get(user__username = request.user.username)
    offer = Product.objects.get(offer=True)

    context = {
        'setting': setting,
        'profile': profile,
        'offer': offer
    }
    return render(request, 'userprofile.html', context)
    # return HttpResponse('Hello World user app installed')
    
def accountform(request):
    setting= Setting.objects.get(pk=1)
    banner = Product.objects.get(banner=True)


    context = {
        'setting': setting,
        'banner': banner
    }
    return render(request, 'accountform.html', context)

def loginform(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')

        else:
            messages.info(request,'Invalid username/password')

    setting= Setting.objects.get(pk=1)
    banner = Product.objects.get(banner=True)

    context = {
        'setting': setting,
        'banner': banner
    }

    return render(request,'accountform.html', context)


def logoutfunc(request):
    logout(request)
    return redirect('loginform')

def registerForm(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            myuser = form.save()
            p = UserProfile(user=myuser)
            p.first_name = myuser.first_name
            p.last_name = myuser.last_name
            p.save()
            login(request,myuser)
            return redirect('index')
        else:
            messages.warning(request,form.errors)
            return redirect('registerform')

    setting= Setting.objects.get(pk=1)
    banner = Product.objects.get(banner=True)


    context = {
        'form':form,
        'setting': setting,
        'banner': banner   
    }

    return render(request, 'accountform.html', context)




@login_required(login_url='/login')
def userupdate(request):
    if request.method == 'POST':
        profileform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        profileform.save()
        messages.success(request, 'Your Account has been updated')
        return redirect('user')

    else:
        profileform = ProfileUpdateForm(instance=request.user.userprofile)
        setting= Setting.objects.get(pk=1)
        category= Category.objects.all()
        offer= Product.objects.get(offer=True)
        profile = UserProfile.objects.filter(user_id=request.user.id).offer()


        context = {
            'profileform': profileform,
            'setting': setting,
            'category': category,
            'offer': offer
        }

    return render(request, 'userupdate.html', context)


@login_required(login_url='/login')
def userpassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request,'Your password was successfully updated!')
            return redirect('user')

        else:
            messages.error(request, 'Please correct the error below.<br>' + str(form.errors))
            return redirect('userpassword')
    else:
        form = PasswordChangeForm(request.user)
        setting= Setting.objects.get(pk=1)
        category=Category.objects.all()
        profile = UserProfile.objects.filter(user__username = request.user.username).first()
        offer = Product.objects.get(offer=True)


        context = {
            'form': form,
            'setting': setting,
            'category': category,
            'profile': profile,
            'offer': offer
        }

    return render(request, 'username.html', context)

