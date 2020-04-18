"""my_bs_app URL Configuration

"""
from django.urls import path

from .views import PostDetail, PostList

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
