from website import grammer
from website import senses
##from website import phrases

# Function for outputing all data about input word
def analizer(input_data):
    output = """<h1>""" + input_data['Header']['Lemma'] + """</h1>"""
    try:
        if input_data['Header']['Gram']:
            output = output + grammer.grammer(input_data['Header']['Gram'])
    except Exception as inst:
          pass
    try:
        if input_data['ID']:
            output = output + """<p>ID: """ + input_data['ID'] + """</p>"""
    except Exception as inst:
        pass
    try:
        for s in input_data['Senses']:
            output = output + senses.sense(s)
    except Exception as inst:
        pass
    try:
        for p in input_data['Phrases']['Phrase']:
            output = output + senses.phrase(p)
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
            output = output + """<p>Avoti:</p>"""
        for source in input_data['Sources']:
            output = output + """<p class="inside_box">""" + source + """</p>"""
    except Exception as inst:
        pass
    return output

