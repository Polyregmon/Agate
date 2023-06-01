from django.shortcuts import render
from .models import ItemMenu, Category

# Create your views here.


def index(request):
    items = ItemMenu.objects.filter(active=True)
    breakfast = Category.objects.filter(engid__iexact="Breakfast")
    britems = items.filter(category__engid="Breakfast")
    coffee = Category.objects.filter(engid__iexact="Coffee")
    citems = items.filter(category__engid="Coffee")
    herbal = Category.objects.filter(engid__iexact="Herbal")
    hitems = items.filter(category__engid="Herbal")
    syrup = Category.objects.filter(engid__iexact="Syrup")
    sitems = items.filter(category__engid="Syrup")
    smoothie = Category.objects.filter(engid__iexact="Smoothie")
    smitems = items.filter(category__engid="Smoothie")
    shake = Category.objects.filter(engid__iexact="Shake")
    shitems = items.filter(category__engid="Shake")
    mocktail = Category.objects.filter(engid__iexact="Mocktail")
    moitems = items.filter(category__engid="Mocktail")
    appetizer = Category.objects.filter(engid__iexact="Appetizer")
    pasta = Category.objects.filter(engid__iexact="Pasta")
    panini = Category.objects.filter(engid__iexact="Panini")
    pizza = Category.objects.filter(engid__iexact="Pizza")
    platter = Category.objects.filter(engid__iexact="Platter")
    salad = Category.objects.filter(engid__iexact="Salad")
    drink = Category.objects.filter(engid__iexact="Drink")
    hookah = Category.objects.filter(engid__iexact="Hookah")
    print (britems)
    ctx = {'title': "Agate Cafe - Menu", 'items': items}
    return render(request, 'blog/index.html', ctx)


