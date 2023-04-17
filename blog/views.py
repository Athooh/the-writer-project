from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Post
from brand_category.models import Brands
from authors.models import Author
from .models import Comment
from .forms import CommentForm
# from datetime import datetime

# Create your views here.


def blog(request):
    post = Post.objects.order_by('-post_date')
    paginator = Paginator(post, 6)
    page = request.GET.get('page')
    paged_post = paginator.get_page(page)
    brands = Brands.objects.all()
    recent_post = Post.objects.all()[5:10]

    context = {
        'post': paged_post,
        'recent_post': recent_post,
        'brands': brands
    }
    return render(request, 'blog/blog.html', context)


def post(request, post_id):
    authors = Author.objects.all().filter(is_mvp=True)
    post = get_object_or_404(Post, pk=post_id)
    recent_post = Post.objects.all()[5:10]
    comments = post.comments.filter(active=True)
    # template_name = 'post.html'
    new_comment = None

    # comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # create Comment object but dont save to database yet
            new_comment = comment_form.save(commit=False)
            # assign the current post to the comment
            new_comment.post = post
            # save the comment to the database
            new_comment.save()

    else:
        comment_form = CommentForm()

    context = {
        'authors': authors,
        'post': post,
        'recent_post': recent_post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form

    }

    return render(request, 'blog/post.html', context)
