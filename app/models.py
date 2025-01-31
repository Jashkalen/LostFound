from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
class Item(models.Model):
    ITEM_TYPES = [
        ('Lost', 'Lost'),
        ('Found', 'Found')
    ]

    type = models.CharField(max_length=10, choices=ITEM_TYPES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateField()
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    contact_email = models.EmailField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"pk": self.pk})

















































