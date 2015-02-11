from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Get the context from the request
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key content is the same as {{ content }} in the template!
    context_dict = {'content':"content"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('index.html', context_dict, context)
