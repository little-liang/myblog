from django.db import models

# Create your models here.


class Catagory(models.Model):
    name = models.CharField('名称',max_length=30)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('名称', max_length=16)
    def __str__(self):
        return self.name

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    publish_time = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    catagory = models.ForeignKey(Catagory)
    content = models.TextField()
    author = models.CharField(max_length=8)
    canbe_content = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article)
    author = models.CharField(max_length=8)
    publish_time = models.DateField(auto_now_add=True)
    content = models.TextField()
    def __str__(self):
        return self.author

