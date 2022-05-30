from django.db import models
from django.contrib.auth.models import AbstractUser
import os

# Create your models here.


class Users(AbstractUser):
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=10)
    is_private = models.BooleanField(default=False)
    bio = models.CharField(max_length=100,blank=True,null=True)
    website = models.URLField(blank=True,null=True)
    img = models.ImageField(blank= True,null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class LikePost(models.Model):
    username = models.ForeignKey(Users,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class CommentPost(models.Model):
    username = models.ForeignKey(Users,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class SharePost(models.Model):
    username = models.ForeignKey(Users,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    def get_upload_path(instance, filename):
        return "Gopipatwa/05062022/"
        # print(instance.update_date.strftime("%B-%d-%Y")str(f"{instance.userid}/{instance.upload_date.strftime('%B-%d-%Y')}/"))
    
    userid = models.ForeignKey(Users,to_field="username",on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    # print("_+++++++++++++++++++++++++++++++++++++++++++++++++++++",upload_date,[i for i in update_date])
    desc = models.TextField(blank=True,null=True)
    tags = models.TextField(blank=True,null=True)
    img_post = models.ImageField(upload_to = get_upload_path)
    like_post = models.ManyToManyField(LikePost,blank=True,null=True)
    comment_post = models.ManyToManyField(CommentPost,blank=True,null=True)
    share_post = models.ManyToManyField(SharePost,blank=True,null=True)


    