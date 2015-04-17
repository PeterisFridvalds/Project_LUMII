def table_gen_no_sk(input_data):
    output = ""
    try:
        output = output + """<div class="inflect"><table id="auto_table"><tr><td><b1>Locījums</b1></td><td><b1>Vārds</b1></td></tr><tr><td><b1>Nominatīvs</b1></td><td id="loc_tab">"""
        for line in input_data:
            try:
                if line['Locījums'] == "Nominatīvs":
                    output = output + line['Vārds'] + " "
            except Exception as inst:
                pass
        output = output + """</td></tr><tr><td><b1>Ģenitīvs</b1></td><td id="loc_tab">"""
        for line in input_data:
            try:
                if line['Locījums'] == "Ģenitīvs":
                    output = output + line['Vārds'] + " "
            except Exception as inst:
                pass
        output = output + """</td></tr><tr><td><b1>Datīvs</b1></td><td id="loc_tab">"""
        for line in input_data:
            try:
                if line['Locījums'] == "Datīvs":
                    output = output + line['Vārds'] + " "
            except Exception as inst:
                pass
        output = output + """</td></tr><tr><td><b1>Akuzatīvs</b1></td><td id="loc_tab">"""
        for line in input_data:
            try:
                if line['Locījums'] == "Akuzatīvs":
                    output = output + line['Vārds'] + " "
            except Exception as inst:
                pass
        output = output + """</td></tr><tr><td><b1>Lokatīvs</b1></td><td id="loc_tab">"""
        for line in input_data:
            try:
                if line['Locījums'] == "Lokatīvs":
                    output = output + line['Vārds'] + " "
            except Exception as inst:
                pass
        output = output + """</td></tr><tr><td><b1>Vokatīvs</b1></td><td id="loc_tab">"""
        for line in input_data:
            try:
                if line['Locījums'] == "Vokatīvs":
                    output = output + line['Vārds'] + " "
            except Exception as inst:
                pass
        output = output + """</td></tr></table><br></div>"""
    except Exception as inst:
        pass
    return output
