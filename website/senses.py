from website import grammer
##from website import phrases

# Function for outputing senses
def sense(input_data):
    output = ""
    try:
        if input_data['SenseID']:
            output = output + """<p id="top_of_list"><b1>""" + input_data['SenseID'] + ". nozīme — " + """</b1>"""
    except Exception as inst:
        pass
    try:
        if input_data['Gloss']:
            output = output + input_data['Gloss'] + """</p>"""
    except Exception as inst:
        pass
    try:
        if input_data['Gram']:
            output = output + grammer.grammer(input_data['Gram'])
    except Exception as inst:
        pass 
    try:
        if input_data['SenseID']:
            output = output + """<div class="inside_box">"""
    except Exception as inst:
        pass 
    try:
        if input_data['Examples']:
            output = output + """<p><b1>Piemēri:</b1></p>"""
            for e in input_data['Examples']:
                output = output + phrase(e)
    except Exception as inst:
        pass
    try:
        if input_data['Senses']:
            output = output + """<p id="top_of_list"><b1>Apakšnozīmes:</b1></p><div class="inside_box">"""
            for s in input_data['Senses']:
                output = output + sense(s)
            output = output + """</div>"""
    except Exception as inst:
        pass
    try:
        if input_data['SenseID']:
            output = output + """</div>"""
    except Exception as inst:
        pass
    return output

# Function for outputing phrases
def phrase(input_data):
    output = """<div class="phrases">"""
    try:
        if input_data['Phrase']['Text']:
            output = output + """<p><b>""" + input_data['Phrase']['Text'] + """ — </b>"""
    except Exception as inst:
        pass
    try:
        for s in input_data['Phrase']['Senses']:
            output = output + sense(s)
    except Exception as inst:
        pass
    try:
        if input_data['Phrase']['Gram']:
            output = output + grammer.grammer(input_data['Phrase']['Gram'])
    except Exception as inst:
        pass
    output = output + """</div>"""
    return output

