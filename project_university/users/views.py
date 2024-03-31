from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginUserForm


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                if cd['type'] == "1":
                    return HttpResponseRedirect(reverse(viewname='students-get-id'))
                else:
                    return HttpResponseRedirect(reverse(viewname='teacher-work-check'))
    else:
        form = LoginUserForm()
    return render(request, template_name='users/login.html', context={'form': form})
