from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User,AbstractUser
from tinymce.models import HTMLField
from tinymce import models as tinymce_models
from uuslug import slugify
#


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title",'timestamp')
from django.db import models

# Create your models here.
class superuser(AbstractUser):
    # user= models.OneToOneField(User,on_delete=models.CASCADE)
    # username = models.CharField(max_length=500)
    password = models.CharField(max_length=50)
    sighs = models.IntegerField(default=0)
    date = models.IntegerField(default=11)
    cha = models.CharField(max_length=100, default="hllo")
    touxiang = models.FileField(upload_to = 'touxiang/',default="touxiang/5.jpg")



class diary(models.Model):
    diary_txt = tinymce_models.HTMLField(max_length=100, default="hllo")
    title = models.CharField(max_length=100, default="hllo")
    user = models.ForeignKey(superuser,on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    kind = models.CharField(max_length=100, default="hllo")
    slug = models.SlugField(default = 0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(diary, self).save(*args, **kwargs)

class comment(models.Model):
    comment = models.CharField(max_length=100, default="hllo")
    user = models.ForeignKey(diary,on_delete=models.CASCADE)

class IMG(models.Model):
    user = models.ForeignKey(superuser,on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    img = models.FileField(upload_to = 'upload/',null=True,default="touxiang/5.jpg" )
