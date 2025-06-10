from django.http import HttpResponse

def home_page(request):
   
    return HttpResponse("Welcome to our Django Book Catalog!")

def home_page(request):
    return HttpResponse("hello world!")