# -*- coding: utf-8 -*-
import json
import codecs

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
                with codecs.open('Paradigmas.json', encoding='utf-8') as f:
                    # transfer json elements to python elements
                    try:
                        document = json.load(f)
                    except Exception as inst:
                        document = []
            except Exception as inst:
                document = []
    return document

## Funkcija, ka pārbauda vai atmiņā ir ielādēta informācija par avotiem, ja nav, tad to ielādē
def sources_init():
    try:
        sources
    except Exception as inst:
        global sources
        sources = []
        if sources == []:
            # open file and read from it
            try:
                with codecs.open('tezaurs-sources.json', encoding='utf-8') as f:
                    # transfer json elements to python elements
                    try:
                        sources = json.load(f)
                    except Exception as inst:
                        sourcest = []
            except Exception as inst:
                sources = []
    return sources

## Funkcija, ka pārbauda vai atmiņā ir ielādēta informācija par arodziņiem, ja nav, tad to ielādē
def flags_init():
    try:
        flag_list
    except Exception as inst:
        global flag_list
        flag_list = []
        if flag_list == []:
            # open file and read from it
            try:
                with codecs.open('tezaurs-flags.json', encoding='utf-8') as f:
                    # transfer json elements to python elements
                    try:
                        flag_list = json.load(f)
                    except Exception as inst:
                        flag_list = []
            except Exception as inst:
                flag_list = []
    return flag_list

## Analizatos, kas sagatavos labošanas formu
def analizer(input_data):
    keys = []
    output = u'<div class="inside_box"><h3>' + input_data[u'Header'][u'Lemma'] + u'</h3><div class="inside_box"><div class="inside_box">'
    try:
        if input_data[u'Header'][u'Pronunciation']:
            output = output + u'<p><b1> Izruna: </b1>'
            out = ''
            for pron in input_data[u'Header'][u'Pronunciation']:
                out = out + pron + u'; '
            out = out + u'beigas_seit'
            out = out.replace('; beigas_seit', '')
            output = output + out + u'</p>'
    except Exception as inst:
        pass

    ## Forma škirkļa galvenes gramatikas labošanai
    try:
        if input_data[u'Header'][u'Gram']:
            output = output + u'<p><b1>Gramatika:</b1></p><div class="inside_box">'
            try:
                if input_data[u'Header'][u'Gram'][u'Paradigm']:
                    output = output + u'<div class="btn-group"><button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">Paradigmas <span class="caret"></span></button>'
                    output = output + u'<ul class="dropdown-menu scrollable-menu" role="menu">'
                    doc = document_init()
                    for line in doc:
                        paradigma = False
                        key1 = u'H_G_' + line['ID'] + u'_parad'
                        keys.append(key1)
                        for parad in input_data[u'Header'][u'Gram'][u'Paradigm']:
                            if parad == line['ID']:
                                output = output + u'<li><label style="padding-left:5px"><input type="checkbox" value="' + key1 + '" name="' + key1 + '" checked> ' + line['Description'] + '</label></li>'
                                paradigma = True
                                break
                        if paradigma == False:
                            output = output + u'<li><label style="padding-left:5px"><input type="checkbox" value="' + key1 + '" name="' + key1 + '"> ' + line['Description'] + '</label></li>'
                    output = output + u'</ul>'
                    output = output + u'</div>'
            except Exception as inst:
                pass
            try:
                output = output + u'<div class="btn-group"><button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">Karodziņi <span class="caret"></span></button>'
                output = output + u'<ul class="dropdown-menu scrollable-menu" role="menu">'
                flag_list = flags_init()
                for f in flag_list:
                    fl = False
                    key1 = u'H_G_' + f
                    keys.append(key1)
                    for flag in input_data[u'Header'][u'Gram'][u'Flags']:
                        if flag == f:
                            output = output + u'<li><label style="padding-left:5px"><input type="checkbox" value="' + f + '" name="' + key1 + '" checked> ' + f + '</label></li>'
                            fl = True
                            break
                    if fl == False:
                        output = output + u'<li><label style="padding-left:5px"><input type="checkbox" value="' + f + '" name="' + key1 + '"> ' + f + '</label></li>'
                output = output + u'</ul>'
                output = output + u'</div>'
            except Exception as inst:
                pass
            try:
                if input_data[u'Header'][u'Gram'][u'AltLemmas']:
                    output = output + u'<p><b1>AltLemmas:</b1></p><div class="inside_box">'
                    for altLem in input_data[u'Header'][u'Gram'][u'AltLemmas']:
                        data = AltLemmas(altLem)
                        for key in data[u'keys']:
                            keys.append(key)
                        output = output + data[u'output'] + u'<br>'
                    output = output + u'</div>'
            except Exception as inst:
                pass
            try:
                if input_data[u'Header'][u'Gram'][u'Leftovers']:
                    output = output + u'<p><b1> Leftovers: </b1><input style="width:50%;" type="text" name="H_G_L" value="'
                    keys.append("H_G_L")
                    for leftover in input_data[u'Header'][u'Gram'][u'Leftovers']:
                        out = ''
                        for left in leftover:
                            out = out + left + u'; '
                        out = out + u'beigas_seit'
                        out = out.replace('; beigas_seit', '')
                    output = output + out + u'"></p>'
            except Exception as inst:
                pass
            try:
                if input_data[u'Header'][u'Gram'][u'Original']:
                    output = output + u'<p><b1>Original: </b1>' + input_data[u'Header'][u'Gram'][u'Original'] + u'<p>'
            except Exception as inst:
                pass
    except Exception as inst:
        pass
    output = output + u'</div>'

    ## Forma šķirkļa identifikatora labošanai
    try:
        if input_data[u'ID']:
            output = output + u'<p><b1> ID: </b1><input style="width:50%;" type="text" name="hom_ID" value="' + input_data[u'ID'] + u'"></p>'
            keys.append("hom_ID")
    except Exception as inst:
        pass

    ## Forma šķirkļa nozīmu labošanai
    try:
        if input_data[u'Senses']:
            output = output + u'<p><b1>Nozīmes:</b1></p><div class="inside_box">'
            for s in input_data[u'Senses']:
                data = sense(s)
                for key in data['keys']:
                    keys.append(key)
                output = output + data['output'] + u'<br>'
            output = output + u'</div>'
    except Exception as inst:
        pass
