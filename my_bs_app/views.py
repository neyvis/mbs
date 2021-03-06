from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post
from .forms import NewUserForm, PostForm


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    context_object_name = 'Post list'
    template_name = 'index.html'
    paginate_by = 4

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
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()

    return render(
        request=request,
        template_name="login.html",
        context={"form": form}
    )


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("home")
        else:
            return render(
                request=request,
                template_name="register.html",
                context={"form": form}
            )

    form = NewUserForm
    return render(
        request=request,
        template_name="register.html",
        context={"form": form}
    )


def create_post(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=True)
            post.author = request.user
            post.save()
            # redirect to the post detail page.
            return redirect(reverse('post_detail', kwargs={'slug': post.slug}))
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def my_posts(request):
    user = request.user
    posts = Post.objects.filter(author_id=user).order_by('-created_on')
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 4)
    try:
        posts_list = paginator.page(page)
    except PageNotAnInteger:
        posts_list = paginator.page(1)
    except EmptyPage:
        posts_list = paginator.page(paginator.num_pages)

    return render(
        request=request,
        template_name="my_posts.html",
        context={"posts_list": posts_list}
    )


def about(request):
    return render(
        request=request,
        template_name="about.html",
    )
