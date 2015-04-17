from website import table_gen_sk
from website import table_gen_no_sk
from website import unknown_analizer

def divdab_analizer(input_data):
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
                output = output + """<p class="inside_box"><b1>Pagātne:</b1></p>""" + sk_dzimt_analizer(past)
        except Exception as inst:
            pass
        try:
            if present != []:
                output = output + """<p class="inside_box"><b1>Tagadne:</b1></p>""" + sk_dzimt_analizer(present)
        except Exception as inst:
            pass
        try:
            if future != []:
                output = output + """<p class="inside_box"><b1>Nākotne:</b1></p>""" + sk_dzimt_analizer(future)
        except Exception as inst:
            pass
        try:
            if no_time != []:
                output = output + """<p class="inside_box"><b1>Laiks nepiemīt:</b1></p>""" + sk_dzimt_analizer(no_time)
        except Exception as inst:
            pass
    except Exception as inst:
        pass
    return output

def sk_dzimt_analizer(input_data):
    output = ""
    sk_vir = []
    sk_siev = []
    sk_bezdz = []
    sk_bez_loc = []
    siev = []
    vir = []
    bez_loc = []
    bezdz = []
    try:
        #Ārējais cikls ieadala iedotos datus pēc skaitļa, iekšejais - pēc dzimtes
        for line in input_data:
            try:
                if (line['Skaitlis'] == "Vienskaitlis") or (line['Skaitlis'] == "Daudzskaitlis"):
                    if line['Dzimte'] == "Vīriešu":
                        sk_vir.append(line)
                    elif line['Dzimte'] == "Sieviešu":
                        sk_siev.append(line)
                    elif line['Locījums'] == "Nepiemīt":
                        bez_loc.append(line)
                    else:
                        sk_bezdz.append(line)
                else:
                    if line['Dzimte'] == "Vīriešu":
                        vir.append(line)
                    elif line['Dzimte'] == "Sieviešu":
                        siev.append(line)
                    elif line['Locījums'] == "Nepiemīt":
                        bez_loc.append(line)
                    else:
                        bezdz.append(line)
            except Exception as inst:
                pass
        try:
            if sk_vir != []:
                output = output + """<p class="double_inside_box"><b1>Vīriesu dzimte</b1></p>""" + table_gen_sk.table_gen_sk(sk_vir)
            if sk_siev != []:
                output = output + """<p class="double_inside_box"><b1>Sieviešu dzimte</b1></p>""" + table_gen_sk.table_gen_sk(sk_siev)
            if sk_bezdz != []:
                output = output + """<p class="double_inside_box"><b1>Dzimte nepiemīt</b1></p>""" + table_gen_sk.table_gen_sk(sk_bezdz)
            if vir != []:
                output = output + """<p class="double_inside_box"><b1>Vīriesu dzimte, skaitlis nepiemīt</b1></p>""" + table_gen_no_sk.table_gen_no_sk(vir)
            if siev != []:
                output = output + """<p class="double_inside_box"><b1>Sieviešu dzimte, skaitlis nepiemīt</b1></p>""" + table_gen_no_sk.table_gen_no_sk(siev)
            if bezdz != []:
                output = output + """<p class="double_inside_box"><b1>Dzimte nepiemīt, skaitlis nepiemīt</b1></p>""" + table_gen_no_sk.table_gen_no_sk(bezdz)
            if bez_loc != []:
                output = output + unknown_analizer.unknown_analizer(bez_loc)
        except Exception as inst:
            pass
    except Exception as inst:
        pass
    return output
