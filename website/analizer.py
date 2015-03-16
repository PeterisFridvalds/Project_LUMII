from website import grammer
from website import senses

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
            output = output + """<p class="inside_box">ID: """ + input_data['ID'] + """</p>"""
    except Exception as inst:
        pass
    try:
        for s in input_data['Senses']:
            output = output + """<div class="senses">""" + senses.sense(s) + """</div>"""
    except Exception as inst:
        pass
    try:
        if input_data['Phrases']:
            output = output + """<p class="inside_box" id="top_of_list"><b1>Frazeoliģismi:</b1></p><div class="inside_box">"""
            for p in input_data['Phrases']:
                output = output + senses.phrase(p)
            output = output + """</div>"""
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
            output = output + """<p id="top_of_list"><b1>Avoti:</b1></p>"""
        for source in input_data['Sources']:
            output = output + """<p class="inside_box">""" + source + """</p>"""
    except Exception as inst:
        pass
    return output

