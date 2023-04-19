from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField
from taggit.managers import TaggableManager
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = slug = models.SlugField(max_length=400, unique=True, blank=True)

    def __str__(self):
        return self.user.get_username()

    @property
    def num_posts(self):
        return Post.objects.filter(user=self).count()
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.get_username())
        super(Author, self).save(*args, **kwargs)

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    description = models.TextField(default="description")

    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return self.title
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("posts", kwargs={
            "slug":self.slug
        })

    @property
    def num_posts(self):
        return Post.objects.filter(categories=self).count()
    
    @property
    def last_post(self):
        return Post.objects.filter(categories=self).latest("date")


class Reply(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:100]

    class Meta:
        verbose_name_plural = "replies"


class Comment(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    replies = models.ManyToManyField(Reply, blank=True)

    def __str__(self):
        return self.content[:100]


class Post(models.Model):
    title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = HTMLField()
    categories = models.ManyToManyField(Category)
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    tags = TaggableManager()
    comments = models.ManyToManyField(Comment, blank=True)
    closed = models.BooleanField(default=False)
    state = models.CharField(max_length=40, default="zero")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse("detail", kwargs={
            "slug":self.slug
        })

    @property
    def num_comments(self):
        return self.comments.count()

    @property
    def last_reply(self):
        return self.comments.latest("date")

    