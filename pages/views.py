from django.shortcuts import  render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from blog.models import Post
from authors.models import Author

# Create your views here.
def index(request):
    post = Post.objects.order_by('-post_date')[:1]
    authors = Author.objects.all().filter(is_mvp=True)
    recent_post = Post.objects.all()[:5]
    
    context = {
        'post' : post,
        'authors' : authors,
        'recent_post' : recent_post
    }
    return render(request, 'pages/index.html', context)

def about(request):
    authors = Author.objects.all()[:3]
    context = {
        'authors' : authors
    }
    return render(request, 'pages/about.html', context) 
