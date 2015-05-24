# -*- coding: utf-8 -*-
# Function for outputing grammer
def grammer(input_data):
    output = u'<div class="grammer"><p><b1>Gramatika:</b1></p><div class="inside_box">'
    try:
        for f in input_data[u'Flags']:
            output = output + u'<p>' + f + u'</p>'
    except Exception as inst:
        pass
    try:
        if input_data[u'Leftovers']:
            if input_data[u'Original']:
                output = output + u'<p><b1>Oriģināls: </b1>' + input_data[u'Original'] + u'</p>'
    except Exception as inst:
        pass
##    try:
##        if input_data[u'Paradigm']:
##            output = output + u'<p><b1>Pradigmas:</b1></p>'
##        for p in input_data[u'Paradigm']:
##            output = output + u'<p class="inside_box">' + p + u'</p>'
##    except Exception as inst:
##        pass
    try:
        for k in input_data[u'AltLemmas']:
            output = output + u'<p id="lemma">' + k[u'Lemma'] + u':</p>'
##            for p in k[u'Paradigm']:
##                output = output + u'<p class="inside_box">' + p + u'</p>'
            output = output + u'<div class="grammer"><p><b1>Gramatika:</b1></p>'
            for f in k[u'Flags']:
                output = output + u'<p class="double_inside_box">' + f + u'</p>'
            output = output + u'</div>'
    except Exception as inst:
        pass
    output = output + u'</div></div>'
    return output
