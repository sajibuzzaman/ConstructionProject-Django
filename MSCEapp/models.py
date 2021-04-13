from django.db import models
from django.forms import ModelForm, TextInput, EmailInput, Textarea


# Create your models here.
class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.EmailField(blank=True, null=True, max_length=50)
    smptserver = models.CharField(blank=True, max_length=50)
    smtpemail = models.EmailField(blank=True, max_length=50)
    smptpassword = models.CharField(blank=True, max_length=10)
    smptport = models.CharField(blank=True, max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/')
    logo = models.ImageField(blank=True, upload_to='images/')
    slider_image = models.ImageField(blank=True, upload_to='images/')
    facebook = models.URLField(blank=True, max_length=50)
    instagram = models.URLField(blank=True, max_length=50)
    twitter = models.URLField(blank=True, max_length=50)
    youtube = models.URLField(blank=True, max_length=50)
    aboutuc = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    reference = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def ImageUrl(self):
        if self.slider_image:
            return self.slider_image.url
        else:
            return ''


class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),

    )
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=40)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField(max_length=1000, blank=True)
    status = models.CharField(max_length=40, choices=STATUS, default='New')
    ip = models.CharField(max_length=100, blank=True)
    Note = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        