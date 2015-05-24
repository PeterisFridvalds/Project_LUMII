# -*- coding: utf-8 -*-
from inflect import table_gen

#Funkcija, kas iedala divdabjus pēc laika
def divdab_analizer(input_data, keys = []):
    output = ""
    past = []
    present = []
    future = []
    no_time = []
    keys.append(u"Laiks")
    try:
        #Ieadala iedotos datus pēc laikiem
        for line in input_data:
            try:
                if line[u'Laiks'] == u"Pagātne":
                    past.append(line)
                elif line[u'Laiks'] == u"Tagadne":
                    present.append(line)
                elif line[u'Laiks'] == u"Nākotne":
                    future.append(line)
                else:
                    no_time.append(line)
            except Exception as inst:
                no_time.append(line)
                
        #Izsauc funkciju, kas apstrādā attiecīgo laiku
        try:
            if past != []:
                output = output + u'<li><div class="inside_box"><p><b1>Pagātne:</b1></p>' + kartas_analizer(past, keys) + u'</div></li>'
            if present != []:
                output = output + u'<li><div class="inside_box"><p><b1>Tagadne:</b1></p>' + kartas_analizer(present, keys) + u'</div></li>'
            if future != []:
                output = output + u'<li><div class="inside_box"><p><b1>Nākotne:</b1></p>' + kartas_analizer(future, keys) + u'</div></li>'
            if no_time != []:
                output = output + u'<li><div class="inside_box"><p><b1>Laiks nepiemīt:</b1></p>' + kartas_analizer(no_time, keys) + u'</div></li>'
        except Exception as inst:
            pass
    except Exception as inst:
        pass
    return output

#Funkcija, kas iedala iedotos datus pēc kārtas
def kartas_analizer(input_data, keys = []):
    output = ""
    cies_karta = []
    dar_karta = []
    no_karta = []
    keys.append(u"Kārta")
    try:
        #Iedala iedotos datus pēc kārtas
        for line in input_data:
            try:
                if line[u'Kārta'] == u"Ciešamā":
                    cies_karta.append(line)
                elif line[u'Kārta'] == u"Darāmā":
                    dar_karta.append(line)
                else:
                    no_karta.append(line)
            except Exception as inst:
                no_karta.append(line)
        #Izsauc funkciju, kas apstādā attiecīgo laiku
        try:
            if cies_karta != []:
                output = output + u'<div class="inside_box"><p><b1>Ciešamā kārta:</b1></p>' + sk_dzimt_analizer(cies_karta, keys) + u'</div>'
            if dar_karta != []:
                output = output + u'<div class="inside_box"><p><b1>Darāmā kārta:</b1></p>' + sk_dzimt_analizer(dar_karta, keys) + u'</div>'
            if no_karta != []:
                output = output + u'<div class="inside_box"><p><b1>Kārta nepiemīt:</b1></p>' + sk_dzimt_analizer(no_karta, keys) + u'</div>'
        except Exception as inst:
            pass
    except Exception as inst:
        pass
    return output

#Funkcija, kas iedala iedotos datus pēc dzimtes
def sk_dzimt_analizer(input_data, keys = []):
    output = ""
    siev = []
    vir = []
    bezdz = []
    keys.append(u"Dzimte")
    try:
        #Iedala iedotos datus pēc dzimtes
        for line in input_data:
            try:
                if line[u'Dzimte'] == u"Vīriešu":
                    vir.append(line)
                elif line[u'Dzimte'] == u"Sieviešu":
                    siev.append(line)
                else:
                    bezdz.append(line)
            except Exception as inst:
                bezdz.append(line)

        #Izsauc funkciju, kas apstrādās attiecīgo dzimti
        try:
            if vir != []:
                output = output + u'<p class="inside_box"><b1>Vīriesu dzimte:</b1></p>' + table_gen.table_gen(vir, keys)
            if siev != []:
                output = output + u'<p class="inside_box"><b1>Sieviešu dzimte:</b1></p>' + table_gen.table_gen(siev, keys)
            if bezdz != []:
                output = output + u'<p class="inside_box"><b1>Dzimte nepiemīt:</b1></p>' + table_gen.table_gen(bezdz, keys)
        except Exception as inst:
            pass
    except Exception as inst:
        pass
    return output
