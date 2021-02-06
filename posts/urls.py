from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('blog/', views.blog, name="post-list"),
    path('seatch/', views.search, name="search"),
    path('posts/<id>/', views.posts, name="post-detail")
]
