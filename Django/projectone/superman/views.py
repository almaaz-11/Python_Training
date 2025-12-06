from django.shortcuts import render

# Create your views here.
def all_superhero(request):
    return render(request, 'superman/all_superhero.html')
