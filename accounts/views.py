from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from . import forms, models
import json


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
            user = User.objects.create_user(user_cd.get('username'),
                                            user_cd.get('email'),
                                            user_cd.get('password'))
            user.last_name = user_cd.get('last_name')
            user.first_name = user_cd.get('first_name')
            if is_client:
                user.is_active = True
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
    context = {'form': forms.CustomAuthenticationForm(request.POST or None)}
    if request.POST:
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('accounts_panel')

        else:
            context['authentication_fail'] = True
    return render(request, "accounts/login.html", context=context)


def logout_user(request):
    logout(request)
    return redirect('home_page')


@login_required(login_url='/accounts/login')
def panel(request):
    if request.user.is_superuser:
        return redirect('admin_panel')
    account = models.Account.objects.get_from_user(request.user)
    if account.is_client():
        return redirect('client_panel')
    if account.is_employee():
        return redirect('employee_panel')


@login_required(login_url='/accounts/login')
def client_panel(request):
    account = models.Account.objects.get_from_user(request.user)
    if not account.is_client():
        return redirect('home_page')
    return render(request, 'accounts/client_panel.html')


@login_required(login_url='/accounts/login')
def employee_panel(request):
    account = models.Account.objects.get_from_user(request.user)
    if not account.is_employee():
        return redirect('home_page')
    return render(request, 'accounts/employee_panel.html')


@login_required(login_url='/accounts/login')
def admin_panel(request):
    if not request.user.is_superuser:
        return redirect('home_page')
    context = {
        'employees': models.Employee.objects.filter(account__is_active=False)}
    return render(request, 'accounts/admin_panel.html', context)


@login_required(login_url='accounts/login')
def update_account(request):
    context = {
        'user_form': forms.UpdateUserForm(request.POST or None,
                                          instance=request.user)}
    account = models.Account.objects.get_from_user(request.user)
    if account.is_employee():
        context['form'] = forms.EmployeeForm(
            request.POST or None, instance=request.user.employee)
    elif account.is_superuser:
        context['form'] = None
    else:
        context['form'] = forms.ClientForm(
            request.POST or None, instance=request.user.client)

    if request.POST:
        if context['user_form'].is_valid() and context['form'] is None:
            user = context['user_form'].save()
            messages.success(request, _('Profile edited'))
            return redirect('accounts_panel')

        if context['user_form'].is_valid() and context['form'].is_valid():
            user = context['user_form'].save()
            obj = context['form'].save()
            messages.success(request, _('Profile edited'))
            return redirect('accounts_panel')
    return render(request, 'accounts/change_user.html', context)


@login_required(login_url='accounts/login')
def toggle_activate_user(request):
    if not request.user.is_superuser:
        raise Http404(_("This is not the road you are looking for!"))
    if request.method == 'POST' and request.is_ajax():
        try:
            account = models.Account.objects.get(id=request.POST['account_id'])
            account.is_active = not account.is_active
            account.save()
            success = True
        except models.Account.DoesNotExist:
            success = False
        return HttpResponse(json.dumps({'success': success}),
                            content_type='application/json')
