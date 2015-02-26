# Function for outputing grammer
def grammer(input_data):
    output = """<div class="grammer">"""
    try:
        output = output + """<p>Pradigma:</p>"""
        for p in input_data['Paradigm']:
            output = output + """<p class="inside_box">Pradigma: """ + p + """</p>"""
    except Exception as inst:
        pass
        
    try:
        output = output + """<p>Karodziņi:</p>"""
        for f in input_data['Flags']:
            output = output + """<p class="inside_box">""" + f + """</p>"""
    except Exception as inst:
        try:
            if input_data['Original']:
                output = output + """<p>Oriģināls: """ + input_data['Original'] + """</p>"""
        except Exception as inst:
            pass
        
    try:
        output = output + """<p>Pārpalikums:</p>"""
        for l in input_data['Leftowers']:
            output = output + """<p class="inside_box">""" + l + """</p>"""
    except Exception as inst:
        pass
    output = output + """</div>"""
    return output
