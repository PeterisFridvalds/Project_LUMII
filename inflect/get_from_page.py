# -*- coding: utf-8 -*-
import requests
import json
from inflect import speach_service
from inflect import verb_analizer
from inflect import unknown_analizer
from inflect import noun_analizer
from inflect import adjective_analizer
from inflect import unrecognized_part_of_speech

def phonetic_transcriber(input_word):
    url = 'http://ezis.ailab.lv:8182/phonetic_transcriber/' + input_word + '?phoneme_set=ipa'
    try:
        retuned_element = requests.get(url)
    except Exception as inst:
        pass
    try:
        if retuned_element:
            phonetic_word = retuned_element.text
            phonetic_word = phonetic_word.replace(" ", "")
            if phonetic_word == u"Unrecognizedsymbolsinstring!":
                phonetic_word = u"Vārda izruna netiek ģenerēta!"
            return phonetic_word
    except Exception as inst:
        pass
    return u'Izrunas serviss pašlaik nestrādā!'

def inflect_word(input_word, speach_id, locit = True, runa = True):
    url = 'http://ezis.ailab.lv:8182/inflect/json/lv/' + input_word
    output = ''
    phonetic_word = phonetic_transcriber(input_word)
    if phonetic_word != u'Vārda izruna netiek ģenerēta!':
        if phonetic_word != u'Izrunas serviss pašlaik nestrādā!':
            output = '<p class="pronunciation"><b1>Izruna: </b1>' + phonetic_word + '</p><br>'
        else:
            output = u'<p>' + phonetic_word + u'</p>'
    else:
        output = u'<p>' + phonetic_word + u'</p>'
    if runa == True:
        if speach_id != u'-1':
            try:
                output = output + speach_service.return_link(speach_id)
            except Exception as inst:
                pass
    try:
        retuned_element = requests.get(url)
    except Exception as inst:
        pass
    try:
        if retuned_element:
            infleted_word = json.loads(retuned_element.text)
            return output + inflect_analizer(infleted_word, input_word, locit)
    except Exception as inst:
        pass
    return output + u'<p>Locīšanas serviss pašlaik nav pieejams</p>'

