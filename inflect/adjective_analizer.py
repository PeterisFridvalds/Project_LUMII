# -*- coding: utf-8 -*-
from inflect import table_gen
from inflect import unknown_analizer

##Funkcija, kas iedala īpašības vārdus pēc pakāpes
def adjective_analizer(input_data, keys = [u"Vārdšķira"]):
    output = ''
    pamata = []
    paraka = []
    visparaka = []
    leftower = []
    keys.append("Pakāpe")

    #Iedala iedotos datus pēc pakāpes
    for line in input_data:
        try:
            if line[u'Pakāpe'] == u"Pamata":
                pamata.append(line)
            elif line[u'Pakāpe'] == u"Pārākā":
                paraka.append(line)
            elif line[u'Pakāpe'] == u"Vispārākā":
                visparaka.append(line)
            else:
                leftower.append(line)
        except Exception as inst:
            leftower.append(line)

    #Izsauc funkciju, kas apstrādās attiecīgo pakāpi
    output = output + u'<ul class="table_layout">'
    try:
        if pamata != []:
            output = output + u'<li><div class="inside_box"><p><b1>Pamata pakāpe</b1></p>' + dzimtes_analizer(pamata, keys) + u'</div></li>'
        if paraka != []:
            output = output + u'<li><div class="inside_box"><p><b1>Pārākā pakāpe</b1></p>' + dzimtes_analizer(paraka, keys) + u'</div></li>'
        if visparaka != []:
            output = output + u'<li><div class="inside_box"><p><b1>Vispārākā pakāpe</b1></p>' + dzimtes_analizer(visparaka, keys) + u'</div></li>'
        if leftower != []:
            output = output + u'<li><div class="inside_box"><p><b1>Pakāpe nepiemīt</b1></p>' + dzimtes_analizer(leftower, keys) + u'</div></li>'
    except Exception as inst:
        pass
    output = output + u'</ul>'
    return output

#Funkcija, kas iedala idotos datus pēc dzimtes
def dzimtes_analizer(input_data, keys):
    output = ""
    vir = []
    siev = []
    nepiem = []
    keys.append(u'Dzimte')

    #Iedala iedotos datus pēc dzimtes
    for line in input_data:
        try:
            if line[u'Dzimte'] == u"Vīriešu":
                vir.append(line)
            elif line[u'Dzimte'] == u"Sieviešu":
                siev.append(line)
            else:
                nepiem.append(line)
        except Exception as inst:
            nepiem.append(line)

    #Izsauc funkciju, kas apstrādā noteikto dzimti
    try:
        if vir != []:
            output = output + u'<div class="inside_box"><p><b1>Vīriesu dzimte:</b1></p>' + noteiktibas_analizer(vir, keys) + u'</div>'
        if siev != []:
            output = output + u'<div class="inside_box"><p><b1>Sieviešu dzimte:</b1></p>' + noteiktibas_analizer(siev, keys) + u'</div>'
        if nepiem != []:
            output = output + u'<div class="inside_box"><p><b1>Dzimte nepiemīt:</b1></p>' + noteiktibas_analizer(nepiem, keys) + u'</div>'
    except Exception as inst:
        pass
    return output

#Funkcija, kas iedala iedotos datus pēc noteiktības
def noteiktibas_analizer(input_data, keys):
    output = ""
    noteikt = []
    nenoteikt = []
    nepiem = []
    keys.append(u'Noteiktība')
    
    #Iedala iedotos datus pēc noteiktības
    for line in input_data:
        try:
            if line[u'Noteiktība'] == u"Noteiktā":
                noteikt.append(line)
            elif line[u'Noteiktība'] == u"Nenoteiktā":
                nenoteikt.append(line)
            else:
                nepiem.append(line)
        except Exception as inst:
            nepiem.append(line)

    #Izsauc funkciju, kas apstrādā noteikto noteiktību
    try:
        if noteikt != []:
            output = output + u'<p class="inside_box"><b1>Noteiktā galotne:</b1></p>' + table_gen.table_gen(noteikt, keys) + u'<br>'
        if nenoteikt != []:
            output = output + u'<p class="inside_box"><b1>Nenoteiktā galotne:</b1></p>' + table_gen.table_gen(nenoteikt, keys) + u'<br>'
        if nepiem != []:
            output = output + u'<p class="inside_box"><b1>Nav ne noteiktā, ne nenoteiktā galotne:</b1></p>' + table_gen.table_gen(nepiem, keys) + u'<br>'
    except Exception as inst:
        pass
    return output
