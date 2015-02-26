from website import grammer
from website import senses
from website import phrases

# Function for outputing all data about input word
def analizer(input_data):
    output = """<h1>""" + input_data['Header']['Lemma'] + """</h1>"""
    try:
        if i['Header']['Gram']:
            output = output + """<p>""" + grammer.grammer(i['Header']['Gram']) + """</p>"""
    except Exception as inst:
          pass
    try:
        if input_data['ID']:
            output = output + """<p>ID: """ + input_data['ID'] + """</p>"""
    except Exception as inst:
        pass
    try:
        for s in input_data['Senses']:
            output = output + """<p>""" + senses.sense(s) + """</p>"""
    except Exception as inst:
        pass
    try:
        for p in input_data['Phrases']['Phrase']:
            output = output + """<p class="inside_box">""" + phrases.phrase(p) + """</p>"""
    except Exception as inst:
        pass
    try:
        output = output + """<p>Avoti:</p>"""
        for source in input_data['Sources']:
            output = output + """<p class="inside_box">""" + source + """</p>"""
    except Exception as inst:
        pass
    return output

