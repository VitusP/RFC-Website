from django.shortcuts import render
from .models import GalleryImage, Contact, Message, ClubDescription

# Home Page views
def homepage(request):
    club_Descriptions = ClubDescription.objects
    return render(request, "main_page/homepage.html", {'Club_Description':club_Descriptions})

def galleryPage(request):
    gallery_Images =  GalleryImage.objects
    return render(request, "main_page/gallery.html", {'Gallery_Images': gallery_Images} )

# Contact Page Views
def contactPage(request):
    contacts = Contact.objects
    messages = Message.objects
    return render(request, "main_page/contact.html", {'Contacts':contacts, 'Messages': messages})
