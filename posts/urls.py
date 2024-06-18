from django.urls import path,include
from . import views

urlpatterns = [
    # path('add/', views.add_post,name='post'),
    path('add/', views.AddPostCreateView.as_view(),name='post'),
    # path('edit/<int:id>', views.edit_post,name='edit'),
    path('edit/<int:id>', views.EditPostView.as_view(),name='edit'),
    # path('delete/<int:id>', views.delete_post,name='delete'),
    path('delete/<int:id>', views.DeletePostView.as_view(),name='delete'),
    path('details/<int:id>', views.DetailPostView.as_view(),name='details'),
]