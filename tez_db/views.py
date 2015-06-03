# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from tez_db import db_object
from tez_db import analizer
from tez_db import correct
import codecs
import json

## Ielādē datu bāzes funkciju pamatlapu
def db(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
        return render_to_response('db_home.html', context)
    else:
        return HttpResponseRedirect('/user/login/', context)

## Apstrādā datu bāzes radīšanas pieprasījumu
def create_db(request):
    # Get the context from the request
    context = RequestContext(request)
    if request.user.is_authenticated():
        document = []
        try:
            with codecs.open('tezaurs-full-for-MongoDB.json', encoding='utf-8') as f:
                # transfer json elements to python elements
                try:
                    document = json.load(f)
                    nolas = 'ir nolasīts'
                except Exception as inst:
                    document = []
                    nolas = 'nav nolasīts'
        except Exception as inst:
            document = []
            nolas = 'nav nolasīts'
        
        radit = db_object.create_db(document)
    
        context_dict = {'nolas':nolas, 'radit':radit}

        return render_to_response('saglab_db.html', context_dict, context)
    else:
        return HttpResponseRedirect('/user/login/', context)

## Apstrādā informācijas pievienošanas datu bāzei pieprasījumu
def add_db_object(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
        document = []
        try:
            with codecs.open('tezaurs-for-MongoDB-add.json', encoding='utf-8') as f:
                # transfer json elements to python elements
                try:
                    document = json.load(f)
                    nolas = 'ir nolasīts'
                except Exception as inst:
                    document = []
                    nolas = 'nav nolasīts'
        except Exception as inst:
            document = []
            nolas = 'nav nolasīts'
        
        radit = db_object.add_db_object(document)
    
        context_dict = {'nolas':nolas, 'radit':radit}

        return render_to_response('saglab_db.html', context_dict, context)
    else:
        return HttpResponseRedirect('/user/login/', context)

## Apstrādā kļūdu paziņojuma pievienošanu
def add_correction(request, word, word_ID):
    context = RequestContext(request)
    correction = request.POST['correction']
    db_object.add_correction(correction, word, word_ID)
    if request.user.is_authenticated():
        return render_to_response('user_correction_added.html', context)
    else:
        return render_to_response('correction_added.html', context)

## Apstrādā kļūdu paziņojumu attēlošanas pieprasijumu
def show_corrections(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
        context_dict = {'data_list': db_object.show_correction()}
        return render_to_response('user_correction_show.html', context_dict, context)
    else:
         return HttpResponseRedirect('/user/login/', context)

## Sagatavo saitu un novirza uz to
def redirect_to(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
        url = "/db/show_json/" + request.POST['input_word'] + "/" + request.POST['word_ID']
        return HttpResponseRedirect(url)
    else:
        return HttpResponseRedirect('/user/login/', context)

## Attēlo labojamos datus
def show_json(request, word, word_ID):
    context = RequestContext(request)
    if request.user.is_authenticated():
        json_data = db_object.find_word_in_db(word, word_ID)
        data = analizer.analizer(json_data)
        context_dict = {'data': data['output'], 'word':word, 'word_ID':word_ID}
        return render_to_response('user_show_for_correction.html', context_dict, context)
    else:
        return HttpResponseRedirect('/user/login/', context)
    
## Astrādā datu labošanu
def update_db_object(request, word, word_ID):
    context = RequestContext(request)
    if request.user.is_authenticated():
        old_json = db_object.find_word_in_db(word, word_ID)
        data = analizer.analizer(old_json)
        keys = data['keys']
        cor = {}
        for key in keys:
            if request.POST.has_key(key):
                cor[key] = request.POST[key]
        corrections = correct.correct(old_json, cor)
        radit = db_object.update_db_object(corrections, word, word_ID)
        json_data = db_object.find_word_in_db(word, word_ID)
        data = analizer.analizer(json_data)
        if word_ID != cor['hom_ID']:
            url = "/db/show_json/" + word + "/" + hom_ID
            return  HttpResponseRedirect(url)
        context_dict = {'data': data['output'], 'word':word, 'word_ID':word_ID, 'radit':u'Izmainas saglabātas!'}
        return render_to_response('user_show_for_correction.html', context_dict, context)
    else:
        return HttpResponseRedirect('/user/login/', context)
