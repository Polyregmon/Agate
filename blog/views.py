from django.shortcuts import render
from .models import ItemMenu

# Create your views here.


def index(request):
    items = ItemMenu.objects.filter(active=True).order_by("-id")
    ctx = {'title': "Agate Cafe - Menu", 'items': items}
    return render(request, 'blog/index.html', ctx)
