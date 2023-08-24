from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import team


# Create your views here.
def demo(request):
    obj = place.objects.all()
    teas=team.objects.all()
    return render(request, 'index.html', {'result': obj,'teas':teas})


# def teammates(request):
#     objs = team.objects.all()
#     return render(request, 'index.html', {'res': objs})

# def addition(request):
#     x=int(request.GET['n1'])
#     y=int(request.GET['n2'])
#     res=x+y
#     return render(request,'about.html',{'result':res})

# def about(request):
#     return render(request, 'about.html')
#
#
# def contact(request):
#     return render(request, 'contact.html')
