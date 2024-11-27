from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *

def index(request):
    done_requests = Request.objects.filter(status='В')[:4]
    accepted_request_counter = Request.objects.filter(status='П').count()
    completed_request_counter = Request.objects.filter(status='В').count()
    new_request_counter = Request.objects.filter(status='Н').count()
    return render(request, 'index.html', {
        'done_requests': done_requests, 'accepted_request_counter': accepted_request_counter,'completed_request_counter': completed_request_counter,
        'new_request_counter': new_request_counter}
    )

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


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        pic_form = ProfilePicForm(request.POST, request.FILES)

        if user_form.is_valid() and pic_form.is_valid():
            user = user_form.save()
            profile = pic_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('home')  # перенаправление на домашнюю страницу
    else:
        user_form = UserRegistrationForm()
        pic_form = ProfilePicForm()

    return render(request, 'signup.html', {'user_form': user_form, 'pic_form': pic_form})

@login_required
def request_add(request):
    if request.method == 'POST':
        form = RequestCreateForm(request.POST, request.FILES)
        if form.is_valid():
            request_save = form.save(commit=False)
            request_save.user = request.user
            request_save.save()
            return redirect('profile')
    else:
        form = RequestCreateForm(initial={'user': request.user.pk})
    return render(request, 'request_add.html', {'form': form})

@login_required
def requests(request):
    new_requests = Request.objects.filter(status='Н')
    context = {'new_requests': new_requests}
    return render(request, 'request.html', context)
