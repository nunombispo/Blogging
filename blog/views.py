from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .forms import PostForm  # We'll create this form next
from django.contrib import messages


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})


@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    # Ensure the logged-in user is the author of the post
    if request.user == post.author:
        post.delete()
        messages.success(request, "Post deleted successfully!")
        return redirect('post_list')
    else:
        messages.error(request, "You don't have permission to delete this post.")
        return redirect('post_detail', slug=post.slug)