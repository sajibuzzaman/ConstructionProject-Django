from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Setting, ContactMessage, ContactForm
from ConstructApp.models import ConstructionCategory, ConstructionProject, Images
from serviceMSCE.models import Services

# Create your views here.

def home(request):
    slider_img = ConstructionProject.objects.order_by('id')[:3]
    services = Services.objects.all
    projects = ConstructionProject.objects.all()
    context={
        'slider_img': slider_img,
        'services': services,
         'projects': projects,
    }
    return render(request, 'homebase.html', context)


def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Your massage has been send successfully!!')

            return redirect('Contact')
    
   
    context={
      
    }
    return render(request, 'ContactMessage.html', context)

def Allprojects(request):

    projects = ConstructionProject.objects.all()
    context={
      
        'projects': projects
    
    }
    return render(request, 'projects.html', context)

def project_single(request, slug):

    single_project = get_object_or_404(ConstructionProject, slug=slug)
    images = Images.objects.filter(constructionproject__slug = slug)

    context={
      
        'single_project' : single_project,
        'images' : images,
    
    }
    return render(request, 'project-single.html', context)


def AboutUs(request):
    context={

    }
    return render(request, 'about.html', context)