##    try:
##        keys = [u'Phrases']
##        if input_data[u'Phrases']:
##            output = output + u'<p><b1>Frāzes:</b1></p><div class="inside_box">'
##            for p in input_data[u'Phrases']:
##                output = output + phrase(p, keys) + u'<br>'
##            output = output + out + u'</div>'
##    except Exception as inst:
##        pass

    ## Forma atvasināto vārdu labošanai
    try:
        if input_data[u'Derivatives']:
            output = output + u'<p><b1>Atvasinātie vārdi:</b1></p><div class="inside_box">'
            for d in input_data[u'Derivatives']:
                data = derivatives(d)
                for key in data['keys']:
                    keys.append(key)
                output = output + data['output'] + u'<br>'
            output = output + u'</div>'
    except Exception as inst:
        pass

    ## Forma avotu labošanai
    try:
        output = output + u'<div class="btn-group"><button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">Avoti <span class="caret"></span></button>'
        output = output + u'<ul class="dropdown-menu scrollable-menu" role="menu">'
        sources = sources_init()
        for s in sources:
            source = False
            keys.append(s)
            for sour in input_data[u'Sources']:
                if sour == s:
                    output = output + u'<li><label style="padding-left:5px"><input type="checkbox" value="' + s + '" name="' + s + '" checked> ' + s + '</label></li>'
                    source = True
                    break
            if source == False:
                output = output + u'<li><label style="padding-left:5px"><input type="checkbox" value="' + s + '" name="' + s + '"> ' + s + '</label></li>'
        output = output + u'</ul>'
        output = output + u'</div>'
    except Exception as inst:
        pass
    output = output + u'</div></div><br><br><br>'
    return {'output':output, 'keys':keys}