def inflect_analizer(input_data, input_word, locit):
    output = ''
    if locit != True:
        output = output + u'Šis vārds netiek locīts!'
        return output
    vardskira = ''
    auto_gen = False
    noun = []
    adverb = []
    adjective = []
    verb = []
    pronoun = []
    abbreviation = []
    punctuation_mark = []
    interjection = []
    residual = []
    numeral = []
    leftower = []
    for elem in input_data:
        #Piefiksē, kas par vārdškiru ir meklētajam vārdam
        try:
            for line in elem:
                if line[u'Vārds'] == input_word:
                    vardskira = line[u'Vārdšķira']
                    break
        except Exception as inst:
            pass
        
        #Sadala vārdus pēc vārdškirām
        try:
            for line in elem:
                if line[u'Vārdšķira'] == u"Lietvārds":
                    noun.append(line)
                    if vardskira != line[u'Vārdšķira']:
                        auto_gen = True
                elif line[u'Vārdšķira'] == u"Apstākļa vārds":
                    adverb.append(line)
                    if vardskira != line[u'Vārdšķira']:
                        auto_gen = True
                elif line[u'Vārdšķira'] == u"Īpašības vārds":
                    adjective.append(line)
                    if vardskira != line[u'Vārdšķira']:
                        auto_gen = True
                elif line[u'Vārdšķira'] == u"Darbības vārds":
                    verb.append(line)
                    if vardskira != line[u'Vārdšķira']:
                        auto_gen = True
                elif line[u'Vārdšķira'] == u"Vietniekvārds":
                    pronoun.append(line)
                    if vardskira != line[u'Vārdšķira']:
                        auto_gen = True
                elif line[u'Vārdšķira'] == u"Saīsinājums":
                    abbreviation.append(line)
                    if vardskira != line[u'Vārdšķira']:
                        auto_gen = True
                elif line[u'Vārdšķira'] == u"Izsauksmes vārds":
                    interjection.append(line)
                    if vardskira != line[u'Vārdšķira']:
                        auto_gen = True
                elif line[u'Vārdšķira'] == u"Reziduālis":
                    residual.append(line)
                    if vardskira != line[u'Vārdšķira']:
                        auto_gen = True
                elif line[u'Vārdšķira'] == u"Pieturzīme":
                    punctuation_mark.append(line)
                    if vardskira != line[u'Vārdšķira']:
                        auto_gen = True
                elif line[u'Vārdšķira'] == u"Skaitļa vārds":
                    numeral.append(line)
                    if vardskira != line[u'Vārdšķira']:
                        auto_gen = True
                else:
                    leftower.append(line)
        except Exception as inst:
            pass

        if leftower != []:
            unrecognized_part_of_speech.unrecognized(leftower)

        #Checkbox, lai varētu nerādīt visus atvasinātajām vārdškirām piederošos vārdus
        try:
            if auto_gen == True:
                output = output + u'<div class="inside_box"><label><input type="checkbox" value="auto_gen_atvasin" checked> Automātiski ģenerēti atvasināti vārdi</label><div class="inside_box">'
                if (noun != []) and (vardskira != u"Lietvārds"):
                    output = output + u'<div class="check_box"><label><input type="checkbox" value="noun" checked> Lietvārdi</label></div>'
                if (adverb != []) and (vardskira != u"Apstākļa vārds"):
                    output = output + u'<div class="check_box"><label><input type="checkbox" value="adverb" checked> Apstākļa vārdi</label></div>'
                if (adjective != []) and (vardskira != u"Īpašības vārds"):
                    output = output + u'<div class="check_box"><label><input type="checkbox" value="adjective" checked> Īpašības vārdi</label></div>'
                if (verb != []) and (vardskira != u"Darbības vārds"):
                    output = output + u'<div class="check_box"><label><input type="checkbox" value="verb" checked> Darbības vārdi</label></div>'
                if (pronoun != []) and (vardskira != u"Vietniekvārds"):
                    output = output + u'<div class="check_box"><label><input type="checkbox" value="pronoun" checked> Vietniekvārdi</label></div>'
                if (abbreviation != []) and (vardskira != u"Saīsinājums"):
                    output = output + u'<div class="check_box"><label><input type="checkbox" value="abbreviation" checked> Saīsinājumi</label></div>'
                if (interjection != []) and (vardskira != u"Izsauksmes vārds"):
                    output = output + u'<div class="check_box"><label><input type="checkbox" value="interjection" checked> Izsauksmes vārdi</label></div>'
                if (residual != []) and (vardskira != u"Reziduālis"):
                    output = output + u'<div class="check_box"><label><input type="checkbox" value="residual" checked> Reziduāļi</label></div>'
                if (punctuation_mark != []) and (vardskira != u"Pieturzīme"):
                    output = output + u'<div class="check_box"><label><input type="checkbox" value="punctuation_mark" checked> Pieturzīmes</label></div>'
                if (numeral != []) and (vardskira != u"Skaitļa vārds"):
                    output = output + u'<div class="check_box"><label><input type="checkbox" value="numeral" checked> Skaitļa vārds</label></div>'
                if leftower != []:
                    output = output + u'<div class="check_box"><label><input type="checkbox" value="leftower" checked> Citi</label></div>'
                output = output + u'<br></div></div>'
        except Exception as inst:
            pass
        
        #Pirmos izvada meklētā vārda locījumus (piederošus meklētā vārda vārdškirai), katrai vārdškirai ir sava funkcija, kas apstrādā tai piederošos datus
        output = output + u'<table>'
        try:
            if (noun != []) and (vardskira == u"Lietvārds"):
                output = output + u'<tr><td><h2>Lietvārds</h2>' + noun_analizer.noun_analizer(noun) + u'</td></tr>'
                noun = []
            elif (adverb != []) and (vardskira == u"Apstākļa vārds"):
                output = output + u'<tr><td><h2>Apstākļa vārds</h2><div class="inside_box">' + unknown_analizer.unknown_analizer(adverb, ["Vārdšķira"]) + u'</div><br></td></tr>'
                adverb = []
            elif (adjective != []) and (vardskira == u"Īpašības vārds"):
                output = output + u'<tr><td><h2>Īpašības vārds</h2>' + adjective_analizer.adjective_analizer(adjective) + u'</td></tr>'
                adjective = []
            elif (verb != []) and (vardskira == u"Darbības vārds"):
                output = output + u'<tr><td><h2>Darbības vārds</h2>' + verb_analizer.verb_analizer(verb) + u'</td></tr>'
                verb = []
            elif (pronoun != []) and (vardskira == u"Vietniekvārds"):
                output = output + u'<tr><td><h2>Vietniekvārds</h2><div class="inside_box">' + unknown_analizer.unknown_analizer(pronoun, ["Vārdšķira"]) + u'</div><br></td></tr>'
                pronoun = []
            elif (abbreviation != []) and (vardskira == u"Saīsinājums"):
                output = output + u'<tr><td><h2>Saīsinājums</h2><div class="inside_box">' + unknown_analizer.unknown_analizer(abbreviation, ["Vārdšķira"]) + u'</div><br></td></tr>'
                abbreviation = []
            elif (interjection != []) and (vardskira == u"Izsauksmes vārds"):
                output = output + u'<tr><td><h2>Izsauksmes vārds</h2><div class="inside_box">' + unknown_analizer.unknown_analizer(interjection, ["Vārdšķira"]) + u'</div><br></td></tr>'
                interjection = []
            elif (residual != []) and (vardskira == u"Reziduālis"):
                output = output + u'<tr><td><h2>Reziduālis</h2><div class="inside_box">' + unknown_analizer.unknown_analizer(residual, ["Vārdšķira"]) + u'</div><br></td></tr>'
                residual = []
            elif (punctuation_mark != []) and (vardskira == u"Pieturzīme"):
                output = output + u'<tr><td><h2>Pieturzīme</h2><div class="inside_box">' + unknown_analizer.unknown_analizer(punctuation_mark, ["Vārdšķira"]) + u'</div><br></td></tr>'
                punctuation_mark = []
            elif (numeral != []) and (vardskira == u"Skaitļa vārds"):
                output = output + u'<tr><td><h2>Skaitļa vārds</h2>' + adjective_analizer.dzimtes_analizer(numeral, ["Vārdšķira"]) + u'</td></tr>'
                numeral = []
            elif leftower != []:
                for line in leftower:
                    output = output + u'<tr><td><h2>' + line[u'Vārdšķira'] + u'</h2><div class="inside_box">' + unknown_analizer.unknown_analizer(leftower, ["Vārdšķira"]) + u'</div></td></tr><br>'
                    break
                leftower = []
        except Exception as inst:
            pass
        output = output + u'</table>'
        
        #Aiz meklētā vārda locījumiem izvada automātiski atvasinātos locijumus
        if auto_gen == True:
            output = output + u'<div class="auto_gen_atvasin"><h2>Automātiski ģenerēti atvasināti vārdi</h2><div class="inside_box">'
            output = output + u'<table>'
            try:
                if noun != []:
                    output = output + u'<tr><td><div class="noun"><h2>Lietvārds</h2>' + noun_analizer.noun_analizer(noun) + u'</div></td></tr>'
                if adverb != []:
                    output = output + u'<tr><td><div class="adverb"><h2>Apstākļa vārds</h2>' + unknown_analizer.unknown_analizer(adverb, ["Vārdšķira"]) + u'</div></td></tr>'
                if adjective != []:
                    output = output + u'<tr><td><div class="adjective"><h2>Īpašības vārds</h2>' + adjective_analizer.adjective_analizer(adjective) + u'</div></td></tr>'
                if verb != []:
                    output = output + u'<tr><td><div class="verb"><h2>Darbības vārds</h2>' + verb_analizer.verb_analizer(verb) + u'</div></td></tr>'
                if pronoun != []:
                    output = output + u'<tr><td><div class="pronoun"><h2>Vietniekvārds</h2>' + unknown_analizer.unknown_analizer(pronoun, ["Vārdšķira"]) + u'</div></td></tr>'
                if abbreviation != []:
                    output = output + u'<tr><td><div class="abbreviation"><h2>Saīsinājums</h2>' + unknown_analizer.unknown_analizer(abbreviation, ["Vārdšķira"]) + u'</div></td></tr>'
                if interjection != []:
                    output = output + u'<tr><td><div class="interjection"><h2>Izsauksmes vārds</h2>' + unknown_analizer.unknown_analizer(interjection, ["Vārdšķira"]) + u'</div></td></tr>'
                if residual != []:
                    output = output + u'<tr><td><div class="residual"><h2>Reziduālis</h2>' + unknown_analizer.unknown_analizer(residual, ["Vārdšķira"]) + u'</div></td></tr>'
                if punctuation_mark != []:
                    output = output + u'<tr><td><div class="punctuation_mark"><h2>Pieturzīme</h2>' + unknown_analizer.unknown_analizer(punctuation_mark, ["Vārdšķira"]) + u'</div></td></tr>'
                if numeral != []:
                    output = output + u'<tr><td><div class="numeral"><h2>Skaitļa Vārds</h2>' + adjective_analizer.dzimtes_analizer(numeral, ["Vārdšķira"]) + u'</div></td></tr>'
                if leftower != []:
                    for line in leftower:
                        output = output + u'<tr><td><div class="leftower"><h2>Citi</h2>' + unknown_analizer.unknown_analizer(leftower) + u'</div></td></tr>'
                        break
            except Exception as inst:
                pass
            output = output + u'</table>'
            output = output + u'</div></div>'

    return output
