from django.shortcuts import render, redirect
from .models import Post
from .form import PostForm
from comment.models import Comment
from comment.form import CommentForm

# Create your views here.
def dashboardPost(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'post/post.html', context)

def dashboardPostCreate(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard-post')
    context = {'form': form}
    return render(request, 'post/post_form.html', context)

def dashboardPostEdit(request, id):
    post = Post.objects.get(id=id)
    comments = post.comments.all()
    form = PostForm(instance=post)
    commentForm = CommentForm(initial={'post': post.id})
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('dashboard-post')
    context = {'form': form, 'comments': comments, 'commentform': commentForm}
    return render(request, 'post/post_form.html', context)

def dashboardPostDelete(request, id):
    post = Post.objects.get(id=id)
    print(post)
    post.image.delete(save=True)
    post.delete()

    return redirect('dashboard-post')