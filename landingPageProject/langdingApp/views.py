from django.shortcuts import render

from .models import about


# Create your views here.
def home(request):
    aboutdata= about.objects.all()[0]
    
    context={
        'aboutt': aboutdata,
        
        
    }

    return render(request, 'index.html',context)

def feature(request):
    return render(request, 'feature.html')
def screenshot(request):
    return render(request, 'screenshot.html')
def review(request):
    return render(request, 'review.html')
def plan(request):
    return render(request, 'plan.html')
def download(request):
    return render(request, 'download.html')