import requests
import json
from website import table_gen_sk
from website import noun_analizer
from website import adverb_analizer
from website import adjective_analizer
from website import verb_analizer
from website import pronoun_analizer

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
    output = ""
    output = """<p class="pronunciation"><b1>Izruna: </b1>""" + phonetic_transcriber(input_word) + """</p><br>"""
    vardskira = ""
    auto_gen = "nav"
    noun = []
    adverb = []
    adjective = []
    verb = []
    pronoun = []
    abbreviation = []
    punctuation_mark = []
    interjection = []
    residual = []
    for elem in input_data:
        try:
            for line in elem:
                if line['Vārds'] == input_word:
                    vardskira = line['Vārdšķira']
                    break
        except Exception as inst:
            pass
        try:
            for line in elem:
                if line['Vārdšķira'] == "Lietvārds":
                    noun.append(line)
                    if vardskira != line['Vārdšķira']:
                        auto_gen = "ir"
                if line['Vārdšķira'] == "Apstākļa vārds":
                    adverb.append(line)
                    if vardskira != line['Vārdšķira']:
                        auto_gen = "ir"
                if line['Vārdšķira'] == "Īpašības vārds":
                    adjective.append(line)
                    if vardskira != line['Vārdšķira']:
                        auto_gen = "ir"
                if line['Vārdšķira'] == "Darbības vārds":
                    verb.append(line)
                    if vardskira != line['Vārdšķira']:
                        auto_gen = "ir"
                if line['Vārdšķira'] == "Vietniekvārds":
                    pronoun.append(line)
                    if vardskira != line['Vārdšķira']:
                        auto_gen = "ir"
                if line['Vārdšķira'] == "Saīsinājums":
                    abbreviation.append(line)
                    if vardskira != line['Vārdšķira']:
                        auto_gen = "ir"
                if line['Vārdšķira'] == "Izsauksmes vārds":
                    interjection.append(line)
                    if vardskira != line['Vārdšķira']:
                        auto_gen = "ir"
                if line['Vārdšķira'] == "Reziduālis":
                    residual.append(line)
                    if vardskira != line['Vārdšķira']:
                        auto_gen = "ir"
                if line['Vārdšķira'] == "Pieturzīme":
                    punctuation_mark.append(line)
                    if vardskira != line['Vārdšķira']:
                        auto_gen = "ir"
        except Exception as inst:
            pass
        try:
            if auto_gen == "ir":
                output = output + """<div class="inside_box"><label><input type="checkbox" value="auto_gen_atvasin" checked> Automātiski ģenerēti atvasināti vārdi</label><br><div class="inside_box">"""
                if (noun != []) and (vardskira != "Lietvārds"):
                    output = output + """<div class="check_box"><label><input type="checkbox" value="noun" checked> Lietvārdi</label><br></div>"""
                if (adverb != []) and (vardskira != "Apstākļa vārds"):
                    output = output + """<div class="check_box"><label><input type="checkbox" value="adverb" checked> Apstākļa vārdi</label><br></div>"""
                if (adjective != []) and (vardskira != "Īpašības vārds"):
                    output = output + """<div class="check_box"><label><input type="checkbox" value="adjective" checked> Īpašības vārdi</label><br></div>"""
                if (verb != []) and (vardskira != "Darbības vārds"):
                    output = output + """<div class="check_box"><label><input type="checkbox" value="verb" checked> Darbības vārdi</label><br></div>"""
                if (pronoun != []) and (vardskira != "Vietniekvārds"):
                    output = output + """<div class="check_box"><label><input type="checkbox" value="pronoun" checked> Vietniekvārdi</label><br></div>"""
                if (pronoun != []) and (vardskira != "Vietniekvārds"):
                    output = output + """<div class="check_box"><label><input type="checkbox" value="abbreviation" checked> Saīsinājumi</label><br></div>"""
                if (pronoun != []) and (vardskira != "Vietniekvārds"):
                    output = output + """<div class="check_box"><label><input type="checkbox" value="interjection" checked> Izsauksmes vārdi</label><br></div>"""
                if (pronoun != []) and (vardskira != "Vietniekvārds"):
                    output = output + """<div class="check_box"><label><input type="checkbox" value="residual" checked> Reziduāļi</label><br></div>"""
                if (pronoun != []) and (vardskira != "Vietniekvārds"):
                    output = output + """<div class="check_box"><label><input type="checkbox" value="punctuation_mark" checked> Pieturzīmes</label><br></div>"""
                output = output + """<br></div></div>"""
        except Exception as inst:
            pass
        try:
            if (noun != []) and (vardskira == "Lietvārds"):
                output = output + """<h2>Lietvārds</h2>""" + noun_analizer.noun_analizer(noun)
                noun = []
            if (adverb != []) and (vardskira == "Apstākļa vārds"):
                output = output + """<h2>Apstākļa vārds</h2>""" + adverb_analizer.adverb_analizer(adverb)
                adverb = []
            if (adjective != []) and (vardskira == "Īpašības vārds"):
                output = output + """<h2>Īpašības vārds</h2>""" + adjective_analizer.adjective_analizer(adjective)
                adjective = []
            if (verb != []) and (vardskira == "Darbības vārds"):
                output = output + """<h2>Darbības vārds</h2>""" + verb_analizer.verb_analizer(verb)
                verb = []
            if (pronoun != []) and (vardskira == "Vietniekvārds"):
                output = output + """<h2>Vietniekvārds</h2>""" + pronoun_analizer.pronoun_analizer(pronoun)
                pronoun = []
            if (abbreviation != []) and (vardskira == "Saīsinājums"):
                output = output + """<h2>Saīsinājums</h2>""" + adverb_analizer.adverb_analizer(abbreviation)
                abbreviation = []
            if (interjection != []) and (vardskira == "Izsauksmes vārds"):
                output = output + """<h2>Izsauksmes vārds</h2>""" + adverb_analizer.adverb_analizer(interjection)
                interjection = []
            if (residual != []) and (vardskira == "Reziduālis"):
                output = output + """<h2>Reziduālis</h2>""" + adverb_analizer.adverb_analizer(residual)
                residual = []
            if (punctuation_mark != []) and (vardskira == "Pieturzīme"):
                output = output + """<h2>Pieturzīme</h2>""" + punctuation_mark_analizer.punctuation_mark_analizer(punctuation_mark)
                punctuation_mark = []
        except Exception as inst:
            pass
        if auto_gen == "ir":
            output = output + """<div class="auto_gen_atvasin"><h2>Automātiski ģenerēti atvasināti vārdi</h2><div class="inside_box">"""
            try:
                if noun != []:
                    output = output + """<div class="noun"><h2>Lietvārds</h2>""" + noun_analizer.noun_analizer(noun) + """</div>"""
                if adverb != []:
                    output = output + """<div class="adverb"><h2>Apstākļa vārds</h2>""" + adverb_analizer.adverb_analizer(adverb) + """</div>"""
                if adjective != []:
                    output = output + """<div class="adjective"><h2>Īpašības vārds</h2>""" + adjective_analizer.adjective_analizer(adjective) + """</div>"""
                if verb != []:
                    output = output + """<div class="verb"><h2>Darbības vārds</h2>""" + verb_analizer.verb_analizer(verb) + """</div>"""
                if pronoun != []:
                    output = output + """<div class="pronoun"><h2>Vietniekvārds</h2>""" + pronoun_analizer.pronoun_analizer(pronoun) + """</div>"""
                if abbreviation != []:
                    output = output + """<div class="abbreviation"><h2>Saīsinājums</h2>""" + adverb_analizer.adverb_analizer(abbreviation) + """</div>"""
                if interjection != []:
                    output = output + """<div class="interjection"><h2>Izsauksmes vārds</h2>""" + adverb_analizer.adverb_analizer(interjection) + """</div>"""
                if residual != []:
                    output = output + """<div class="residual"><h2>Reziduālis</h2>""" + adverb_analizer.adverb_analizer(residual) + """</div>"""
                if punctuation_mark != []:
                    output = output + """<div class="punctuation_mark"><h2>Pieturzīme</h2>""" + punctuation_mark_analizer.punctuation_mark_analizer(punctuation_mark) + """</div>"""
            except Exception as inst:
                pass
            output = output + """</div></div>"""

        return output
