from django.shortcuts import render

# Create your views here.

def AllBooksView(request):
    context={

    }
    return render(request, 'BookHome.html', context)