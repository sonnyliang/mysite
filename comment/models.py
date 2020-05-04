from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


# Create your models here.
class Comment(models.Model):

    # 评论对象
    content_type=models.ForeignKey(ContentType, on_delete = models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # 评论内容
    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)

    # 评论用户
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)

    class Meta:
        ordering=['-comment_time']