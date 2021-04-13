from django.shortcuts import render
from .models import Services, MSCETeam

# Create your views here.
def ServicesView(request):
    services = Services.objects.all()
    context={
        'services': services
    }
    return render(request, 'service.html', context)

def MSCETeamView(request):
    team = MSCETeam.objects.all()
    context ={
        'team': team
    }
    return render(request, 'team.html', context)
