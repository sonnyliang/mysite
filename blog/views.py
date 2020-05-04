from django.shortcuts import render, get_object_or_404
from .models import Blog, BlogType
from django.contrib.contenttypes.models import ContentType
from comment.models import Comment

# Create your views here.
def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    return render(request,'blog/blog_list.html', context)

def blog_detail(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    context={}
    context['blog']=get_object_or_404(Blog, pk=blog_pk)

    context['user'] = request.user

    blog_content_type = ContentType.objects.get_for_model(blog)
    comments = Comment.objects.filter(content_type = blog_content_type, object_id = blog.pk)
    context['comments'] = comments 

    return render(request,'blog/blog_detail.html',context)

def blogs_with_type(request, blog_type_pk):
    context={} 
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)  
    context['blogs']= Blog.objects.all().filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    return render(request,'blog/blogs_with_type.html', context)

