from website import grammer
from website import phrases

# Function for outputing senses
def sense(input_data):
    output = """<div class="senses">"""
    try:
        if input_data['SenseID']:
            output = output + """<p>""" + input_data['SenseID'] + ". nozīme" + """</p>"""
    except Exception as inst:
        pass
    
    output = output + """<div class="inside_box">"""    
    try:
        if input_data['Gram']:
            output = output + """<p>""" + grammer.grammer(input_data['Gram']) + """</p>"""
    except Exception as inst:
        pass
        
    try:
        if input_data['Gloss']:
            output = output + """<p>Skaidrojums: """ + input_data['Gloss'] + """</p>"""
    except Exception as inst:
        pass
        
    try:
        for p in input_data['Examples']['Phrase']:
            output = output + """<p>Piemēri: """ + phrases.phrase(p) + """</p>"""
    except Exception as inst:
        pass
            
    try:
        if input_data['Senses']:
            output = output + """<p>""" + sense(input_data['Senses']) + """</p>"""
    except Exception as inst:
        pass
    output = output + """</div>"""
    output = output + """</div>"""
    return output
