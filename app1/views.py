from django.shortcuts import render

# Create your views here.
def a1_first(request):
    d=context={'a':200,'b':100}
    return render(request,'a1_first.html',d)

def a1_second(request):
    d=context={'a':200,'b':300,'c':200}
    return render(request,'a1_second.html',d)