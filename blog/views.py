from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Post
from brand_category.models import Brands
from authors.models import Author

# Create your views here.
def blog(request):
    post = Post.objects.order_by('-post_date')
    paginator = Paginator(post, 6)
    page = request.GET.get('page')
    paged_post = paginator.get_page(page)
    brands = Brands.objects.all()
    recent_post = Post.objects.all()[5:10]
    
    context = {
        'post' : paged_post,
        'recent_post' : recent_post,
        'brands': brands
    }
    return render(request, 'blog/blog.html', context) 

def post(request, post_id):
    authors = Author.objects.all().filter(is_mvp=True)
    post = get_object_or_404(Post, pk=post_id)
    recent_post = Post.objects.all()[5:10]
   
    context = {
        'authors' : authors,
        'post' : post,
        'recent_post' : recent_post
        
        
    }
    return render(request, 'blog/post.html', context)