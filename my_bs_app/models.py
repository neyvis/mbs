from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from . import constants


class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images')
    content = models.TextField(help_text="Enter your text here.")
    status = models.IntegerField(choices=constants.STATUSES, default=constants.STATUS_DRAFT)

    class Meta:
        ordering = ['-created_on']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
