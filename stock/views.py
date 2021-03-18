from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Produit
from .forms import ProduitForm

# Create your views here.

def index(request):
    template = loader.get_template('connexion.html')
    return HttpResponse(template.render(request=request))

def dashboard(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render(request=request))

def approv(request):
    template = loader.get_template('approv.html')
    return HttpResponse(template.render(request=request))

def reapprov(request):
    template = loader.get_template('reapprov.html')
    return HttpResponse(template.render(request=request))

def produits(request):
    produits=Produit.objects.all()
    context={'produits':produits}
    template = loader.get_template('produits.html')
    return HttpResponse(template.render(context, request=request))

def save_product(request):
    name=request.GET['name']
    quantite=request.GET['quantite']
    securite=request.GET['securite']
    alerte=request.GET['alerte']
    Produit.objects.create( name=name, quantite=quantite, securite=securite, alerte=alerte)
    produits = Produit.objects.all()
    context = {'produits': produits}
    template = loader.get_template('produits.html')
    return HttpResponse(template.render(context, request=request))


def update_product(request, id_produit):
    ids=int(id_produit)
    produit = Produit.objects.get(pk=ids)
    name=request.GET['name']
    quantite=request.GET['quantite']
    securite=request.GET['securite']
    alerte=request.GET['alerte']
    #Produit.objects.create( name=name, quantite=quantite, securite=securite, alerte=alerte)

    forms=ProduitForm(request.GET, instance=produit)
    forms.save()
    produits = Produit.objects.all()
    context = {'produits': produits}
    template = loader.get_template('produits.html')
    return HttpResponse(template.render(context, request=request))

def detail(request, id_produit):
    ids=int(id_produit)
    produit=Produit.objects.get(pk=ids)
    context={'produit':produit}
    template = loader.get_template('detail.html')
    return HttpResponse(template.render(context, request=request))
    #return HttpResponse(produit)