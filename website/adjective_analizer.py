from website import table_gen_sk
from website import unknown_analizer

def adjective_analizer(input_data):
    output = ""
    pamata = []
    paraka = []
    visparaka = []
    leftower = []
    try:
        for line in input_data:
            try:
                if (line['Pakāpe'] == "Pamata") or (line['Pakāpe'] == "Pārākā") or (line['Pakāpe'] == "Vispārākā"):
                    if line['Pakāpe'] == "Pamata":
                        pamata.append(line)
                    elif line['Pakāpe'] == "Pārākā":
                        paraka.append(line)
                    elif line['Pakāpe'] == "Vispārākā":
                        visparaka.append(line)
                    else:
                        leftower.append(line)
                else:
                    leftower.append(line)
            except Exception as inst:
                pass
    except Exception as inst:
        pass
    try:
        if pamata != []:
            output = output + """<p class="inside_box"><b1>Pamata pakāpe</b1></</p>""" + dzimtes_analizer(pamata)
        if paraka != []:
            output = output + """<p class="inside_box"><b1>Pārākā pakāpe</b1></</p>""" + dzimtes_analizer(paraka)
        if visparaka != []:
            output = output + """<p class="inside_box"><b1>Vispārākā pakāpe</b1></</p>""" + dzimtes_analizer(visparaka)
        if leftower != []:
            output = output + unknown_analizer.unknown_analizer(leftower)
    except Exception as inst:
        pass
    return output

def dzimtes_analizer(input_data):
    output = ""
    vir = []
    siev = []
    nepiem = []
    try:
        for line in input_data:
            try:
                if line['Dzimte'] == "Vīriešu":
                    vir.append(line)
                elif line['Dzimte'] == "Sieviešu":
                    siev.append(line)
                else:
                    nepiem.append(line)
            except Exception as inst:
                pass
    except Exception as inst:
        pass
    try:
        if vir != []:
            output = output + """<div class="inside_box"><p class="inside_box"><b1>Vīriesu dzimte:</b1></</p>""" + noteiktibas_analizer(vir)
        if siev != []:
            output = output + """<div class="inside_box"><p class="inside_box"><b1>Sieviešu dzimte:</b1></</p>""" + noteiktibas_analizer(siev)
        if nepiem != []:
            output = output + unknown_analizer.unknown_analizer(nepiem)
    except Exception as inst:
        pass
    return output

def noteiktibas_analizer(input_data):
    output = ""
    noteikt = []
    nenoteikt = []
    nepiem = []
    try:
        for line in input_data:
            try:
                if line['Noteiktība'] == "Noteiktā":
                    noteikt.append(line)
                elif line['Noteiktība'] == "Nenoteiktā":
                    nenoteikt.append(line)
                else:
                    nepiem.append(line)
            except Exception as inst:
                pass
    except Exception as inst:
        pass
    try:
        if noteikt != []:
            output = output + """<p class="double_inside_box"><b1>Noteiktā galotne:</b1></</p>""" + table_gen_sk.table_gen_sk(noteikt) + """<br>"""
        if nenoteikt != []:
            output = output + """<p class="double_inside_box"><b1>Nenoteiktā galotne:</b1></</p>""" + table_gen_sk.table_gen_sk(nenoteikt) + """<br>"""
        if nepiem != []:
            output = output + unknown_analizer.unknown_analizer(nepiem)
    except Exception as inst:
        pass
    output = output + """</div>"""
    return output
