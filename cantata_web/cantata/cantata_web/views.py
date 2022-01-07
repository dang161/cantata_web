from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'layouts/index.html')
def about(request):
    return render(request, 'layouts/about.html')
def menu(request):
    return render(request, 'layouts/menu.html')
def blog(request):
    return render(request, 'layouts/blog.html')
def contact(request):
    return render(request, 'layouts/contact.html')       