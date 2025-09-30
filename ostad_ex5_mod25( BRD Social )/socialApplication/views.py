from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from . import forms,models

# Create your views here.
def custom_login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method =='POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        validate_user = authenticate(username=username, password=password)
        if validate_user is not None:
            login(request, validate_user)
            messages.success(request, 'login successfull')
            return redirect('home')
        else:
            messages.error(request, 'Wrong User details')
            return redirect('login')
    return render(request, 'login.html', {})
    # return render(request, 'login.html', {'form': form})

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if len(password)<3:
            messages.error(request, 'Password must be at least 3 characters')
            return redirect('register')
        elif password!=confirm_password:
            messages.error(request, 'Password did not matched')
            return redirect('register')
        get_all_users_by_username = User.objects.filter(username=username)
        if get_all_users_by_username:
            messages.error(request,'Username already exists')
            return redirect('register')
        
        new_user = User.objects.create_user(username=username, email=email, password=password,confirm_password=confirm_password)
        new_user.save()
        messages.success(request, 'User created successfully')
        return redirect('login')
    return render(request, 'register.html', {})

def Logout(request):
    logout(request)
    messages.info(request, 'You are logged out')
    return redirect('login')
  
# @login_required
def home(request):
    posts = models.addPost.objects.order_by('-created_at')
    return render(request, 'posts.html', {'posts': posts})

def profile(request):
    posts = models.addPost.objects.filter(user = request.user)
    return render(request, 'profile.html', {'userposts': posts})

@login_required
def create(request):
    if request.method == 'POST':
        form = forms.AddPostForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, "Post created successfully.")
            return redirect('home')
    else:
        form = forms.AddPostForm()
        return render(request, 'create.html', {'form': form})

@login_required(login_url='custom login')
def edit(request,id):
    editPost = models.addPost.objects.get(id = id)
    if request.method == 'POST':
        postForm = forms.AddPostForm(request.POST,request.FILES,instance=editPost)
        if postForm.is_valid():
            instance1 = postForm.save(commit=False)
            instance1.user = request.user
            instance1.save()
            messages.success(request, "Post updated successfully.")
            return redirect('profile')
    else:
        postForm = forms.AddPostForm(instance=editPost)
    return render(request, 'editPost.html', {'postForm': postForm, 'edit': True})        

@login_required(login_url='custom login')
def delete(request,id):
    deletePost = models.addPost.objects.get(id = id)
    deletePost.delete()   
    messages.success(request, "Post deleted successfully.")
    return redirect('profile')

 