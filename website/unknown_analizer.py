def unknown_analizer(input_data):
    output = ""
    counting_keys = 0
    try:
        for line in input_data:
            try:
                for key in line:
                    if key != "Vārds":
                        if key != "Vārdšķira":
                            counting_keys = counting_key + 1
            except Exception as inst:
                pass
            if counting_keys == 0:
                output = output + """<p style="max-width: 500px"><b1>""" + line['Vārds'] + """</b1></p>"""
            else:
                output = output + """<p style="max-width: 500px"><b1>""" + line['Vārds'] + """: </b1></p>"""
            for key in line:
                if key != "Vārds":
                    if key != "Vārdšķira":
                        output = output + """<p class="inside_box">""" + key + ": " + line[key] + ";</p>"
    except Exception as inst:
        pass
    return output
