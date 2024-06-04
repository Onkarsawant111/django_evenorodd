from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def onkar(request):
    return HttpResponse("<h1>even or odd at `evenodd route`</h1>")
    
def evenodd(request):
    content = {} 
    s = " "
    try:
        if request.method == "POST":
            # manual form validation : 
            if request.POST.get('num')=="": 
                return render(request, 'onkar.html',{'error':True})

            num = eval(request.POST.get('num'))
            r = num % 2
            if r == 0:
                s = "even"
            elif r != 0:
                s = "odd"   
    except:
        if TypeError:
            s = "only numbers are allowed"
        elif ValueError:
            s = "cannot be empty"
    content = {'value':s}
    return render(request, 'onkar.html', content)