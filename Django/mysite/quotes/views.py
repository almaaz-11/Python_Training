from django.shortcuts import render

def home(request):
    return render(request, 'quotes/home.html')

def passing_data(request):
    context = {
        "username": "Almaaz"
    }
    return render(request, 'quotes/passing_data.html', context)
