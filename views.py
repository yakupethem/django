from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import loader
from. models import yazar,kitap

# Create your views here.

def index(request):
    return HttpResponse("anasayfa")

def authors(request):
    
    context={
        "liste":kitap.objects.all()
    }
    return render(request,"authors.html",context)

def books(request):
    return HttpResponse("kitaplar")

def details(request,authorId):
    try:
        context={
            "detay":yazar.objects.get(pk=authorId)
        }
    except yazar.DoesNotExist:
        raise Http404("yazar bulunamadı")
    return render(request,"authordetail.html",context)