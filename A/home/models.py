from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="postss")
    body = models.TextField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #Meta options
    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("home:post_detail", args=(self.id, self.slug))

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Ucomment")
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="Pcomment")
    reply = models.ForeignKey("self", on_delete=models.CASCADE, related_name="rcomments", blank=True, null=True)
    is_reply = models.BooleanField(default=False)
    body = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.body[:30]}'

