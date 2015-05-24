# -*- coding: utf-8 -*-
from inflect import unknown_analizer

##Funkcija, kas iedotos datus iedala pēc laika
def person_analizer(input_data, keys = []):
    output = ''
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
                
        #Pārbauda, vai ir kaut kādi dati, kas atiecas uz attiecīgo laiku, ja tādi ir, izsauc f-ju, kas tālāk apstrādā noteikto laiku
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

#Funkcija, kas iedotos datus iegala pēc kārtas
def kartas_analizer(input_data, keys = []):
    output = ''
    cies_karta = []
    dar_karta = []
    no_karta = []
    keys.append(u"Kārta")
    try:
        #Iedala pēc kārdas
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
        try:
            if cies_karta != []:
                output = output + u'<div class="inside_box"><p><b1>Ciešamā kārta:</b1></p>' + person_table_gen(cies_karta, keys) + u'</div>'
            if dar_karta != []:
                output = output + u'<div class="inside_box"><p><b1>Darāmā kārta:</b1></p>' + person_table_gen(dar_karta, keys) + u'</div>'
            if no_karta != []:
                output = output + u'<div class="inside_box"><p><b1>Kārta nepiemīt:</b1></p>' + person_table_gen(no_karta, keys) + u'</div>'
        except Exception as inst:
            pass
    except Exception as inst:
        pass
    return output

#Funkcija, kas iedala datus pēc personas
def person_table_gen(input_data, keys):
    output = ""
    vsk = False
    dsk = False
    no_sk = False
    pirm_pers = []
    otr_pers = []
    tres_pers = []
    no_pers = []
    keys.append(u"Persona")
    try:
        for line in input_data:
            #Pārbauda, vai ir vārdi noteiktajos skaitļos
            try:
                if line[u'Skaitlis'] == u"Vienskaitlis":
                    vsk = True
                if line[u'Skaitlis'] == u"Daudzskaitlis":
                    dsk = True
                if line[u'Skaitlis'] == u"Nepiemīt":
                    no_sk = True
            except Exception as inst:
                no_sk = True
                
            #Iedala datus pēc personas
            try:
                if line[u'Persona'] == u"1":
                    pirm_pers.append(line)
                elif line[u'Persona'] == u"2":
                    otr_pers.append(line)
                elif line[u'Persona'] == u"3":
                    tres_pers.append(line)
                else:
                    no_pers.append(line)
            except Exception as inst:
                no_pers.append(line)
                
        output = output + u'<div class="inflect">'
        #Ja ir dati 1., 2. vai 3. personai, tad veido tabulu ar tik rinidņām, cik personām dati ir domāti
        if (pirm_pers != []) or (otr_pers != []) or (tres_pers != []):
            output = output + u'<table id="auto_table">'
            output = output + u'<tr><td><b1>Persona</b1></td>'
            if vsk == True:
                output = output + u'<td><b1>Viensk.</b1></td>'
            if dsk == True:
                output = output + u'<td><b1>Daudzsk.</b1></td>'
            if no_sk == True:
                output = output + u'<td><b1>Sk.nepiemīt</b1></td>'
            output = output + u'</tr>'
            
            if pirm_pers != []:
                output = output + line_gen(pirm_pers, u"1", vsk, dsk, no_sk)
            if otr_pers != []:
                output = output + line_gen(otr_pers, u"2", vsk, dsk, no_sk)
            if tres_pers != []:
                output = output + line_gen(tres_pers, u"3", vsk, dsk, no_sk)
            output = output + u'</table>'
        #Ja persona nepiemīt, izvada vārdu, kā arī līdz šim neizvadītos uz vārdu attiecošos atslēgas vārdus un to vērtības
        try:
            if no_pers != []:
                output = output + unknown_analizer.unknown_analizer(no_pers, keys)
        except Exception as inst:
            pass
        output = output + u'</div>'
    except Exception as inst:
        pass
    return output

#Funkcija, kas ģenerē tabulas rindiņu
def line_gen(input_data, pers, vsk, dsk, no_sk):
    output = ""
    output = output + u'<tr><td><b1> ' + pers + u'. </b1></td>'
    if vsk == True:
        output = output + u'<td id="loc_tab">'
        for line in input_data:
            try:
                if line[u'Skaitlis'] == u"Vienskaitlis":
                    output = output + line[u'Vārds'] + u"; "
            except Exception as inst:
                pass
        output = output + u'</td>'
    if dsk == True:
        output = output + u'<td id="loc_tab">'
        for line in input_data:
            try:
                if line[u'Skaitlis'] == u"Daudzskaitlis":
                    output = output + line[u'Vārds'] + u"; "
            except Exception as inst:
                pass
        output = output + u'</td>'
    if no_sk == True:
        output = output + u'<td id="loc_tab">'
        for line in input_data:
            try:
                if line[u'Skaitlis'] == u"Nepiemīt":
                    output = output + line[u'Vārds'] + u"; "
            except Exception as inst:
                pass
        output = output + u'</td>'
    output = output + u'</tr>'
    output = output.replace(u'; </td>', u'</td>')
    output = output.replace(u'<td id="loc_tab"></td>', u'<td id="loc_tab"> - </td>')

    return output
    
            
            
            
        
