from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Post
import datetime
from django.utils import timezone
def home(request):
    posts = Post.objects.filter(published_date__lte= timezone.now()).order_by('published_date')
    return render(request, './home.html', {'posts': posts})