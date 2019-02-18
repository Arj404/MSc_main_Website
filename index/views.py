from django.shortcuts import render
from index.models import Team, Events, Gallery

# Create your views here.


def index(request):
    team = Team.objects.all()
    events = Events.objects.all()
    gallery = Gallery.objects.all()
    context = {
        "core_team": team,
        "event": events,
        "gallery": gallery,
    }
    return render(request, 'index.html', context)