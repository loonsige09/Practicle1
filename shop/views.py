from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def location(request):
    return render(request, 'location.html')

def catalog(request):
    products = [
        {'name': 'Робот-пылесос', 'category': 'Умный дом', 'price': 34990},
        {'name': 'Кофемашина', 'category': 'Техника для кухни', 'price': 42500},
        {'name': 'Умная лампа', 'category': 'Освещение', 'price': 2490},
        {'name': 'Электрочайник', 'category': 'Техника для кухни', 'price': 3200},
        {'name': 'Метеостанция', 'category': 'Гаджеты', 'price': 5990},
        {'name': 'Умные часы', 'category': 'Гаджеты', 'price': 15900},
        {'name': 'Микроволновая печь', 'category': 'Техника для кухни', 'price': 8900},
        {'name': 'Увлажнитель воздуха', 'category': 'Климат', 'price': 4500},
        {'name': 'Смарт-колонка', 'category': 'Умный дом', 'price': 7490},
        {'name': 'Телевизор 4K', 'category': 'Электроника', 'price': 49990},
    ]
    return render(request, 'catalog.html', {'products': products})

def promotions(request):
    suppliers = [
        {'title': 'Китай (Шэньчжэнь)', 'desc': 'Электроника и комплектующие для умного дома.'},
        {'title': 'Германия (Мюнхен)', 'desc': 'Бытовая техника премиум-класса и кухонные гаджеты.'},
        {'title': 'Южная Корея (Сеул)', 'desc': 'Инновационные решения для освещения и климата.'},
        {'title': 'Россия (Москва)', 'desc': 'Локальные сборщики умных устройств и аксессуаров.'},
    ]
    return render(request, 'promotions.html', {'suppliers': suppliers})
