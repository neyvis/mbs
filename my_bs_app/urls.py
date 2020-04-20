"""my_bs_app URL Configuration

"""
from django.urls import path
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from .views import PostDetail, PostList, login_request, register_request, logout_request


urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('login/', login_request, name='login'),
    path('register/', register_request, name='register'),
    path('logout', logout_request, name='logout'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
