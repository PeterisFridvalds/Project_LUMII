##from website import senses
from website import grammer

# Function for outputing phrases
def phrase(input_data):
    output = """<div class="phrases">"""
    try:
        if input_data['Phrase']['Text']:
            output = output + """<p>""" + input_data['Phrase']['Text'] + """:</p>"""
    except Exception as inst:
        pass
    
    try:
        
        for s in input_data['Phrase']['Senses']:
            output = output + """<p class="inside_box"> te jābūt skaidrojumam </p>"""
            output = output + """<p class="inside_box"> te jābūt skaidrojumam""" + senses.sense(s) + """</p>"""
    except Exception as inst:
        pass

    try:
        if input_data['Phrase']['Gram']:
            output = output + """<p>Gramatika: """ + grammer.grammer(input_data['Phrase']['Gram']) + """</p>"""
    except Exception as inst:
        pass

    
    output = output + """</div>"""
    return output
