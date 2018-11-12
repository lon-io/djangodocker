from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/create', views.create_post, name='create_post'),
    path('posts/edit/<int:post_id>', views.edit_post, name='edit_post'),
    path('posts/update/<int:post_id>', views.update_post, name='edit_post'),
    path('posts/<int:post_id>', views.post, name='post'),
]
