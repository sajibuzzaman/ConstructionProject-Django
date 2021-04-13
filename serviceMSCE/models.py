from django.db import models
from ConstructApp.models import ConstructionCategory
# Create your models here.
class Services(models.Model):
    STATUS=(
        ('True', 'True'),
        ('False', 'False')
    )
    title = models.CharField(max_length=200)
    titleicon = models.CharField(max_length=200)
    image = models.ImageField(upload_to='services/')
    details = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class MSCETeam(models.Model):
    STATUS=(
        ('True', 'True'),
        ('False', 'False')
    )
    name = models.CharField(max_length=200)
    sp_category = models.ForeignKey(ConstructionCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='team/')
    details = models.TextField()
    facebook_url = models.URLField(max_length=200, blank=True, null=True)
    twitter_url = models.URLField(max_length=200, blank=True, null=True)
    instagram_url = models.URLField(max_length=200, blank=True, null=True)
    youtube_url = models.URLField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=30, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name