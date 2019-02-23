from django.shortcuts import render
from gallery.models import Gallery

# Create your views here.


def gallery(request):
    gallery_m = Gallery.objects.all()
    context = {
        "gallery_m": gallery_m,
    }
    return render(request, 'gallery.html', context)

