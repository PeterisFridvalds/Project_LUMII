# -*- coding: utf-8 -*-
from tezaurs import grammer
from tezaurs import senses

# Function for outputing all data about input word
def analizer(input_data):
    output = u'<h3>' + input_data[u'Header'][u'Lemma']
    try:
        if input_data[u'ID']:
            if input_data[u'ID'] != "0":
                output = output + u'<sup><b1 style="font-size:15px">' + input_data[u'ID'] + u'</b1></sup>'
    except Exception as inst:
        pass
    try:
        if input_data[u'Header'][u'Pronunciation']:
            pronunciation_out = u'<b1 class="pronunciation">- <b2><b1> Izruna: </b1>'
            for elem in input_data[u'Header'][u'Pronunciation']:
                pronunciation_out = pronunciation_out + elem + u'; '
            pronunciation_out = pronunciation_out + u'end of pronunciation list'
            pronunciation_out = pronunciation_out.replace(u'; end of pronunciation list', u'</b2></b1>')
            output = output + pronunciation_out
    except Exception as inst:
          pass
    output = output + u'</h3>'
    try:
        if input_data[u'Header'][u'Gram']:
            output = output + grammer.grammer(input_data[u'Header'][u'Gram'])
    except Exception as inst:
          pass
    try:
        if input_data[u'ID']:
            if input_data[u'ID'] != "0":
                output = output + u'<p class="inside_box" style="font-weight:bold;">Homonīms</p>'
    except Exception as inst:
        pass
    try:
        for s in input_data[u'Senses']:
            output = output + u'<div class="senses">' + senses.sense(s) + u'</div>'
    except Exception as inst:
        pass
    try:
        if input_data[u'Phrases']:
            output = output + u'<div class="phrases"><p class="inside_box" id="top_of_list"><b1>Frazeoliģismi:</b1></p><div class="inside_box">'
            for p in input_data[u'Phrases']:
                output = output + senses.phrase(p)
            output = output + u'</div></div>'
    except Exception as inst:
        pass
    try:
        output = output + u'<div class="derivatives">'
        for d in  input_data[u'Derivatives']:
            output = output + analizer(d)
        output = output + u'</div>'
    except Exception as inst:
        pass
    try:
        if input_data[u'Sources']:
            output = output + u'<div class="sources"><p id="top_of_list"><b1>Avoti:</b1></p>'
            for source in input_data[u'Sources']:
                output = output + u'<p class="inside_box"><a href="http://tezaurs.lv/sv/avoti.pdf">' + source + u'</a></p>'
            output = output + u'</div>'
    except Exception as inst:
        pass
    return output

def AltLemmas(input_data, word):
    for i in input_data[u'Header'][u'Gram'][u'AltLemmas']:
        if i[u'Lemma'] == word:
            output = u'<div id="AltLemmas"><h3>' + i[u'Lemma'] + u'</h3>'
            output = output + grammer.grammer(i)
            break
    output = output + u'<br><p>Sīkāk skatīt pie <a href="/tezaurs/' + input_data[u'Header'][u'Lemma'] + '/' + input_data[u'ID'] +'"><b1>' + input_data[u'Header'][u'Lemma'] + u'</b1></a></p></div>'
    return output

def Derivatives(input_data, word):
    for i in input_data[u'Derivatives']:
        if i[u'Header'][u'Lemma'] == word:
            output = analizer(i)
            break
    output = output + u'<br><p>Sīkāk skatīt pie <a href="/tezaurs/' + input_data[u'Header'][u'Lemma'] + '/' + input_data[u'ID'] +'"><b1>' + input_data[u'Header'][u'Lemma'] + u'</b1></p>'
    return output
