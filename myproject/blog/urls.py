from django.urls import path

from myproject.blog.apis.Posts import PostApi 
urlpatterns = [
    path('post/', PostApi.as_view(), name='post'),
]
