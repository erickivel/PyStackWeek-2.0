from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth


def cadastro(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0:
            messages.add_message(request, constants.ERROR,
                                 'Preencha todos os campos')
            return redirect('/auth/cadastro')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR,
                                 'Já existe um usuário com esse nome cadastrado')
            return redirect('/auth/cadastro')

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            user.save()

            messages.add_message(request, constants.SUCCESS,
                                 'Usuário cadastrado com sucesso!')

            return redirect('/auth/login')
        except:
            return redirect('/auth/cadastro')


def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        print(password)

        if not user:
            messages.add_message(request, constants.ERROR,
                                 'Email or password are incorrect!')
            return redirect('/auth/login')
        else:
            auth.login(request, user)
            return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/auth/login')
