from django.shortcuts import redirect, render

def index(request):
    return redirect('simulation/')


def simulation(request):
    return render(request,'index.html')
