from django.shortcuts import  render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from blog.models import Post
from authors.models import Author
from brand_category.models  import Brands

# Create your views here.
def index(request):
    post = Post.objects.order_by('-post_date')[:1]
    authors = Author.objects.all().filter(is_mvp=True)
    recent_post = Post.objects.all()[5:10]
    brands = Brands.objects.all()
    
    context = {
        'post' : post,
        'authors' : authors,
        'recent_post' : recent_post,
        'brands': brands
    }
    return render(request, 'pages/index.html', context)

def about(request):
    authors = Author.objects.all()[:3]
    recent_post = Post.objects.all()[5:10]
    num_posts = Post.objects.all().count()
    authors_count = Author.objects.all().count()
    
    context = {
        'authors' : authors,
        'recent_post' : recent_post,
        'num_posts' : num_posts,
        'authors_count' : authors_count
    }
    return render(request, 'pages/about.html', context) 
