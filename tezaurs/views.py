# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
import json
import codecs
from tezaurs import show_db
from tezaurs import search_word
from tezaurs.models import *

## Paredzēts, lai pārbaudītu, vai ir ievadīti dati
##def show(request):
##    context = RequestContext(request)
##    context_dict = {'data_list': show_db.show_db()}
##    return render_to_response('show_db.html', context_dict, context)

## Funkcija, ka pārbauda vai atmiņā ir ielādēta informācija par nelokāmajiem vārdiem, ja nav, tad to ielādē
def document_init():
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

## Ielādē sākumlapu, kuras rikjosla atkarīga, vai lietotājs ir vai nav pieslēdzies
def home(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
        return render_to_response('user_home.html', context)
    else:
        return render_to_response('home.html', context)

## Sagatavo saiti un pārvirza uz to
def redirect_to_show(request):
    context = RequestContext(request)
    url = "/tezaurs/" + request.POST['input_word'] + "/" + request.POST['word_ID']

    if request.POST['input_word'] == "":
        return HttpResponseRedirect('/tezaurs')
    else:
        return HttpResponseRedirect(url)

## Sagatavo meklētā šķirkļa informāciju izvadei, kuras rikjosla atkarīga, vai lietotājs ir vai nav pieslēdzies
def show_word(request, input_word, word_ID):
    context = RequestContext(request)

    ## Atrod škirkļa vādru un tam līdzīgus vārdus (meklēto vārdu padod tālākai apstrādei)
    data = search_word.search_word(input_word, word_ID)
    json_data = data['output']
    word_list = data['word_list']
    speach_id = data['speach_id']

    ## Izsauc funkciju izvadāmās informācijas sagatavošanai
    context_dict = search_word.return_centext_dict(json_data, input_word, word_ID, speach_id, word_list, document_init())
    if request.user.is_authenticated():
        return render_to_response('user_show.html', context_dict, context)
    else:
        return render_to_response('show.html', context_dict, context)




