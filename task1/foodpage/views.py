from django.shortcuts import render,redirect

# Create your views here.
def projecthomepage(request):
    return render(request, 'projecthomepage.html')

def breakfasthomepage(request):
    return render(request, 'breakfasthomepage.html')

def lunchhomepage(request):
    return render(request, 'lunchhomepage.html')
