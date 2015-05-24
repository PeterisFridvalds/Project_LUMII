# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
import json
import codecs
from tezaurs import create_db_object
from tezaurs import show_db
from tezaurs import search_word
from tezaurs.models import *

def show(request):
    context = RequestContext(request)
    context_dict = {'data_list': show_db.show_db()}
    return render_to_response('show_db.html', context_dict, context)
    
def home(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
        return render_to_response('user_home.html', context)
    else:
        return render_to_response('home.html', context)

def redirect_to_show(request):
    # Get the context from the request
    context = RequestContext(request)
    url = "/tezaurs/" + request.POST['input_word'] + "/" + request.POST['word_ID']

    if request.POST['input_word'] == "":
        return HttpResponseRedirect('/tezaurs')
    else:
        return HttpResponseRedirect(url)

def show_word(request, input_word, word_ID):
    # Get the context from the request
    context = RequestContext(request)
    data = search_word.search_word(input_word, word_ID)
    json_data = data['output']
    word_list = data['word_list']
    speach_id = data['speach_id']
    context_dict = search_word.return_centext_dict(json_data, input_word, word_ID, speach_id, word_list)
    if request.user.is_authenticated():
        return render_to_response('user_show.html', context_dict, context)
    else:
        return render_to_response('show.html', context_dict, context)


def add_to_db(request):
    # Get the context from the request
    context = RequestContext(request)
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
        
    radit = create_db_object.create_db(document)
    

    context_dict = {'nolas':nolas, 'radit':radit}

    return render_to_response('saglab_db.html', context_dict, context)

