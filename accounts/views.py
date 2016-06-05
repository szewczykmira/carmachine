from django.shortcuts import render, redirect
from django.contrib.auth.models import User
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

