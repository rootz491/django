from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
# Create your models here.


class note(models.Model):
        title = models.CharField(max_length=50, null=False)
        content = models.TextField(max_length=250, null=False)
        createdAt = models.DateTimeField(auto_now_add=True)
        is_bookmarked = models.BooleanField(default=False)
        id = models.CharField(max_length=32, primary_key=True)
        user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

        class Meta:
                ordering = ['-createdAt', 'title', 'content']

        def __str__(self):
                return self.title

        def get_absolute_url(self):
                return reverse('note:index')