from django.contrib import admin
from .models import GalleryImage, Contact, Message, ClubDescription
# Register your models here.
admin.site.register(GalleryImage)
admin.site.register(Contact)
admin.site.register(Message)
admin.site.register(ClubDescription)