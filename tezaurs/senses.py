# -*- coding: utf-8 -*-
from tezaurs import grammer

# Function for outputing senses
def sense(input_data):
    output = ""
    try:
        if input_data[u'SenseID']:
            output = output + u'<p id="top_of_list"><b1>' + input_data[u'SenseID'] + u'. nozīme — ' + u'</b1>'
    except Exception as inst:
        pass
    try:
        if input_data[u'Gloss']:
            output = output + input_data[u'Gloss'] + u'</p>'
    except Exception as inst:
        pass
    try:
        if input_data[u'Gram']:
            output = output + grammer.grammer(input_data[u'Gram'])
    except Exception as inst:
        pass 
    try:
        if input_data[u'SenseID']:
            output = output + u'<div class="inside_box">'
    except Exception as inst:
        pass 
    try:
        if input_data[u'Examples']:
            output = output + u'<div class="examples"><p><b1>Piemēri:</b1></p>'
            for e in input_data[u'Examples']:
                output = output + phrase(e)
            output = output + u'</div>'
    except Exception as inst:
        pass
    try:
        if input_data[u'Senses']:
            output = output + u'<div class="subsenses"><p id="top_of_list"><b1>Apakšnozīmes:</b1></p><div class="inside_box">'
            for s in input_data[u'Senses']:
                output = output + sense(s)
            output = output + u'</div></div>'
    except Exception as inst:
        pass
    try:
        if input_data[u'SenseID']:
            output = output + u'</div>'
    except Exception as inst:
        pass
    return output

# Function for outputing phrases
def phrase(input_data):
    output = u'<div class="inside_box">'
    try:
        if input_data[u'Phrase'][u'Text']:
            output = output + u'<p><b>' + input_data[u'Phrase'][u'Text'] + u' — </b>'
    except Exception as inst:
        pass
    try:
        for s in input_data[u'Phrase'][u'Senses']:
            output = output + sense(s)
    except Exception as inst:
        pass
    try:
        if input_data[u'Phrase'][u'Gram']:
            output = output + grammer.grammer(input_data[u'Phrase'][u'Gram'])
    except Exception as inst:
        pass
    output = output + u'</div>'
    return output

