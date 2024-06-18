from django.db import models
from categories.models import category
from django.contrib.auth.models import User
class post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    category=models.ManyToManyField(category)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='posts/media/uploads/',blank=True,null=True)
    def __str__(self):
        return self.title

class comment(models.Model):
    post=models.ForeignKey(post,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=100)
    email=models.EmailField()
    body=models.TextField()
    create_on=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"comment by {self.name}"
    
        
    
        class Meta:
            abstract = True
    