from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def visit_count_view(request):
    visit_count = request.session.get('visit_count', 0)

    visit_count += 1

    request.session['visit_count'] = visit_count

    request.session['fav_lang'] = 'Python'

    print(request.session.items())

    return HttpResponse(f"You have visited this page {visit_count} times")

def remove_favorite_language(request):
    if 'fav_lang' in request.session:
        del request.session['fav_lang']

    return HttpResponse("Favorite language removed from session.")

def clear_session(request):
    request.session.clear()
    return HttpResponse("All session data cleared.")

def flush_session(request):
    request.session.flush()
    return HttpResponse("Session completely flushed.")

