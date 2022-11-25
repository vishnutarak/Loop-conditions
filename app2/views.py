from django.shortcuts import render

# Create your views here.
def a2_first(request):
    d=context={'a':200,'b':300,'c':400}
    return render(request,'a2_first.html',d)

def a2_second(request):
    d=context={'name':'Tarak'}
    return render(request,'a2_second.html',d)