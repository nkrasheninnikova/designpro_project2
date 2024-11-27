from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *

def index(request):
    return render(request, 'index.html')

@login_required
def indexacc(request):
    user_requests = Request.objects.filter(user=request.user)
    return render(request, 'profile.html', {'user_requests': user_requests})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.fio = form.cleaned_data['fio']  # Предполагается, что это поле есть в форме
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = SignUpForm()  # Создаем форму для GET-запроса

    return render(request, 'signup.html', {'form': form})  # Возвращаем форму для отображения

