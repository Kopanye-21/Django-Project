

# Create your views here.
from django.shortcuts import render, redirect
from .models import Post

def home(request):
   
    return render(request, 'home.html', )

def test_posts(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        return redirect('home')
    return render(request, 'test_posts.html')