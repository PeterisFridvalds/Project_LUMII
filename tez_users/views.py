# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

def login(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
        return HttpResponseRedirect('/user/loggedin/', context)
    else:
        return render_to_response('user_login.html', context)

def login_post(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
        return HttpResponseRedirect('/user/loggedin/', context)
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/user/loggedin/', context)
        else:
            return HttpResponseRedirect('/user/ivalid/', context)

def logout(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
        auth.logout(request)
        return HttpResponseRedirect('/', context)
    else:
        return HttpResponseRedirect('/user/login/', context)

def loggedin(request):
    context = RequestContext(request)
    context_dict = {'user_name': request.user.username}
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/user/login/', context)
    else:
        return render_to_response('user_loggedin.html', context_dict, context)

def ivalid(request):
    context = RequestContext(request)
    return render_to_response('user_ivalid.html', context)

def ivalid_register(request):
    context = RequestContext(request)
    return render_to_response('user_ivalid_register.html', context)

def register(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                new_user = form.save()
                return HttpResponseRedirect('/user/register_sucsess/', context)
            else:
                return HttpResponseRedirect('/user/register/ivalid', context)
        else:
            return render_to_response('user_register.html', context)
    else:
        return HttpResponseRedirect('/user/login/', context)

def register_sucsess(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
        context_dict = {'user_name': request.user.username, 'user_register': 'Jaunais lietotājs ir veiksmīgi reģistrēts!'}
        return render_to_response('user_loggedin.html', context_dict, context)
    else:
        return HttpResponseRedirect('/user/login/', context)
