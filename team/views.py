from django.shortcuts import render
from team.models import Team

# Create your views here.


def team(request):
    team = Team.objects.all()
    context = {
        "team": team,
    }
    return render(request, 'team.html', context)
