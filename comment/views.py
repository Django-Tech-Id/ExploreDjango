from django.shortcuts import render, redirect

import comment
from .models import Comment
from .form import CommentForm

# Create your views here.
def dashboardComment(request):
    categories = Comment.objects.all()
    context = {'categories': categories}
    return render(request, 'comment/comment.html', context)

def dashboardCommentCreate(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
    return redirect(request.META.get('HTTP_REFERER'))

def dashboardCommentEdit(request, id):
    comment = Comment.objects.get(id=id)
    form = CommentForm(instance=comment)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('dashboard-comment')
    context = {'form': form}
    return render(request, 'comment/comment_form.html', context)

def dashboardCommentDelete(request, id):
    comment = Comment.objects.get(id=id)
    comment.image.delete(save=True)
    comment.delete()

    return redirect('dashboard-comment')