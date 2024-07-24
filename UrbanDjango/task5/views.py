from django.shortcuts import render
from .forms import UserRegister

# Create your views here.


def sign_up_by_django(request):
    users = {
        'DIE.EID': 'test1234',
        'Shrewder': 'turtle_suck',
        'Splinter': 'my_sons\'r_turtle'
    }
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username in users.keys():
                info.update({'error': 'Пользователь с таким именем существует!'})
            elif password != repeat_password:
                info.update({'error': 'Пароли не совпадают'})
            elif age < 18:
                info.update({'error': 'Вам нет 18, пожалуйста, покиньте страницу :с'})
            else:
                info.update({'message': f'Приветствуем, {username}'})
    else:
        form = UserRegister()
    info.update({'form': form})
    return render(request, 'registration_page.html', context={'info': info})


def sign_up_by_html(request):
    users = {
        'DIE.EID': 'test1234',
        'Shrewder': 'turtle_suck',
        'Splinter': 'my_sons\'r_turtle'
    }
    info = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        if username in users.keys():
            info.update({'error': 'Пользователь с таким именем существует!'})
        elif password != repeat_password:
            info.update({'error': 'Пароли не совпадают'})
        elif age < 18:
            info.update({'error': 'Вам нет 18, пожалуйста, покиньте страницу :с'})
        else:
            info.update({'message': f'Приветствуем, {username}'})
    return render(request, 'registration_page.html', context={'info': info})