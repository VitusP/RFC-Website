from django.db import models

# Recirculating Farm Gallery image
class GalleryImage(models.Model):
    # Image Title
    img_title = models.CharField(max_length=50, null=True)
    # Image description
    img_description = models.TextField(max_length=200, null=True)
    # Image
    image = models.ImageField(upload_to='images/', null=True)

# Contact of user
class Contact(models.Model):
    # First Name
    first_Name = models.CharField(max_length=50, null=True)
    # Last Name
    last_Name = models.CharField(max_length=50, null=True)
    # Email Address
    email_Address = models.CharField(max_length=50, null=True)

# Message unique for a Contact
class Message(models.Model):
    # Message
    message = models.TextField(max_length=200, null=True)