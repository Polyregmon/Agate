from django.db import models

# Create your models here.


class ItemMenu(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to="media/", null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    active = models.BooleanField(default=True)
    eng = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.title
