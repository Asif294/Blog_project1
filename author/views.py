from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from . import forms
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import post
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import View
def register(request):
    if request.method=='POST':
        form=forms.RegistationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Accounnt created successfully')
            return redirect('userlogin')
    else:
        form=forms.RegistationForm()
    return render(request,'register.html',{'form':form,'type':'Register'})

def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, 'Logged in Successfully')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Login informtion incorrect')
                return redirect('register')
        else:
            messages.warning(request, 'Invalid login form data')
            return render(request, 'register.html', {'form': form, 'type': 'Login'})
    else:
        form = AuthenticationForm()
        return render(request, 'register.html', {'form' : form, 'type' : 'Login'})
    

class userloginview(LoginView):
    template_name='register.html'
    

    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request,'Login Successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request,'Invalid Login Information')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
        
    

class LogoutV(View):
    def get(self,request):
        logout(request)
        redirect('userlogin')

    

@login_required
def profile(request):
    data=post.objects.filter(author=request.user)
    return render(request,'profile.html',{'data':data})
@login_required
def edit_profile(request):
    if request.method=="POST":
        form=forms.changeuserdata (request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'profile Updated successfully')
            return redirect('profile')
    else:
        form=forms.changeuserdata(instance=request.user)
    return render(request,'update_profile.html',{'form':form,})

def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'password.html', {'form' : form})

def user_logout(request):
    logout(request)
    return redirect('userlogin')

