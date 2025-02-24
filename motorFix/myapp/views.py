from django.http import HttpResponse  # Import HttpResponse

def index(request):
    return HttpResponse("Hello World")  
