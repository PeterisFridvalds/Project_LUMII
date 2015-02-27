from website import grammer
##from website import phrases

# Function for outputing senses
def sense(input_data):
    output = """<div class="senses">"""
    try:
        if input_data['SenseID']:
            output = output + """<p>""" + input_data['SenseID'] + ". nozīme" + """</p>"""
            output = output + """<div class="inside_box">"""
    except Exception as inst:
        pass
        
    try:
        if input_data['Gram']:
            output = output + grammer.grammer(input_data['Gram'])
    except Exception as inst:
        pass
        
    try:
        if input_data['Gloss']:
            output = output + """<p>Skaidrojums: """ + input_data['Gloss'] + """</p>"""
    except Exception as inst:
        pass
        
    try:
        if input_data['Examples']:
            output = output + """<p>Piemēri:</p>"""
        for e in input_data['Examples']:
            output = output + phrase(e)
    except Exception as inst:
        pass
    
    output = output + """<div class="inside_box">"""
            
    try:
        if input_data['Senses']:
            output = output + sense(input_data['Senses'])
    except Exception as inst:
        pass
    
    output = output + """</div>"""
    try:
        if input_data['SenseID']:
            output = output + """</div>"""
    except Exception as inst:
        pass
    output = output + """</div>"""
    return output

# Function for outputing phrases
def phrase(input_data):
    output = """<div class="phrases">"""
    try:
        if input_data['Phrase']['Text']:
            output = output + """<p>""" + input_data['Phrase']['Text'] + """:</p>"""
    except Exception as inst:
        pass

    try:
        if input_data['Phrase']['Gram']:
            output = output + grammer.grammer(input_data['Phrase']['Gram'])
    except Exception as inst:
        pass
    
    try:
        
        for s in input_data['Phrase']['Senses']:
            output = output + sense(s)
    except Exception as inst:
        pass

    
    output = output + """</div>"""
    return output

