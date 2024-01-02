from django.db import models
from django.utils.text import slugify

class CountScope(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date= models.DateField(blank=True, null=True)
    slug = models.SlugField(default="",null=True, blank=True, unique=True, db_index=True) 
    isActive = models.BooleanField(default=False, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args,kwargs)

    def __str__(self):
        return f"{self.title}"