from website import table_gen
from website import unknown_analizer

#Funkcija, kas iedala īpašības vārdus pēc pakāpes
def adjective_analizer(input_data, keys = ["Vārdšķira"]):
    output = ""
    pamata = []
    paraka = []
    visparaka = []
    leftower = []
    keys.append("Pakāpe")

    #Iedala iedotos datus pēc pakāpes
    for line in input_data:
        try:
            if line['Pakāpe'] == "Pamata":
                pamata.append(line)
            elif line['Pakāpe'] == "Pārākā":
                paraka.append(line)
            elif line['Pakāpe'] == "Vispārākā":
                visparaka.append(line)
            else:
                leftower.append(line)
        except Exception as inst:
            leftower.append(line)

    #Izsauc funkciju, kas apstrādās attiecīgo pakāpi
    try:
        if pamata != []:
            output = output + """<div class="inside_box"><p><b1>Pamata pakāpe</b1></p>""" + dzimtes_analizer(pamata, keys) + """</div>"""
        if paraka != []:
            output = output + """<div class="inside_box"><p><b1>Pārākā pakāpe</b1></p>""" + dzimtes_analizer(paraka, keys) + """</div>"""
        if visparaka != []:
            output = output + """<div class="inside_box"><p><b1>Vispārākā pakāpe</b1></p>""" + dzimtes_analizer(visparaka, keys) + """</div>"""
        if leftower != []:
            output = output + """<div class="inside_box"><p><b1>Pakāpe nepiemīt</b1></p>""" + dzimtes_analizer(leftower, keys) + """</div>"""
    except Exception as inst:
        pass
    return output

#Funkcija, kas iedala idotos datus pēc dzimtes
def dzimtes_analizer(input_data, keys):
    output = ""
    vir = []
    siev = []
    nepiem = []
    keys.append('Dzimte')

    #Iedala iedotos datus pēc dzimtes
    for line in input_data:
        try:
            if line['Dzimte'] == "Vīriešu":
                vir.append(line)
            elif line['Dzimte'] == "Sieviešu":
                siev.append(line)
            else:
                nepiem.append(line)
        except Exception as inst:
            nepiem.append(line)

    #Izsauc funkciju, kas apstrādā noteikto dzimti
    try:
        if vir != []:
            output = output + """<div class="inside_box"><p><b1>Vīriesu dzimte:</b1></p>""" + noteiktibas_analizer(vir, keys) + """</div>"""
        if siev != []:
            output = output + """<div class="inside_box"><p><b1>Sieviešu dzimte:</b1></p>""" + noteiktibas_analizer(siev, keys) + """</div>"""
        if nepiem != []:
            output = output + """<div class="inside_box"><p><b1>Dzimte nepiemīt:</b1></p>""" + noteiktibas_analizer(nepiem, keys) + """</div>"""
    except Exception as inst:
        pass
    return output

#Funkcija, kas iedala iedotos datus pēc noteiktības
def noteiktibas_analizer(input_data, keys):
    output = ""
    noteikt = []
    nenoteikt = []
    nepiem = []
    keys.append('Noteiktība')
    
    #Iedala iedotos datus pēc noteiktības
    for line in input_data:
        try:
            if line['Noteiktība'] == "Noteiktā":
                noteikt.append(line)
            elif line['Noteiktība'] == "Nenoteiktā":
                nenoteikt.append(line)
            else:
                nepiem.append(line)
        except Exception as inst:
            nepiem.append(line)

    #Izsauc funkciju, kas apstrādā noteikto noteiktību
    try:
        if noteikt != []:
            output = output + """<p class="inside_box"><b1>Noteiktā galotne:</b1></p>""" + table_gen.table_gen(noteikt) + """<br>"""
        if nenoteikt != []:
            output = output + """<p class="inside_box"><b1>Nenoteiktā galotne:</b1></p>""" + table_gen.table_gen(nenoteikt) + """<br>"""
        if nepiem != []:
            output = output + """<p class="inside_box"><b1>Nav ne noteiktā, ne nenoteiktā galotne:</b1></p>""" + table_gen.table_gen(nepiem) + """<br>"""
    except Exception as inst:
        pass
    return output
