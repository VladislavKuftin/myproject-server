from django.shortcuts import render


# Create your views here.

def index(request):
    menu = {'title':'Магазин'}
    return render(request, "mainapp/index.html", menu)


def products(request):
    menu = {'title': "Продукты"}
    return render(request, "mainapp/products.html",menu)


def contact(request):
    menu = {'title': "Контакты"}
    return render(request, "mainapp/contact.html", menu)


def context(request):
    context = {
        'title':'test context',
        'header':'Добро пожаловать на сайт',
        'username':'John',
        'products': [
            {'name':'Стулья', 'price':5678},
            {'name':'Диваны', 'price':15678},
            {'name':'Столы', 'price':25678},
        ]
    }
    return render(request, "mainapp/text_context.html", context)

def menu(requset):
    links_menu = [
        {'href':'products_all', 'name':'все'},
        {'href':'products_home', 'name':'дом'},
        {'href':'products_office', 'name':'офис'},
        {'href':'products_classic', 'name':'классика'},
    ]

    return render(requset, 'inc_categories_menu.html', links_menu)
