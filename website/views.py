from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from website import search_word
from website import analizer
import json

def index(request):
    # Get the context from the request
    context = RequestContext(request)

    # Return a rendered response to send to the client.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('index.html', context)

def show(request):
    # Get the context from the request
    context = RequestContext(request)
    
    # Check if it is POST method
    if request.method == 'POST':
        # open file and read from it
        with open('test_fails(10r).json', encoding='utf-8') as f:
            # transfer json elements to python elements
            document = json.load(f)

        # data get result from search function
        # Search function looks for input word in document(variable, wich contains jason converted to python)
        data = search_word.search_word(document, request.POST['input_word'])

        # Calls analizer function
        # output_data = analizer.analizer(data)

        # Function returns word and data for outputing on screen
        context_dict = search_word.return_centext_dict(data, request.POST['input_word'])

    # Return a rendered response to send to the client.
    return render_to_response('show.html', context_dict, context)
