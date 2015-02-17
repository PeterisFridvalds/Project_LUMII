from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse

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
        # Put input_word in to content
        context_dict = {'content':request.POST['input_word']}

    # Return a rendered response to send to the client.
    return render_to_response('show.html', context_dict, context)
