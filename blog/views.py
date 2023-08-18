from django.shortcuts import render
from .models import Post
posts = [
        {
            'author': 'Jacob B',
            'title': 'My First Blog Post',
            'content': 'First post content',
            'date_posted': 'August 27, 2018'
        },
             {
            'author': 'Jacob B',
            'title': 'My Second Blog Post',
            'content': 'Second  post content',
            'date_posted': 'August 27, 2018'
        }
        ]


def home(request):
    context = {
        'posts': Post.objects.all()        
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
