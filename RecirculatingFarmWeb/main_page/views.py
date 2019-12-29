from django.shortcuts import render
from .models import GalleryImage, Contact, Message

# Home Page views
def homepage(request):
    return render(request, "main_page/homepage.html")

def galleryPage(request):
    gallery_Images =  GalleryImage.objects
    return render(request, "main_page/gallery.html", {'Gallery_Images': gallery_Images} )

# Contact Page Views
def contactPage(request):
    contacts = Contact.objects
    messages = Message.objects
    return render(request, "main_page/contact.html", {'Contacts':contacts, 'Messages': messages})
