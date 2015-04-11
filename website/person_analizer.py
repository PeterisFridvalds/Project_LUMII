def person_analizer(input_data):
    output = ""
    past = []
    present = []
    future = []
    no_time = []
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
                pass
        #pārbauda, vai ir kaut kādi dati, kas atiecas uz attiecīgo laiku, ja tādi ir, izsauc f-ju, kas izveido HTML kodu locījumiem
        try:
            if past != []:
                output = output + """<p class="inside_box"><b1>Pagātne:</b1>""" + person_table_gen(past)
        except Exception as inst:
            pass
        try:
            if present != []:
                output = output + """<p class="inside_box"><b1>Tagadne:</b1>""" + person_table_gen(present)
        except Exception as inst:
            pass
        try:
            if future != []:
                output = output + """<p class="inside_box"><b1>Nākotne:</b1>""" + person_table_gen(future)
        except Exception as inst:
            pass
        try:
            if no_time != []:
                output = output + """<p class="inside_box"><b1>Laiks nepiemīt:</b1>""" + person_table_gen(no_time)
        except Exception as inst:
            pass
    except Exception as inst:
        pass
    return output

def person_table_gen(input_data):
    output = ""
    pirm_pers = "0"
    otr_pers = "0"
    tres_pers = "0"
    try:
        for line in input_data:
            #Pārbauda vai ir dati, kas attiecas uz noteiktu personu
            try:
                if line['Persona'] == "1":
                    pirm_pers = "1"
                if line['Persona'] == "2":
                    otr_pers = "1"
                if line['Persona'] == "3":
                    tres_pers = "1"
            except Exception as inst:
                pass
        output = output + """<div class="inflect">"""
        #Ja ir dati 1., 2. vai 3. personai, tad veido tabulu ar tik rinidņām, cik personām dati ir domāti
        if (pirm_pers != "0") or (otr_pers != "0") or (tres_pers != "0"):
            output = output + """<table id="auto_table"><tr><td><b1>Persona</b1></td><td><b1>Viensk.</b1></td><td><b1>Daudzsk.</b1></td><td><b1>Sk.nepiemīt</b1></td></tr>"""
            if pirm_pers != "0":
                output = output + """<tr><td><b1> 1. </b1></td><td id="loc_tab">"""
                for line in input_data:
                    try:
                        if line['Persona'] == "1":
                            if line['Skaitlis'] == "Vienskaitlis":
                                output = output + line['Vārds'] + "; "
                    except Exception as inst:
                        pass
                output = output + """</td><td id="loc_tab">"""
                for line in input_data:
                    try:
                        if line['Persona'] == "1":
                            if line['Skaitlis'] == "Daudzskaitlis":
                                output = output + line['Vārds'] + "; "
                    except Exception as inst:
                        pass
                output = output + """</td><td id="loc_tab">"""
                for line in input_data:
                    try:
                        if line['Persona'] == "1":
                            if line['Skaitlis'] == "Nepiemīt":
                                output = output + line['Vārds'] + "; "
                    except Exception as inst:
                        pass
            if otr_pers != "0":
                output = output + """</td></tr><tr><td><b1> 2. </b1></td><td id="loc_tab">"""
                for line in input_data:
                    try:
                        if line['Persona'] == "2":
                            if line['Skaitlis'] == "Vienskaitlis":
                                output = output + line['Vārds'] + "; "
                    except Exception as inst:
                        pass
                output = output + """</td><td id="loc_tab">"""
                for line in input_data:
                    try:
                        if line['Persona'] == "2":
                            if line['Skaitlis'] == "Daudzskaitlis":
                                output = output + line['Vārds'] + "; "
                    except Exception as inst:
                        pass
                output = output + """</td><td id="loc_tab">"""
                for line in input_data:
                    try:
                        if line['Persona'] == "2":
                            if line['Skaitlis'] == "Nepiemīt":
                                output = output + line['Vārds'] + "; "
                    except Exception as inst:
                        pass
            if tres_pers != "0":
                output = output + """</td></tr><tr><td><b1> 3. </b1></td><td id="loc_tab">"""
                for line in input_data:
                    try:
                        if line['Persona'] == "3":
                            if line['Skaitlis'] == "Vienskaitlis":
                                output = output + line['Vārds'] + "; "
                    except Exception as inst:
                        pass
                output = output + """</td><td id="loc_tab">"""
                for line in input_data:
                    try:
                        if line['Persona'] == "3":
                            if line['Skaitlis'] == "Daudzskaitlis":
                                output = output + line['Vārds'] + "; "
                    except Exception as inst:
                        pass
                output = output + """</td><td id="loc_tab">"""
                for line in input_data:
                    try:
                        if line['Persona'] == "3":
                            if line['Skaitlis'] == "Nepiemīt":
                                output = output + line['Vārds'] + "; "
                    except Exception as inst:
                        pass
            output = output + """</td></tr></table>"""
        #Ja persona nepiemīt, izvada vāru, kā arī informāciju, par to vai vārds ir vienskaitlī, daudzskaitlī vai tam skaitlis nepiemīt
        for line in input_data:
            try:
                if line['Persona'] == "Nepiemīt":
                    output = output + """<p><b1>""" + line['Vārds'] + """: </b1>Skaitlis: """ + line['Skaitlis'] + """</p>"""
            except Exception as inst:
                pass
        output = output + """</div>"""
    except Exception as inst:
        pass
    return output
