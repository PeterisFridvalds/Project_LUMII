from website import grammer
##from website import senses

# Function for outputing phrases
def phrase(input_data):
    output = """<div class="phrases">"""
    try:
        if input_data['Text']:
            output = output + """<p>""" + input_data['Text'] + """</p>"""
    except Exception as inst:
        pass

    try:
        if input_data['Gram']:
            output = output + """<p>""" + grammer.grammer(input_data['Gram']) + """</p>"""
    except Exception as inst:
        pass

    try:
        if input_data['Senses']:
            output = output + """<p>""" + senses.sense(input_data['Senses']) + """</p>"""
    except Exception as inst:
        pass
    output = output + """</div>"""
    return output
