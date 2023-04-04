from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Post

# Create your views here.
def blog(request):
    post = Post.objects.order_by('-post_date')
    
    paginator = Paginator(post, 6)
    page = request.GET.get('page')
    paged_post = paginator.get_page(page)
    
    recent_post = Post.objects.all()[:4]
    context = {
        'post' : paged_post,
        'recent_post' : recent_post
    }
    return render(request, 'blog/blog.html', context) 

def post(request, post_id):
    return render(request, 'blog/post.html')