import requests
import json

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
    for elem in input_data:
        try:
            for line in elem:
                output = """<p class="pronunciation"><b1>Izruna: </b1>""" + phonetic_transcriber(line['Vārds']) + """</p><br>"""
                break
        except Exception as inst:
            pass
        try:
            for line in elem:
                output = output + """<p>""" + line['Vārdšķira']
                try:
                    if line['Deklinācija']:
                        output = output + ", " + line['Deklinācija'] + """. deklinācija, """ + line['Dzimte'] + """</p><h3 class="inflect">Locījumi</h3>"""
                except Exception as inst:
                    pass
                output = output + """<table class="inflect">"""
                if line['Vārdšķira'] == "Lietvārds":
                    output = output + """<tr><td><b>Locījums</b></td><td><b>Vienskaitlis</b></td><td><b>Daudzskaitlis</b></td></tr>"""
                break
        except Exception as inst:
            pass
        try:
            for line in elem:
                if line['Locījums'] == "Nominatīvs":
                    output = output + """<tr><td><b1>Nominatīvs</b1></td>"""
                break
            for line in elem:
                if line['Locījums'] == "Nominatīvs":
                    output = output + """<td>""" + line['Vārds'] + """</td>"""
            output = output + """</tr><tr><td><b1>Ģenitīvs</b1></td>"""
            for line in elem:
                if line['Locījums'] == "Ģenitīvs":
                    output = output + """<td>""" + line['Vārds'] + """</td>"""
            output = output + """</tr><tr><td><b1>Datīvs</b1></td>"""
            for line in elem:
                if line['Locījums'] == "Datīvs":
                    output = output + """<td>""" + line['Vārds'] + """</td>"""
            output = output + """</tr><tr><td><b1>Akuzatīvs</b1></td>"""
            for line in elem:
                if line['Locījums'] == "Akuzatīvs":
                    output = output + """<td>""" + line['Vārds'] + """</td>"""
            output = output + """</tr><tr><td><b1>Lokatīvs</b1></td>"""
            for line in elem:
                if line['Locījums'] == "Lokatīvs":
                    output = output + """<td>""" + line['Vārds'] + """</td>"""
            output = output + """</tr><tr><td><b1>Vokatīvs</b1></td>"""
            for line in elem:
                if line['Locījums'] == "Vokatīvs":
                    output = output + """<td>""" + line['Vārds'] + """</td>"""
            output = output + """</tr>"""
        except Exception as inst:
            pass
        output = output + """</table>"""
        return output
        
