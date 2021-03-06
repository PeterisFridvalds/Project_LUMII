# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from inflect import search_word
import json
import codecs

def document_init(): # Function that returns python data loded fom json
    try:
        document
    except Exception as inst:
        global document
        document = []
        if document == []:
            # open file and read from it
            try:
                with codecs.open('NotForInflecting.json', encoding='utf-8') as f:
                    # transfer json elements to python elements
                    try:
                        document = json.load(f)
                    except Exception as inst:
                        document = []
            except Exception as inst:
                document = []
    return document

def index(request):
    'Get the context from the request'
    context = RequestContext(request)
    if request.user.is_authenticated():
        return render_to_response('user_inflect_index.html', context)
    else:
        return render_to_response('inflect_index.html', context)

def redirect_to_show(request):
    # Get the context from the request
    context = RequestContext(request)
    url = "/inflect/" + request.POST['input_word']

    if request.POST['input_word'] == "":
        return HttpResponseRedirect('/inflect')
    else:
        return HttpResponseRedirect(url)

def show_word(request, input_word):
    # Get the context from the request
    context = RequestContext(request)

    # data get result from search function
    # Search function looks for input word in document(variable, wich contains jason converted to python)
    data = search_word.search_word(document_init(), input_word)
    json_data = data['output']
    speach_id = data['speach_id']

    # Calls analizer function
    # output_data = analizer.analizer(data)

    # Function returns word and data for outputing on screen
    context_dict = search_word.return_centext_dict(json_data, input_word, speach_id)

    if request.user.is_authenticated():
        return render_to_response('user_inflect_show.html', context_dict, context)
    else:
        return render_to_response('inflect_show.html', context_dict, context)
