from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget

from .models import Post
from . import constants


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ("title", "image", "content")
        widgets = {
            'content': SummernoteWidget(),
        }

    def save(self, commit=True):
        post = super(PostForm, self).save(commit=False)
        post.status = constants.STATUS_DRAFT

        return post
