from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Category
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'forum/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    return render(request, 'forum/post_detail.html', {'post': post, 'comments': comments})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author == request.user:
        post.delete()
        return redirect('post_list')
    else:
        return render(request, 'forum/error.html', {'message': 'Du kannst nur deine eigenen Beiträge löschen!'})

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
    return render(request, 'forum/create_post.html', {'form': form})