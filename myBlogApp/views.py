from django.shortcuts import render,get_object_or_404
from django.http import HttpRequest,HttpResponse
from .models import Post
import datetime
from django.utils import timezone
def home(request):
    posts = Post.objects.filter(published_date__lte= timezone.now()).order_by('published_date')
    return render(request, './home.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})