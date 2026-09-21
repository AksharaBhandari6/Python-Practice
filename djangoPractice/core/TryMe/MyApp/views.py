from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')
    #return HttpResponse("this is trial page")
def about(request):
    return render(request,'about.html')
def menu(request):
    return render(request,'menu.html')
def contact(request):
    return render(request,'contact.html')
def reviews(request):
    return render(request,'reviews.html')

