from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    author = models.ForeignKey('Author',on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    content = models.TextField()
    description = models.TextField()
    min_to_read = models.DateTimeField()
    tag = models.ManyToManyField(Tag,on_delete=models.CASCADE)
    view_count = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
