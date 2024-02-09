from django.shortcuts import render
from .models import *

# Create your views here.
def MainView(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = ContactUsUser(name=name, email=email,message=message)
        contact.save()

    # Получение всех объектов модели MenuItem
    menu_items = Product.objects.all()

    # Делим данные на две части
    total_items = len(menu_items)
    mid_point = total_items // 2

    menu_items_1 = menu_items[:mid_point]  # Первая половина
    menu_items_2 = menu_items[mid_point:]  # Вторая половина
    
    
    context = {
        'intro' : Intro.objects.last(),
        'menu_items_1': menu_items_1,
        'menu_items_2': menu_items_2,
        'about' : About.objects.last(),
        'contact_us_info' : ContactUsInfo.objects.last(),
    }
    return render(request, 'index.html', context)