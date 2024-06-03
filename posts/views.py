from django.shortcuts import render, redirect
from . import forms
from . import models
def add_post(request):
    if request.method=="POST":
        PostForm=forms.PostForm(request.POST)
        if PostForm.is_valid():
            PostForm.save()
            return redirect('post')
    else:
        PostForm = forms.PostForm()
    return render(request, 'add_post.html', {'form' : PostForm})  

def edit_post(request,id):
    posts=models.post.objects.get(pk=id)  #filter kora hole jeita dekte chai
    PostForm = forms.PostForm(instance = posts)
    if request.method=="POST":
        PostForm=forms.PostForm(request.POST, instance= posts)
        if PostForm.is_valid():
            PostForm.save()
            return redirect('homepage')
        
    return render(request, 'add_post.html', {'form' : PostForm})

def delete_post(request,id):
     posts=models.post.objects.get(pk=id)
     posts.delete()
     return redirect('homepage')