from django.db import models
from django.forms import ModelForm
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.




class Setting(models.Model):
    STATUS =(
        ('True', 'True'),
        ('False', 'False'),
    )


    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    desscription = models.CharField(max_length=255, null=True)
    company = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(null=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    icon = models.ImageField(blank=True, null=True, upload_to='images/')
    logo = models.ImageField(blank=True, null=True, upload_to='images/')
    cart_icon = models.ImageField(blank=True, null=True, upload_to='images/')
    menu_icon = models.ImageField(blank=True, null=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    about = RichTextUploadingField(blank=True)
    about2 = RichTextUploadingField(blank=True, default='About')
    contact = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return self.title

class Brand(models.Model):
    title = models.CharField(max_length=10,blank=True,null=True)
    brands = models.ImageField(blank=True,null=True,upload_to='images/')


    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    comment = models.CharField(max_length=250, blank=True, null=True, default='Thumbs up Alist')
    testimos = models.ImageField(blank=True,null=True, upload_to='images/')

    def __str__(self):
        return self.name
    
class ContactMessage(models.Model):
    STATUS =(
        ('New', 'New'),
        ('Read', 'Read'),
        ('pending', 'Pending'),
        ('closed', 'Closed'),
    )


    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True, max_length=50)
    message = models.CharField(blank=True, max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    note = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ContactForm(ModelForm):
    class Meta:
        model= ContactMessage
        fields = ['name', 'email', 'subject', 'message']





