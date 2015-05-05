from website import unknown_analizer

#Funkcija, kas iedotos datus iedala pēc laika
def person_analizer(input_data, keys = []):
    output = ""
    past = []
    present = []
    future = []
    no_time = []
    keys.append("Laiks")
    try:
        #Ieadala iedotos datus pēc laikiem
        for line in input_data:
            try:
                if line['Laiks'] == "Pagātne":
                    past.append(line)
                elif line['Laiks'] == "Tagadne":
                    present.append(line)
                elif line['Laiks'] == "Nākotne":
                    future.append(line)
                else:
                    no_time.append(line)
            except Exception as inst:
                no_time.append(line)
                
        #Pārbauda, vai ir kaut kādi dati, kas atiecas uz attiecīgo laiku, ja tādi ir, izsauc f-ju, kas tālāk apstrādā noteikto laiku
        try:
            if past != []:
                output = output + """<li><div class="inside_box"><p><b1>Pagātne:</b1></p>""" + kartas_analizer(past, keys) + "</div></li>"
            if present != []:
                output = output + """<li><div class="inside_box"><p><b1>Tagadne:</b1></p>""" + kartas_analizer(present, keys) + "</div></li>"
            if future != []:
                output = output + """<li><div class="inside_box"><p><b1>Nākotne:</b1></p>""" + kartas_analizer(future, keys) + "</div></li>"
            if no_time != []:
                output = output + """<li><div class="inside_box"><p><b1>Laiks nepiemīt:</b1></p>""" + kartas_analizer(no_time, keys) + "</div></li>"
        except Exception as inst:
            pass
    except Exception as inst:
        pass
    return output

#Funkcija, kas iedotos datus iegala pēc kārtas
def kartas_analizer(input_data, keys = []):
    output = ""
    cies_karta = []
    dar_karta = []
    no_karta = []
    keys.append("Kārta")
    try:
        #Iedala pēc kārdas
        for line in input_data:
            try:
                if line['Kārta'] == "Ciešamā":
                    cies_karta.append(line)
                elif line['Kārta'] == "Darāmā":
                    dar_karta.append(line)
                else:
                    no_karta.append(line)
            except Exception as inst:
                no_karta.append(line)
        try:
            if cies_karta != []:
                output = output + """<div class="inside_box"><p><b1>Ciešamā kārta:</b1></p>""" + person_table_gen(cies_karta, keys) + "</div>"
            if dar_karta != []:
                output = output + """<div class="inside_box"><p><b1>Darāmā kārta:</b1></p>""" + person_table_gen(dar_karta, keys) + "</div>"
            if no_karta != []:
                output = output + """<div class="inside_box"><p><b1>Kārta nepiemīt:</b1></p>""" + person_table_gen(no_karta, keys) + "</div>"
        except Exception as inst:
            pass
    except Exception as inst:
        pass
    return output

#Funkcija, kas iedala datus pēc personas
def person_table_gen(input_data, keys):
    output = ""
    vsk = "0"
    dsk = "0"
    no_sk = "0"
    pirm_pers = []
    otr_pers = []
    tres_pers = []
    no_pers = []
    keys.append("Persona")
    try:
        for line in input_data:
            #Pārbauda, vai ir vārdi noteiktajos skaitļos
            try:
                if line['Skaitlis'] == "Vienskaitlis":
                    vsk = "1"
                if line['Skaitlis'] == "Daudzskaitlis":
                    dsk = "1"
                if line['Skaitlis'] == "Nepiemīt":
                    no_sk = "1"
            except Exception as inst:
                no_sk = "1"
                
            #Iedala datus pēc personas
            try:
                if line['Persona'] == "1":
                    pirm_pers.append(line)
                elif line['Persona'] == "2":
                    otr_pers.append(line)
                elif line['Persona'] == "3":
                    tres_pers.append(line)
                else:
                    no_pers.append(line)
            except Exception as inst:
                no_pers.append(line)
                
        output = output + """<div class="inflect">"""
        #Ja ir dati 1., 2. vai 3. personai, tad veido tabulu ar tik rinidņām, cik personām dati ir domāti
        if (pirm_pers != []) or (otr_pers != []) or (tres_pers != []):
            output = output + """<table id="auto_table">"""
            output = output + """<tr><td><b1>Persona</b1></td>"""
            if vsk == "1":
                output = output + """<td><b1>Viensk.</b1></td>"""
            if dsk == "1":
                output = output + """<td><b1>Daudzsk.</b1></td>"""
            if no_sk == "1":
                output = output + """<td><b1>Sk.nepiemīt</b1></td>"""
            output = output + """</tr>"""
            
            if pirm_pers != []:
                output = output + line_gen(pirm_pers, "1", vsk, dsk, no_sk)
            if otr_pers != []:
                output = output + line_gen(otr_pers, "2", vsk, dsk, no_sk)
            if tres_pers != []:
                output = output + line_gen(tres_pers, "3", vsk, dsk, no_sk)
            output = output + """</table>"""
        #Ja persona nepiemīt, izvada vārdu, kā arī līdz šim neizvadītos uz vārdu attiecošos atslēgas vārdus un to vērtības
        try:
            if no_pers != []:
                output = output + unknown_analizer.unknown_analizer(no_pers, keys)
        except Exception as inst:
            pass
        output = output + """</div>"""
    except Exception as inst:
        pass
    return output

#Funkcija, kas ģenerē tabulas rindiņu
def line_gen(input_data, pers, vsk, dsk, no_sk):
    output = ""
    output = output + """<tr><td><b1> """ + pers + """. </b1></td>"""
    if vsk == "1":
        output = output + """<td id="loc_tab">"""
        for line in input_data:
            try:
                if line['Skaitlis'] == "Vienskaitlis":
                    output = output + line['Vārds'] + "; "
            except Exception as inst:
                pass
        output = output + """</td>"""
    if dsk == "1":
        output = output + """<td id="loc_tab">"""
        for line in input_data:
            try:
                if line['Skaitlis'] == "Daudzskaitlis":
                    output = output + line['Vārds'] + "; "
            except Exception as inst:
                pass
        output = output + """</td>"""
    if no_sk == "1":
        output = output + """<td id="loc_tab">"""
        for line in input_data:
            try:
                if line['Skaitlis'] == "Nepiemīt":
                    output = output + line['Vārds'] + "; "
            except Exception as inst:
                pass
        output = output + """</td>"""
    output = output + """</tr>"""
    output = output.replace("""; </td>""", """</td>""")
    output = output.replace("""<td id="loc_tab"></td>""", """<td id="loc_tab"> - </td>""")

    return output
    
            
            
            
        
