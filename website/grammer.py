# Function for outputing grammer
def grammer(input_data):
    output = """<div class="grammer"><p>Gramatika:</p><div class="inside_box">"""
    try:
        for f in input_data['Flags']:
            output = output + """<p id="list_of">""" + f + """</p>"""
    except Exception as inst:
        pass
    try:
        if input_data['Leftovers']:
            if input_data['Original']:
                output = output + """<p>Oriģināls: """ + input_data['Original'] + """</p>"""
    except Exception as inst:
        pass
    try:
        if input_data['Paradigm']:
            output = output + """<p id="top_of_list">Pradigmas:</p>"""
        for p in input_data['Paradigm']:
            output = output + """<p class="inside_box" id="list_of">""" + p + """</p>"""
    except Exception as inst:
        pass
            
    numbers = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20",
               "21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40"]
    for p in numbers:
        try:
            for k in input_data['AltLemmas'][p]:
                output = output + """<p id="lemma">""" + k['Lemma'] + """:</p>"""
                output = output + """<p class="inside_box">Gramatika:</p>"""
                for f in k['Flags']:
                    output = output + """<p class="double_inside_box">""" + f + """</p>"""
        except Exception as inst:
            pass
    output = output + """</div></div>"""
    return output
