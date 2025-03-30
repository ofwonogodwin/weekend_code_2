from django.shortcuts import render
from.models import Members
from.forms import MemberForm

# Create your views here.
def home(request):
    return render (request,'home.html')

def about(request):
    currentMembers = Members.objects.all
    return render(request,'about.html',{'all':currentMembers})

def gallery(request):
    return render(request,'gallery.html')

def contact(request):
    if request.method =='post':
        form =MemberForm(request.post or None)
    else:
        return render(request,'contact.html')