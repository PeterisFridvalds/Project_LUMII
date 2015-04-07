import requests
import json
from website import noun_analizer
from website import adverb_analizer
from website import verb_analizer

def phonetic_transcriber(input_word):
    url = 'http://ezis.ailab.lv:8182/phonetic_transcriber/' + input_word + '?phoneme_set=ipa'
    retuned_element = requests.get(url)
    phonetic_word = retuned_element.text
    return phonetic_word.replace(" ", "")

def inflect_word(input_word):
    url = 'http://ezis.ailab.lv:8182/inflect/json/lv/' + input_word
    retuned_element = requests.get(url)
    infleted_word = json.loads(retuned_element.text)
    return inflect_analizer(infleted_word)

def inflect_analizer(input_data):
    output = ""
    noun = []
    adverb = []
    verb = []
##    adjective = []
##    pronoun = []
##    abbreviation = []
##    punctuation_mark = []
##    interjection = []
##    residual = []
    for elem in input_data:
        try:
            for line in elem:
                output = """<p class="pronunciation"><b1>Izruna: </b1>""" + phonetic_transcriber(line['Vārds']) + """</p><br>"""
                break
        except Exception as inst:
            pass
        try:
            for line in elem:
                if line['Vārdšķira'] == "Lietvārds":
                    noun.append(line)
                if line['Vārdšķira'] == "Apstākļa vārds":
                    adverb.append(line)
                if line['Vārdšķira'] == "Darbības vārds":
                    verb.append(line)
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
        return output
        
