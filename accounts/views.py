from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from . import forms


def add_user(request, is_client=False):
    context = {'add_user': True,
               'user_form': forms.AccountForm(request.POST or None)}

    if is_client:
        context['form'] = forms.ClientForm(request.POST or None)
    else:
        context['form'] = forms.EmployeeForm(request.POST or None)
    if request.POST:
        if context['user_form'].is_valid() and context['form'].is_valid():
            user_cd = context['user_form'].cleaned_data
            user = User.objects.create_user(user_cd.get('first_name'),
                                            user_cd.get('email'),
                                            user_cd.get('password'))
            user.last_name = user_cd.get('last_name')
            user.save()

            obj = context['form'].save(commit=False)
            obj.account = user
            obj.save()
            messages.success(request, _("Your account has been created!"))
            return redirect('home_page')
        else:
            messages.error(request, _("Make sure all data are all right!"))
    return render(request, "accounts/add_user.html", context=context)


def login_user(request):
    context = {'form': forms.AuthenticationForm(request.POST or None)}
    if request.POST:
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('home_page')

        else:
            context['authentication_fail'] = True
    return render(request, "accounts/login.html", context=context)


def logout_user(request):
    logout(request)
    return redirect('home_page')
