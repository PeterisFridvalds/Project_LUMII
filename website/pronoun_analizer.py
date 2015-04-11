def from website import (input_data):
    output = ""
    try:
        for line in input_data:
            output = output + """<p><b1>Vietniekvārds: </b1>""" + line['Vārds'] + """:</p>"""
            try:
                if line['Locījums']:
                    output = output + """<p class="inside_box">Locījums: """ + line['Vārds'] + """</p>"""
            except Exception as inst:
                pass
            try:
                if line['Skaitlis']:
                    output = output + """<p class="inside_box">Skaitlis: """ + line['Skaitlis'] + """</p>"""
            except Exception as inst:
                pass
            try:
                if line['Dzimte']:
                    output = output + """<p class="inside_box">Dzimte: """ + line['Dzimte'] + """</p>"""
            except Exception as inst:
                pass
            try:
                if line['Persona']:
                    output = output + """<p class="inside_box">Persona: """ + line['Persona'] + """</p>"""
            except Exception as inst:
                pass
    except Exception as inst:
        pass
    return output
