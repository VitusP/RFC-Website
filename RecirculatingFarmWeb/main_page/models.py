from django.db import models

# Recirculating Farm Gallery image
class GalleryImage(models.Model):
    # Image Title
    img_title = models.CharField(max_length=50, null=True)
    # Image description
    img_description = models.TextField(max_length=200, null=True)
    # Image
    image = models.ImageField(upload_to='images/', null=True)
    # object return
    def __str__(self):
        return "Image Title: %s, Description: %s" % (self.img_title, self.img_description)

# Contact of user
class Contact(models.Model):
    # First Name
    first_Name = models.CharField(max_length=50, null=True)
    # Last Name
    last_Name = models.CharField(max_length=50, null=True)
    # Email Address
    email_Address = models.CharField(max_length=50, null=True)
    # object return 
    def __str__(self):
        return "Name: %s %s, Email: %s" % (self.first_Name, self.last_Name, self.email_Address)

# Message unique for a Contact
class Message(models.Model):
    # Message
    message = models.TextField(max_length=200, null=True)
    def __str__(self):
        return "Message: %20s" % (self.message)

# Homepage Image/Description model
class ClubDescription(models.Model):
    # Text title
    description_Title = models.CharField(max_length=50, null=True)
    # Text description
    description = models.TextField(max_length=200, null=True)
    # Image
    description_image = models.ImageField(null=True)