from website import table_gen_sk

def adjective_analizer(input_data):
    output = ""
    pamata_v = []
    paraka_v = []
    visparaka_v = []
    pamata_s = []
    paraka_s = []
    visparaka_s = []
    leftower = []
    try:
        for line in input_data:
            try:
                if (line['Pakāpe'] == "Pamata") or (line['Pakāpe'] == "Pārākā") or (line['Pakāpe'] == "Vispārākā"):
                    if line['Pakāpe'] == "Pamata":
                        if line['Dzimte'] == "Vīriešu":
                            pamata_v.append(line)
                        if line['Dzimte'] == "Sieviešu":
                            pamata_s.append(line)
                    elif line['Pakāpe'] == "Pārākā":
                        if line['Dzimte'] == "Vīriešu":
                            paraka_v.append(line)
                        if line['Dzimte'] == "Sieviešu":
                            paraka_s.append(line)
                    elif line['Pakāpe'] == "Vispārākā":
                        if line['Dzimte'] == "Vīriešu":
                            visparaka_v.append(line)
                        if line['Dzimte'] == "Sieviešu":
                            visparaka_s.append(line)
                    else:
                        leftower.append(line)
                else:
                    leftower.append(line)
            except Exception as inst:
                pass
    except Exception as inst:
        pass
    try:
        if pamata_v != []:
            output = output + """<p class="inside_box"><b1>Vīriešu dzimte, pamata pakāpe</b1></</p>""" + table_gen_sk.table_gen_sk(pamata_v) + """<br>"""
        if paraka_v != []:
            output = output + """<p class="inside_box"><b1>Vīriešu dzimte, pārākā pakāpe</b1></</p>""" + table_gen_sk.table_gen_sk(paraka_v) + """<br>"""
        if visparaka_v != []:
            output = output + """<p class="inside_box"><b1>Vīriešu dzimte, vispārākā pakāpe</b1></</p>""" + table_gen_sk.table_gen_sk(visparaka_v) + """<br>"""
        if pamata_s != []:
            output = output + """<p class="inside_box"><b1>Sieviesu dzimte, pamata pakāpe</b1></</p>""" + table_gen_sk.table_gen_sk(pamata_s) + """<br>"""
        if paraka_s != []:
            output = output + """<p class="inside_box"><b1>Sieviesu dzimte, pārākā pakāpe</b1></</p>""" + table_gen_sk.table_gen_sk(paraka_s) + """<br>"""
        if visparaka_s != []:
            output = output + """<p class="inside_box"><b1>Sieviesu dzimte, vispārākā pakāpe</b1></p>""" + table_gen_sk.table_gen_sk(visparaka_s) + """<br>"""
        for line in leftower:
            output = output + """<p style="max-width: 500px"><b1>""" + line['Vārds'] + """: </b1>"""
            for key in line:
                if key != "Vārds":
                    output = output + key + " - " + line[key] + "; "
            output = output + """</p>"""
    except Exception as inst:
        pass
    return output
