from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from website import search_word
from website import analizer
import json

def document_init(): # Function that returns python data loded fom json
    global document
    document = []
    if document == []:
        # open file and read from it
        try:
            with open('tezaurs-full.json', encoding='utf-8') as f:
                # transfer json elements to python elements
                try:
                    document = json.load(f)
                except Exception as inst:
                    document = []
        except Exception as inst:
            document = []
    return document

def home(request):
    # Get the context from the request
    context = RequestContext(request)

    # Return a rendered response to send to the client.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('index.html', context)

def index(request):
    # Get the context from the request
    context = RequestContext(request)

    # Return a rendered response to send to the client.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('index.html', context)

def redirect_to_show(request):
    # Get the context from the request
    context = RequestContext(request)
    url = "/website/" + request.POST['input_word'] + "/" + request.POST['word_ID']

    if request.POST['input_word'] == "":
        return HttpResponseRedirect('/website')
    else:
        return HttpResponseRedirect(url)

def show_word(request, input_word, word_ID):
    # Get the context from the request
    context = RequestContext(request)
    
    # open file and read from it
    try:
        document
    except Exception as inst:
        document = document_init

    # data get result from search function
    # Search function looks for input word in document(variable, wich contains jason converted to python)
    data = search_word.search_word(document, input_word)
    json_data = data['output']
    speach_id = data['speach_id']

    # Calls analizer function
    # output_data = analizer.analizer(data)

    # Function returns word and data for outputing on screen
    context_dict = search_word.return_centext_dict(json_data, input_word, word_ID, speach_id)

    # Return a rendered response to send to the client.
    return render_to_response('show.html', context_dict, context)