## Funkcija gramatikas labošanas foramas sagatavošanai
def grammer(input_data, key):
    output = ''
    keys = []

    try:
        if input_data[u'Paradigm']:
            output = output + u'<div class="btn-group"><button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">Paradigmas <span class="caret"></span></button>'
            output = output + u'<ul class="dropdown-menu scrollable-menu" role="menu">'
            doc = document_init()
            for line in doc:
                paradigma = False
                key1 = key + u'_' + line['ID'] + u'_parad'
                for parad in input_data[u'Paradigm']:
                    if parad == line['ID']:
                        output = output + u'<li><label style="padding-left:5px"><input type="checkbox" value="' + key1 + '" name="' + key1 + '" checked> ' + line['Description'] + '</label></li>'
                        paradigma = True
                        break
                if paradigma == False:
                    output = output + u'<li><label style="padding-left:5px"><input type="checkbox" value="' + key1 + '" name="' + key1 + '"> ' + line['Description'] + '</label></li>'
                keys.append(key1)
            output = output + u'</ul>'
            output = output + u'</div>'
    except Exception as inst:
         pass
    
    ## Forma karodziņu labošanai
    try:
        output = output + u'<div class="btn-group"><button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">Karodziņi <span class="caret"></span></button>'
        output = output + u'<ul class="dropdown-menu scrollable-menu" role="menu">'
        flag_list = flags_init()
        for f in flag_list:
            fl = False
            key1 = key + f
            keys.append(key1)
            for flag in input_data[u'Flags']:
                if flag == f:
                    output = output + u'<li><label style="padding-left:5px"><input type="checkbox" value="' + f + '" name="' + key1 + '" checked> ' + f + '</label></li>'
                    fl = True
                    break
            if fl == False:
                output = output + u'<li><label style="padding-left:5px"><input type="checkbox" value="' + f + '" name="' + key1 + '"> ' + f + '</label></li>'
        output = output + u'</ul>'
        output = output + u'</div>'
    except Exception as inst:
        pass

    ## Forma pārpalikuma labošanai
    try:
        if input_data[u'Leftovers']:
            key2 = key + u'_L'
            output = output + u'<p><b1> Leftovers: </b1><input style="width:50%;" type="text" name="' + key2 + '" value="'
            for leftover in input_data[u'Leftovers']:
                out = ''
                for left in leftover:
                    out = out + left + u'; '
                out = out + u'beigas_seit'
                out = out.replace('; beigas_seit', '')
            output = output + out + u'"></p>'
            keys.append(key2)
    except Exception as inst:
        pass

    ## Oriģināla izvade
    try:
        if input_data[u'Original']:
            output = output + u'<p><b1>Original: </b1>' + input_data[u'Original'] + u'<p>'
    except Exception as inst:
        pass
    return {'output':output, 'keys': keys}

## Funkcija AltLemmu labošanas formu sagatavošanai
def AltLemmas(input_data):
    keys = []
    output = u'<p><b1>Lemma: </b1>' + input_data[u'Lemma'] + u'</p>'
    try:
        if input_data[u'Paradigm']:
            output = output + u'<div class="btn-group"><button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">Paradigmas <span class="caret"></span></button>'
            output = output + u'<ul class="dropdown-menu scrollable-menu" role="menu">'
            doc = document_init()
            for line in doc:
                paradigma = False
                key1 = input_data[u'Lemma'] + '_' + line['ID'] + u'_parad'
                keys.append(key1)
                for parad in input_data[u'Paradigm']:
                    if parad == line['ID']:
                        output = output + u'<li><label style="padding-left:5px"><input type="checkbox" value="' + key1 + '" name="' + key1 + '" checked> ' + line['Description'] + '</label></li>'
                        paradigma = True
                        break
                if paradigma == False:
                    output = output + u'<li><label style="padding-left:5px"><input type="checkbox" value="' + key1 + '" name="' + key1 + '"> ' + line['Description'] + '</label></li>'
            output = output + u'</ul>'
            output = output + u'</div>'
    except Exception as inst:
         pass
    try:
        output = output + u'<div class="btn-group"><button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">Karodziņi <span class="caret"></span></button>'
        output = output + u'<ul class="dropdown-menu scrollable-menu" role="menu">'
        flag_list = flags_init()
        for f in flag_list:
            fl = False
            key1 = input_data[u'Lemma'] + f
            keys.append(key1)
            for flag in input_data[u'Flags']:
                if flag == f:
                    output = output + u'<li><label style="padding-left:5px"><input type="checkbox" value="' + f + '" name="' + key1 + '" checked> ' + f + '</label></li>'
                    fl = True
                    break
            if fl == False:
                output = output + u'<li><label style="padding-left:5px"><input type="checkbox" value="' + f + '" name="' + key1 + '"> ' + f + '</label></li>'
        output = output + u'</ul>'
        output = output + u'</div>'
    except Exception as inst:
        pass
    return {'output':output, 'keys': keys}

