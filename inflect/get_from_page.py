import requests
import json
from inflect import verb_analizer
from website import unknown_analizer
from website import noun_analizer
from website import adjective_analizer
from website import unrecognized_part_of_speech

def phonetic_transcriber(input_word):
    url = 'http://ezis.ailab.lv:8182/phonetic_transcriber/' + input_word + '?phoneme_set=ipa'
    retuned_element = requests.get(url)
    phonetic_word = retuned_element.text
    phonetic_word = phonetic_word.replace(" ", "")
    if phonetic_word == "Unrecognizedsymbolsinstring!":
        phonetic_word = "Vārda izruna netiek ģenerēta!"
    return phonetic_word

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
    numeral = []
    leftower = []
    for elem in input_data:
        #Piefiksē, kas par vārdškiru ir meklētajam vārdam
        try:
            for line in elem:
                if line['Vārds'] == input_word:
                    vardskira = line['Vārdšķira']
                    break
        except Exception as inst:
            pass
        
        #Iedala vārdus pēc vārdškirām
        try:
            for line in elem:
                if line['Vārdšķira'] == "Lietvārds":
                    noun.append(line)
                    if vardskira != line['Vārdšķira']:
                        auto_gen = "ir"
                elif line['Vārdšķira'] == "Apstākļa vārds":
                    adverb.append(line)
                    if vardskira != line['Vārdšķira']:
                        auto_gen = "ir"
                elif line['Vārdšķira'] == "Īpašības vārds":
                    adjective.append(line)
                    if vardskira != line['Vārdšķira']:
                        auto_gen = "ir"
                elif line['Vārdšķira'] == "Darbības vārds":
                    verb.append(line)
                    if vardskira != line['Vārdšķira']:
                        auto_gen = "ir"
                elif line['Vārdšķira'] == "Vietniekvārds":
                    pronoun.append(line)
                    if vardskira != line['Vārdšķira']:
                        auto_gen = "ir"
                elif line['Vārdšķira'] == "Saīsinājums":
                    abbreviation.append(line)
                    if vardskira != line['Vārdšķira']:
                        auto_gen = "ir"
                elif line['Vārdšķira'] == "Izsauksmes vārds":
                    interjection.append(line)
                    if vardskira != line['Vārdšķira']:
                        auto_gen = "ir"
                elif line['Vārdšķira'] == "Reziduālis":
                    residual.append(line)
                    if vardskira != line['Vārdšķira']:
                        auto_gen = "ir"
                elif line['Vārdšķira'] == "Pieturzīme":
                    punctuation_mark.append(line)
                    if vardskira != line['Vārdšķira']:
                        auto_gen = "ir"
                elif line['Vārdšķira'] == "Skaitļa vārds":
                    numeral.append(line)
                    if vardskira != line['Vārdšķira']:
                        auto_gen = "ir"
                else:
                    leftower.append(line)
        except Exception as inst:
            pass

        if leftower != []:
            unrecognized_part_of_speech.unrecognized(leftower)

        #Checkbox, lai varētu nerādīt visus atvasinātajām vārdškirām piederošos vārdus
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
                if (abbreviation != []) and (vardskira != "Saīsinājums"):
                    output = output + """<div class="check_box"><label><input type="checkbox" value="abbreviation" checked> Saīsinājumi</label><br></div>"""
                if (interjection != []) and (vardskira != "Izsauksmes vārds"):
                    output = output + """<div class="check_box"><label><input type="checkbox" value="interjection" checked> Izsauksmes vārdi</label><br></div>"""
                if (residual != []) and (vardskira != "Reziduālis"):
                    output = output + """<div class="check_box"><label><input type="checkbox" value="residual" checked> Reziduāļi</label><br></div>"""
                if (punctuation_mark != []) and (vardskira != "Pieturzīme"):
                    output = output + """<div class="check_box"><label><input type="checkbox" value="punctuation_mark" checked> Pieturzīmes</label><br></div>"""
                if (numeral != []) and (vardskira != "Skaitļa vārds"):
                    output = output + """<div class="check_box"><label><input type="checkbox" value="numeral" checked> Skaitļa vārds</label><br></div>"""
                if leftower != []:
                    output = output + """<div class="check_box"><label><input type="checkbox" value="leftower" checked> Citi</label><br></div>"""
                output = output + """<br></div></div>"""
        except Exception as inst:
            pass
        
        #Pirmos izvada meklētā vārda locījumus (piederošus meklētā vārda vārdškirai), katrai vārdškirai ir sava funkcija, kas apstrādā tai piederošos datus
        output = output + '<table>'
        try:
            if (noun != []) and (vardskira == "Lietvārds"):
                output = output + """<tr><td><h2>Lietvārds</h2>""" + noun_analizer.noun_analizer(noun) + '</td></tr>'
                noun = []
            elif (adverb != []) and (vardskira == "Apstākļa vārds"):
                output = output + """<tr><td><h2>Apstākļa vārds</h2><div class="inside_box">""" + unknown_analizer.unknown_analizer(adverb, ["Vārdšķira"]) + "</div><br></td></tr>"
                adverb = []
            elif (adjective != []) and (vardskira == "Īpašības vārds"):
                output = output + """<tr><td><h2>Īpašības vārds</h2>""" + adjective_analizer.adjective_analizer(adjective) + '</td></tr>'
                adjective = []
            elif (verb != []) and (vardskira == "Darbības vārds"):
                output = output + """<tr><td><h2>Darbības vārds</h2>""" + verb_analizer.verb_analizer(verb) + '</td></tr>'
                verb = []
            elif (pronoun != []) and (vardskira == "Vietniekvārds"):
                output = output + """<tr><td><h2>Vietniekvārds</h2><div class="inside_box">""" + unknown_analizer.unknown_analizer(pronoun, ["Vārdšķira"]) + "</div><br></td></tr>"
                pronoun = []
            elif (abbreviation != []) and (vardskira == "Saīsinājums"):
                output = output + """<tr><td><h2>Saīsinājums</h2><div class="inside_box">""" + unknown_analizer.unknown_analizer(abbreviation, ["Vārdšķira"]) + "</div><br></td></tr>"
                abbreviation = []
            elif (interjection != []) and (vardskira == "Izsauksmes vārds"):
                output = output + """<tr><td><h2>Izsauksmes vārds</h2><div class="inside_box">""" + unknown_analizer.unknown_analizer(interjection, ["Vārdšķira"]) + "</div><br></td></tr>"
                interjection = []
            elif (residual != []) and (vardskira == "Reziduālis"):
                output = output + """<tr><td><h2>Reziduālis</h2><div class="inside_box">""" + unknown_analizer.unknown_analizer(residual, ["Vārdšķira"]) + "</div><br></td></tr>"
                residual = []
            elif (punctuation_mark != []) and (vardskira == "Pieturzīme"):
                output = output + """<tr><td><h2>Pieturzīme</h2><div class="inside_box">""" + unknown_analizer.unknown_analizer(punctuation_mark, ["Vārdšķira"]) + "</div><br></td></tr>"
                punctuation_mark = []
            elif (numeral != []) and (vardskira == "Skaitļa vārds"):
                output = output + """<tr><td><h2>Skaitļa vārds</h2>""" + adjective_analizer.dzimtes_analizer(numeral, ["Vārdšķira"]) + '</td></tr>'
                numeral = []
            elif leftower != []:
                for line in leftower:
                    output = output + """<tr><td><h2>""" + line['Vārdšķira'] + """</h2><div class="inside_box">""" + unknown_analizer.unknown_analizer(leftower, ["Vārdšķira"]) + "</div></td></tr><br>"
                    break
                leftower = []
        except Exception as inst:
            pass
        output = output + '</table>'
        
        #Aiz meklētā vārda locījumiem izvada automātiski atvasinātos locijumus
        if auto_gen == "ir":
            output = output + """<div class="auto_gen_atvasin"><h2>Automātiski ģenerēti atvasināti vārdi</h2><div class="inside_box">"""
            output = output + '<table>'
            try:
                if noun != []:
                    output = output + """<tr><td><div class="noun"><h2>Lietvārds</h2>""" + noun_analizer.noun_analizer(noun) + """</div></td></tr>"""
                if adverb != []:
                    output = output + """<tr><td><div class="adverb"><h2>Apstākļa vārds</h2>""" + unknown_analizer.unknown_analizer(adverb, ["Vārdšķira"]) + """</div></td></tr>"""
                if adjective != []:
                    output = output + """<tr><td><div class="adjective"><h2>Īpašības vārds</h2>""" + adjective_analizer.adjective_analizer(adjective) + """</div></td></tr>"""
                if verb != []:
                    output = output + """<tr><td><div class="verb"><h2>Darbības vārds</h2>""" + verb_analizer.verb_analizer(verb) + """</div></td></tr>"""
                if pronoun != []:
                    output = output + """<tr><td><div class="pronoun"><h2>Vietniekvārds</h2>""" + unknown_analizer.unknown_analizer(pronoun, ["Vārdšķira"]) + """</div></td></tr>"""
                if abbreviation != []:
                    output = output + """<tr><td><div class="abbreviation"><h2>Saīsinājums</h2>""" + unknown_analizer.unknown_analizer(abbreviation, ["Vārdšķira"]) + """</div></td></tr>"""
                if interjection != []:
                    output = output + """<tr><td><div class="interjection"><h2>Izsauksmes vārds</h2>""" + unknown_analizer.unknown_analizer(interjection, ["Vārdšķira"]) + """</div></td></tr>"""
                if residual != []:
                    output = output + """<tr><td><div class="residual"><h2>Reziduālis</h2>""" + unknown_analizer.unknown_analizer(residual, ["Vārdšķira"]) + """</div></td></tr>"""
                if punctuation_mark != []:
                    output = output + """<tr><td><div class="punctuation_mark"><h2>Pieturzīme</h2>""" + unknown_analizer.unknown_analizer(punctuation_mark, ["Vārdšķira"]) + """</div></td></tr>"""
                if numeral != []:
                    output = output + """<tr><td><div class="numeral"><h2>Skaitļa Vārds</h2>""" + adjective_analizer.dzimtes_analizer(numeral, ["Vārdšķira"]) + """</div></td></tr>"""
                if leftower != []:
                    for line in leftower:
                        output = output + """<tr><td><div class="leftower"><h2>Citi</h2>""" + unknown_analizer.unknown_analizer(leftower) + """</div></td></tr>"""
                        break
            except Exception as inst:
                pass
            output = output + '</table>'
            output = output + """</div></div>"""

        return output
