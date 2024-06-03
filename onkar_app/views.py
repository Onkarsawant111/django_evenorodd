from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def onkar(request):
    return HttpResponse("<h1>even or odd at `evenodd route`</h1>")
def evenodd(request):
    content = {} 
    try:
        if request.method == "POST":
            num = eval(request.POST.get('num'))
            r = num % 2
            if r == 0:
                s = "even"
            else:
                s = "odd"        
    except:
        pass
    content = {'value':s}
    return render(request, 'onkar.html', content)