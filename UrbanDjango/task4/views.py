from django.shortcuts import render

# Create your views here.

__games = ['Atomic Heart', 'It takes Two', 'To be Headed or not To be']
#__user_product = set()


def main_page(request):
    return render(request, './fourth_task/main_page.html')


def shop_page(request):
    context = {
        'games': __games,
        #'user_product': __user_product
    }
    return render(request, './fourth_task/shop_page.html', context=context)


def basket_page(request):
    return render(request, './fourth_task/basket_page.html')