## Funkcija nozīmju labošanas formu sagatavošanai
def sense(input_data):
    keys = []
    output = ''
    try:
        if input_data[u'SenseID']:
            output = output + u'<p><b1>' + input_data[u'SenseID'] + u'. nozīme</b1></p><div class="inside_box">'
            sense_key = input_data[u'SenseID'] + u'_noz'
    except Exception as inst:
        sense_key = "noz"
    try:
        if input_data[u'Gram']:
            output = output + u'<p><b1>Gramatika:</b1></p><div class="inside_box">'
            data = grammer(input_data[u'Gram'], sense_key)
            for key in data['keys']:
                keys.append(key)
            output = output + data['output'] + u'</div>'
    except Exception as inst:
        pass
    try:
        if input_data[u'Gloss']:
            output = output + u'<p><b1> Skaidrojums: </b1><input style="width:50%;" type="text" name="' + sense_key + '" value="' + input_data[u'Gloss'] + u'"></p>'
            keys.append(sense_key)
    except Exception as inst:
        pass
##    if input_key == "":
##        try:
##            if input_data[u'Examples']:
##                output = output + u'<p><b1>Piemēri:</b1></p><div class="inside_box">'
##                for e in input_data[u'Examples']:
##                    data = phrase(e, sense_key)
##                    for k in data['keys']:
##                        keys.append(k)
##                    output = output + data['output'] + u'<br>'
##                output = output + u'</div>'
##        except Exception as inst:
##            pass
##    try:
##        if input_data[u'Senses']:
##            output = output + u'<p><b1>Apakšozīmes:</b1></p><div class="inside_box">'
##            for s in input_data[u'Senses']:
##                output = output + sense(s) + u'<br>'
##            output = output + u'</div>'
##    except Exception as inst:
##        pass
    try:
        if input_data[u'SenseID']:
            output = output + u'</div>'
    except Exception as inst:
        pass
    return {'output':output, 'keys':keys}

## Funkcija piemēru labošanas formas sagatavošanai
##def phrase(input_data, input_key):
##    output = ''
##    keys = []
##    try:
##        if input_data[u'Phrase'][u'Text']:
##            key = input_key + '_' + input_data[u'Phrase'][u'Text'].replace(' ', '_')
##    except Exception as inst:
##        key = input_key + "prase_key"
##    try:
##        if input_data[u'Phrase'][u'Text']:
##            keys.append(key)
##            output = output + u'<p><b1> Teksts: </b1><input type="text" name"' + key + '" value="' + input_data[u'Phrase'][u'Text'] + u'"></p>'
##    except Exception as inst:
##        pass
##    try:
##        if input_data[u'Phrase'][u'Gram']:
##            output = output + u'<p><b1>Gramatika:</b1></p><div class="inside_box">'
##            data = grammer(input_data[u'Phrase'][u'Gram'], key)
##            for k in data['keys']:
##                keys.append(k)
##            output = output + data['output'] + u'</div>'
##    except Exception as inst:
##        pass
##    try:
##        if input_data[u'Phrase'][u'Senses']:
##            output = output + u'<p><b1>nozīmes:</b1></p><div class="inside_box">'
##            skait = 0
##            for s in input_data[u'Phrase'][u'Senses']:
##                skait = sakit + 1
##                input_key = key + '_' + str(skait)
##                out = sense(s, input_key)
##                for k in out['keys']:
##                    keys.append(k)
##                output = output + out['output'] + u'<br>'
##            output = output + u'</div>'
##    except Exception as inst:
##        pass
##    return {'output':output, 'keys':keys}

## Funkcija alternatīvo vārdu labošanas formas sagatavošanai
def derivatives(input_data):
    output = u'<h3>' + input_data[u'Header'][u'Lemma'] + u'</h3><div class="inside_box">'
    keys = []
    key = input_data[u'Header'][u'Lemma']
    try:
        if input_data[u'Header'][u'Pronunciation']:
            output = output + u'<p><b1> Izruna: </b1>'
            out = ''
            for pron in input_data[u'Header'][u'Pronunciation']:
                out = out + pron + u'; '
            out = out + u'beigas_seit'
            out = out.replace('; beigas_seit', '')
            output = output + out + u'</p>'
    except Exception as inst:
        pass
    try:
        if input_data[u'Header'][u'Gram']:
            output = output + u'<p><b1>Gramatika:</b1></p><div class="inside_box">'
            data = grammer(input_data[u'Header'][u'Gram'], key)
            for key in data['keys']:
                keys.append(key)
            output = output + data['output'] + u'</div>'
    except Exception as inst:
        pass
    output = output + u'</div>'
    return {'output':output, 'keys':keys}
        

