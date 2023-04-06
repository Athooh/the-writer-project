from django.shortcuts import  render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Gallary, Gallary2
from blog.models import Post

# Create your views here.
def gallary(request):
    gallary = Gallary.objects.all()[1:5]
    gallary2 = Gallary2.objects.all()[0:4]
    main_photo = Gallary.objects.all()[:1]
    main_photo1 = Gallary2.objects.all()[4:5]
    recent_post = Post.objects.all()[:5]
    context = {
        'gallary': gallary,
        'gallary2': gallary2,
        'main_photo': main_photo,
        'main_photo1': main_photo1,
        'recent_post': recent_post
    }
    return render(request, 'gallary/gallary.html', context)


