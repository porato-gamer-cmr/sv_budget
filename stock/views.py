from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Produit
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
def listproduits(request):
    produits = Produit.objects.all();
    return JsonResponse([produit.serialize() for produit in produits], safe=False)

@csrf_exempt
def addproduits(request):
    if request.method == 'POST':
        req = request.body
        my_json = req.decode('utf8').replace("'", '"')
        produit = json.loads(my_json)
        name=produit['name']
        quantite=produit['quantite']
        securite=produit['securite']
        alerte=produit['alerte']
        Produit.objects.create( name=name, quantite=quantite, securite=securite, alerte=alerte)
    return JsonResponse({'message': 'Enregistrement reussi' })

@csrf_exempt
def updateproduits(request):
    if request.method == 'POST':
        req = request.body
        my_json = req.decode('utf8').replace("'", '"')
        produit = json.loads(my_json)
        ids=produit['id']
        name=produit['name']
        quantite=produit['quantite']
        securite=produit['securite']
        alerte=produit['alerte']
        Produit.objects.filter(id=ids).update(name=name, quantite=quantite, securite=securite, alerte=alerte)
    return JsonResponse({'message': 'Mise à jour reussi' })

@csrf_exempt
def deleteproduits(request):
    if request.method == 'POST':
        req = request.body
        my_json = req.decode('utf8').replace("'", '"')
        produit = json.loads(my_json)
        ids=produit['index']
        prod = Produit.objects.get(pk=ids)
        prod.delete()
    return JsonResponse({'message': 'Suppression reussi' })
