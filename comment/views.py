from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from .models import Comment

# Create your views here.
def update_comment(request):
    user = request.user

    text = request.POST.get('text','')
    if text =='':
        return render(request, 'error.html',{'messgae':'评论内容为空'})

    comment_type = request.POST.get('content_type','')
    object_id = int(request.POST.get('object_id',''))

    model_class = ContentType.objects.get(model=comment_type).model_class()
    model_obj = model_class.objects.get(pk=object_id)

    comment= Comment()
    comment.user = user
    comment.text = text

    comment.content_object =model_obj
    comment.save()

    # 评论后回到原来页面

    referer = request.META.get('HTTP_REFERER',reverse('home'))
    return redirect(referer)