from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import markdown2
import markdown

def markdown_to_html(markdownText,images):
    # md = markdown2.Markdown()
    image_ref = ""
    for image in images:
        image_url = settings.MEDIA_URL + image.image.url
        image_ref = "%s\n[%s]: %s" % (image_ref,image,image_url)

    md = "%s\n%s" % (markdownText,image_ref)
    html = markdown2.Markdown(md)

class NewUser(AbstractUser):
    profile = models.CharField('profile',default='',max_length=256)

    def __str__(self):
        return self.username
class Category(models.Model):
    name = models.CharField('Category_name',max_length=256)
    intro = models.TextField('introduction',default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['name']

class Image(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to="image")

    def __str__(self):
        return self.name

class ArticleManager(models.Manager):

     def query_by_category(self,category_id):
         query = self.get_queryset().filter(category_id=category_id)
         return query

     def query_by_time(self):
         query = self.get_queryset().order_by('-pub_date')
         return query

     def query_by_keyword(self,keyword):
         query = self.get_queryset().filter(titel__contains=keyword)
         return query

class Article(models.Model):
    category = models.ForeignKey(Category,blank=True,null=True,verbose_name='belong to')
    title = models.CharField(max_length=256)
    author = models.ForeignKey('Author')
    content = models.TextField('content')
    images = models.ManyToManyField(Image,blank=True)
    pub_date = models.DateTimeField(auto_now_add=True,editable=True)
    update_time = models.DateTimeField(auto_now=True,null=True)
    published = models.BooleanField('notDraft',default=True)
    comment_num = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag',verbose_name='标签',blank=True)

    def __str__(self):
        return self.title

    @property
    def body_html(self):
        return markdown_to_html(self.content,self.images.all())

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'

    objects = ArticleManager()

    def get_markdown(self):
        md = markdown.Markdown(['extra','codehilite'])

        for image in self.images.all():
            image_url = '/blog' + image.image.url
            name = image.name
            md.references[name.lower()] = (image_url,'')

        convert = md.convert(self.content)


        return convert

class Tag(models.Model):
    name = models.CharField('标签名',max_length=20)
    created_time = models.DateTimeField('创建时间',auto_now_add=True)
    update_time = models.DateTimeField('更新时间',auto_now=True, null=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey('NewUser',null=True)
    article = models.ForeignKey(Article,null=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self):
        return self.content

class Author(models.Model):
    name = models.CharField(max_length=256)
    profile = models.CharField('profile',default='',max_length=256)
    password = models.CharField('password',max_length=256)
    register_date = models.DateTimeField(auto_now_add=True,editable=True)

    def __str__(self):
        return self.name

class Train(models.Model):
    train_id = models.CharField('train_id',max_length=256)
    start = models.CharField('start', max_length=256)
    dest = models.CharField('dest', max_length=256)
    time = models.CharField('time', max_length=256)

    def __str__(self):
        return self.id