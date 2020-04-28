from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

import datetime

from .models import Post

from .forms import NewUserForm, PostForm


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    #queryset = Post.objects.all()
    context_object_name = 'Post list'
    template_name = 'index.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as {username}")
                print("You are now logged in as {username}")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():

            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect("home")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "register.html",
                          context={"form":form})

    form = NewUserForm
    return render(request = request,
                  template_name = "register.html",
                  context={"form":form})


def create_post(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            status = 0
            created_on = datetime.datetime.now()
            updated_on = datetime.datetime.now()
            post = form.save(commit=False)
            slug = slugify(post.title)
            post.slug = slug
            post.status = status
            post.created_on = created_on
            post.updated_on = updated_on
            post.author = request.user
            post.save()
            # redirect to the post detail page.
            return redirect(reverse('post_detail', kwargs={'slug': slug}))
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def my_posts(request):
    user = request.user
    posts_list = Post.objects.filter(author_id=user).order_by('-created_on')

    return render(request = request,
                  template_name = "my_posts.html",
                  context={"posts_list":posts_list})

def about(request):
    return render(request=request,
                  template_name="about.html",
                  )


