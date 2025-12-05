from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Quote of the Day</h1><p>Stay hungry, stay foolish!</p>")
