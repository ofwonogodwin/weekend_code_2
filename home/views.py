from django.shortcuts import render
from.models import Members

# Create your views here.
def home(request):
    return render (request,'home.html')

def about(request):
    currentMembers = Members.objects.all
    return render(request,'about.html',{'all':currentMembers})

def gallery(request):
    return render(request,'gallery.html')

def contact(request):
    return render(request,'contact.html')