from django.shortcuts import render
from menu.models import Dish

def menu(request):
    dishes = Dish.objects.all()
    return render(request, 'core/menu.html', {'dishes': dishes})
