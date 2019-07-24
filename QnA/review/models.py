from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question-home',kwargs={'pk': self.pk})

class Question(models.Model):
    title = models.CharField(max_length=100)
    q_title = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=40, default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('answer-home',kwargs={'pk': self.pk})

class Answer(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField(default="")
    a_title = models.ForeignKey(Question, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Just(models.Model):
    title = models.OneToOneField(Post, on_delete=models.CASCADE)