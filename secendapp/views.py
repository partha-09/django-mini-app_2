from django.shortcuts import render
from django.http import HttpResponse
from secendapp.models import Information
# Create your views here.
def Contact(request):
    if request.method=='POST':
        fullName=request.POST.get('name')
        emial=request.POST.get('email')
        phone=request.POST.get('phone')
        home=Information(fullName=fullName,emial=emial,phone=phone)
        home.save()
    return render(request,'Register.html')
def info(request):
    namelist = Information.objects.all()
    context = {
        'namelist': namelist,  # This will be a list of tuples
    }
    return render(request, 'Inquiry.html', context)
