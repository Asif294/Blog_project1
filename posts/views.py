from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
@login_required
def add_post(request):
    if request.method == 'POST': 
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid(): 
            post_form.instance.author = request.user
            post_form.save() 
            return redirect('profile') 
    else: 
        post_form = forms.PostForm()
    return render(request, 'add_post.html', {'form' : post_form}) 

@method_decorator(login_required,name='dispatch')
class AddPostCreateView(CreateView):
    model=models.post
    form_class=forms.PostForm
    template_name='add_post.html'
    success_url=reverse_lazy('profile')
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

@login_required
def edit_post(request,id):
    posts=models.post.objects.get(pk=id)  
    PostForm = forms.PostForm(instance = posts)
    if request.method=="POST":
        PostForm=forms.PostForm(request.POST, instance= posts)
        if PostForm.is_valid():
            PostForm.instance.author = request.user
            PostForm.save()
            return redirect('profile')
        
    return render(request, 'add_post.html', {'form' : PostForm})

@method_decorator(login_required,name='dispatch')
class EditPostView(UpdateView):
    model=models.post
    form_class=forms.PostForm
    template_name='add_post.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('profile')



@login_required
def delete_post(request,id):
     posts=models.post.objects.get(pk=id)
     posts.delete()
     return redirect('homepage')

@method_decorator(login_required,name='dispatch')
class DeletePostView(DeleteView):
    model=models.post
    template_name='delete.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('profile')

class DetailPostView(DetailView):
    model = models.post
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'

    def post(self,request,*args,**kwargs):
        comment_form = forms.commentForm(data=self.request.POST)
        post=self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        
      
            
        comment_form = forms.commentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context


       

    
