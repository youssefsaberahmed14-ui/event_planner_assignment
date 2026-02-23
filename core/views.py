from django.http import HttpResponse

def home(request):
    return HttpResponse("welcome to home page")

def about(request):
    return HttpResponse("welcome to about page")