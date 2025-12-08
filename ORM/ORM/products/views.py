from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def visit_count_view(request):
    visit_count = request.session.get('visit_count', 0)

    visit_count += 1

    request.session['visit_count'] = visit_count

    return HttpResponse(f"You have visited this page {visit_count} times")
