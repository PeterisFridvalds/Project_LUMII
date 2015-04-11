import requests
import json
from website import noun_analizer
from website import adverb_analizer
from website import verb_analizer
##from website import pronoun_analizer

def phonetic_transcriber(input_word):
    url = 'http://ezis.ailab.lv:8182/phonetic_transcriber/' + input_word + '?phoneme_set=ipa'
    retuned_element = requests.get(url)
    phonetic_word = retuned_element.text
    return phonetic_word.replace(" ", "")

def inflect_word(input_word):
    url = 'http://ezis.ailab.lv:8182/inflect/json/lv/' + input_word
    retuned_element = requests.get(url)
    infleted_word = json.loads(retuned_element.text)
    return inflect_analizer(infleted_word, input_word)

def inflect_analizer(input_data, input_word):
    output = """<p class="pronunciation"><b1>Izruna: </b1>""" + phonetic_transcriber(input_word) + """</p><br>"""
    vardskira = ""
    noun = []
    adverb = []
    verb = []
    pronoun = []
##    adjective = []
##    abbreviation = []
##    punctuation_mark = []
##    interjection = []
##    residual = []
    for elem in input_data:
        try:
            for line in elem:
                if line['Vārds'] == input_word:
                    vardskira.append(line['Vārdšķira'])
                    break
        except Exception as inst:
            pass
        try:
            for line in elem:
##                if line['Vārdšķira'] == "Lietvārds":
##                    noun.append(line)
##                if (line['Vārdšķira'] == "Apstākļa vārds") or (line['Vārdšķira'] == "Īpašības vārds"):
##                    adverb.append(line)
                if line['Vārdšķira'] == "Darbības vārds":
                    verb.append(line)
##                if line['Vārdšķira'] == "Vietniekvārds":
##                    pronoun.append(line)
        except Exception as inst:
            pass
        try:
            if noun != []:
                output = output + """<h2>Lietvārda locījumi</h2>""" + noun_analizer.noun_analizer(noun)
        except Exception as inst:
            pass
        try:
            if adverb != []:
                output = output + """<h2>Apstākļa vārda locījumi</h2>""" + adverb_analizer.adverb_analizer(adverb)
        except Exception as inst:
            pass
        try:
            if verb != []:
                output = output + """<h2>Darbības vārda locījumi</h2>""" + verb_analizer.verb_analizer(verb)
        except Exception as inst:
            pass
        try:
            if pronoun != []:
                output = output + """<h2>Darbības vārda locījumi</h2>""" + pronoun_analizer.pronoun_analizer(pronoun)
        except Exception as inst:
            pass
        return output
        
