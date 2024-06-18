from django.shortcuts import render
from posts.models import post
from categories.models import category
def home(request ,category_slug=None):
    data=post.objects.all()
    if category_slug is not None:
        categorya=category.objects.get(slug=category_slug)
        data=post.objects.filter(category=categorya)
    categorys=category.objects.all()
    return render(request,'home.html',{'data':data , 'category':categorys})