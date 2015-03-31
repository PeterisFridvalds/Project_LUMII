from website import grammer
from website import senses

# Function for outputing all data about input word
def analizer(input_data):
    output = """<h1>""" + input_data['Header']['Lemma']
    try:
        if input_data['ID']:
            if input_data['ID'] != "0":
                output = output + """<sup><b1 style="font-size:15px">""" + input_data['ID'] + """</b1></sup>"""
    except Exception as inst:
        pass
    try:
        if input_data['Header']['Pronunciation']:
            output = output + """ <b1 class="pronunciation">- <b2><b1> Izruna: </b1>""" + input_data['Header']['Pronunciation'] + """</b2></b1>"""
    except Exception as inst:
          pass
    output = output + """</h1>"""
    try:
        if input_data['Header']['Gram']:
            output = output + grammer.grammer(input_data['Header']['Gram'])
    except Exception as inst:
          pass
    try:
        if input_data['ID']:
            if input_data['ID'] != "0":
                output = output + """<p class="inside_box" style="font-weight:bold;">Homonīms</p>"""
    except Exception as inst:
        pass
    try:
        for s in input_data['Senses']:
            output = output + """<div class="senses">""" + senses.sense(s) + """</div>"""
    except Exception as inst:
        pass
    try:
        if input_data['Phrases']:
            output = output + """<div class="phrases"><p class="inside_box" id="top_of_list"><b1>Frazeoliģismi:</b1></p><div class="inside_box">"""
            for p in input_data['Phrases']:
                output = output + senses.phrase(p)
            output = output + """</div></div>"""
    except Exception as inst:
        pass
    try:
        output = output + """<div class="derivatives">"""
        for d in  input_data['Derivatives']:
            output = output + analizer(d)
        output = output + """</div>"""
    except Exception as inst:
        pass
    try:
        if input_data['Sources']:
            output = output + """<div class="sources"><p id="top_of_list"><b1>Avoti:</b1></p>"""
            for source in input_data['Sources']:
                output = output + """<p class="inside_box">""" + source + """</p>"""
            output = output + """</div>"""
    except Exception as inst:
        pass
    return output

def AltLemmas(input_data, data):
    output = """<div id="AltLemmas"><h1>""" + input_data['Lemma'] + """</h1>"""
    output = output + grammer.grammer(input_data)
    output = output + """<br><br><p>Sīkāk skatīt pie <b1>""" + data['Header']['Lemma'] + """</b1></p></div>"""
    return output

def Derivatives(input_data, data):
    output = analizer(input_data)
    output = output + """<br><br><p>Sīkāk skatīt pie <b1>""" + data['Header']['Lemma'] + """</b1></p>"""
    return output
