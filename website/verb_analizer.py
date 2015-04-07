from website import noun_analizer
from website import noun_analizer_no_count

def verb_analizer(input_data):
    output = ""
    pag_v = []
    pag_s = []
    pag_nepiem = []
    pag_navsk_v = []
    pag_navsk_s = []
    pag_navsk_nepiem = []
    tag_v = []
    tag_s = []
    tag_nepiem = []
    tag_navsk_v = []
    tag_navsk_s = []
    tag_navsk_nepiem = []
    nak_v = []
    nak_s = []
    nak_nepiem = []
    nak_navsk_v = []
    nak_navsk_s = []
    nak_navsk_nepiem = []
    nep_v = []
    nep_s = []
    nep_nepiem = []
    nep_navsk_v = []
    nep_navsk_s = []
    nep_navsk_nepiem = []
    leftower = []
    try:
        for line in input_data:
            try:
                if line['Locījums'] != "Nepiemīt":
                    if line['Laiks'] == "Pagātne":
                        if (line['Skaitlis'] == "Vienskaitlis") or (line['Skaitlis'] == "Daudzskaitlis"):
                            if line['Dzimte'] == "Vīriešu":
                                pag_v.append(line)
                            elif line['Dzimte'] == "Sieviešu":
                                pag_s.append(line)
                            else:
                                pag_nepiem.append(line)
                        elif line['Skaitlis'] == "Nepiemīt":
                            if line['Dzimte'] == "Vīriešu":
                                pag_navsk_v.append(line)
                            elif line['Dzimte'] == "Sieviešu":
                                pag_navsk_s.append(line)
                            else:
                                pag_navsk_nepiem.append(line)
                    elif line['Laiks'] == "Tagadne":
                        if (line['Skaitlis'] == "Vienskaitlis") or (line['Skaitlis'] == "Daudzskaitlis"):
                            if line['Dzimte'] == "Vīriešu":
                                tag_v.append(line)
                            elif line['Dzimte'] == "Sieviešu":
                                tag_s.append(line)
                            else:
                                tag_nepiem.append(line)
                        elif line['Skaitlis'] == "Nepiemīt":
                            if line['Dzimte'] == "Vīriešu":
                                tag_navsk_v.append(line)
                            elif line['Dzimte'] == "Sieviešu":
                                tag_navsk_s.append(line)
                            else:
                                tag_navsk_nepiem.append(line)
                    elif line['Laiks'] == "Nākotne":
                        if (line['Skaitlis'] == "Vienskaitlis") or (line['Skaitlis'] == "Daudzskaitlis"):
                            if line['Dzimte'] == "Vīriešu":
                                nak_v.append(line)
                            elif line['Dzimte'] == "Sieviešu":
                                nak_s.append(line)
                            else:
                                nak_nepiem.append(line)
                        elif line['Skaitlis'] == "Nepiemīt":
                            if line['Dzimte'] == "Vīriešu":
                                nak_navsk_v.append(line)
                            elif line['Dzimte'] == "Sieviešu":
                                nak_navsk_s.append(line)
                            else:
                                nak_navsk_nepiem.append(line)
                    elif line['Laiks'] == "Nepiemīt":
                        if (line['Skaitlis'] == "Vienskaitlis") or (line['Skaitlis'] == "Daudzskaitlis"):
                            if line['Dzimte'] == "Vīriešu":
                                nep_v.append(line)
                            elif line['Dzimte'] == "Sieviešu":
                                nep_s.append(line)
                            else:
                                nep_nepiem.append(line)
                        elif line['Skaitlis'] == "Nepiemīt":
                            if line['Dzimte'] == "Vīriešu":
                                nep_navsk_v.append(line)
                            elif line['Dzimte'] == "Sieviešu":
                                nep_navsk_s.append(line)
                            else:
                                nep_navsk_nepiem.append(line)
                else:
                    leftower.append(line)
            except Exception as inst:
                pass
    except Exception as inst:
        pass
    try:
        if pag_v != []:
            output = output + """<p class="inside_box"><b1>Pagātne, vīriešu dzimte</b1></p>""" + noun_analizer.noun_analizer(pag_v)
    except Exception as inst:
        pass
    try:
        if pag_s != []:
            output = output + """<p class="inside_box"><b1>Pagātne, sieviešu dzimte</b1></p>""" + noun_analizer.noun_analizer(pag_s)
    except Exception as inst:
        pass
    try:
        if pag_nepiem != []:
            output = output + """<p class="inside_box"><b1>Pagātne, dzimte nepiemīt</b1></p>""" + noun_analizer.noun_analizer(pag_nepiem)
    except Exception as inst:
        pass
    
    try:
        if pag_navsk_v != []:
            output = output + """<p class="inside_box"><b1>Pagātne, skaitlis nepiemīt, vīriešu dzimte</b1></p>""" + noun_analizer_no_count.noun_analizer(pag_navsk_v)
    except Exception as inst:
        pass
    try:
        if pag_navsk_s != []:
            output = output + """<p class="inside_box"><b1>Pagātne, skaitlis nepiemīt, sieviešu dzimte</b1></p>""" + noun_analizer_no_count.noun_analizer(pag_navsk_s)
    except Exception as inst:
        pass
    try:
        if pag_navsk_nepiem != []:
            output = output + """<p class="inside_box"><b1>Pagātne, skaitlis nepiemīt, dzimte nepiemīt</b1></p>""" + noun_analizer_no_count.noun_analizer(pag_navsk_nepiem)
    except Exception as inst:
        pass
    try:
        if tag_v != []:
            output = output + """<p class="inside_box"><b1>Tagadne, vīriešu dzimte</b1></p>""" + noun_analizer.noun_analizer(tag_v)
    except Exception as inst:
        pass
    try:
        if tag_s != []:
            output = output + """<p class="inside_box"><b1>Tagadne, sieviešu dzimte</b1></p>""" + noun_analizer.noun_analizer(tag_s)
    except Exception as inst:
        pass
    try:
        if tag_nepiem != []:
            output = output + """<p class="inside_box"><b1>Tagadne, dzimte nepiemīt</b1></p>""" + noun_analizer.noun_analizer(tag_nepiem)
    except Exception as inst:
        pass
    
    try:
        if tag_navsk_v != []:
            output = output + """<p class="inside_box"><b1>Tagadne, skaitlis nepiemīt, vīriešu dzimte</b1></p>""" + noun_analizer_no_count.noun_analizer(tag_navsk_v)
    except Exception as inst:
        pass
    try:
        if tag_navsk_s != []:
            output = output + """<p class="inside_box"><b1>Tagadne, skaitlis nepiemīt, sieviešu dzimte</b1></p>""" + noun_analizer_no_count.noun_analizer(tag_navsk_s)
    except Exception as inst:
        pass
    try:
        if tag_navsk_nepiem != []:
            output = output + """<p class="inside_box"><b1>Tagadne, skaitlis nepiemīt, dzimte nepiemīt</b1></p>""" + noun_analizer_no_count.noun_analizer(tag_navsk_nepiem)
    except Exception as inst:
        pass
    try:
        if nak_v != []:
            output = output + """<p class="inside_box"><b1>Nākotne, vīriešu dzimte</b1></p>""" + noun_analizer.noun_analizer(nak_v)
    except Exception as inst:
        pass
    try:
        if nak_s != []:
            output = output + """<p class="inside_box"><b1>Nākotne, sieviešu dzimte</b1></p>""" + noun_analizer.noun_analizer(nak_s)
    except Exception as inst:
        pass
    try:
        if nak_nepiem != []:
            output = output + """<p class="inside_box"><b1>Nākotne, dzimte nepiemīt</b1></p>""" + noun_analizer.noun_analizer(nak_nepiem)
    except Exception as inst:
        pass
    
    try:
        if nak_navsk_v != []:
            output = output + """<p class="inside_box"><b1>Nākotne, skaitlis nepiemīt, vīriešu dzimte</b1></p>""" + noun_analizer_no_count.noun_analizer(nak_navsk_v)
    except Exception as inst:
        pass
    try:
        if nak_navsk_s != []:
            output = output + """<p class="inside_box"><b1>Nākotne, skaitlis nepiemīt, sieviešu dzimte</b1></p>""" + noun_analizer_no_count.noun_analizer(nak_navsk_s)
    except Exception as inst:
        pass
    try:
        if nak_navsk_nepiem != []:
            output = output + """<p class="inside_box"><b1>Nākotne, skaitlis nepiemīt, dzimte nepiemīt</b1></p>""" + noun_analizer_no_count.noun_analizer(nak_navsk_nepiem)
    except Exception as inst:
        pass
    try:
        if nep_v != []:
            output = output + """<p class="inside_box"><b1>Laiks nepiemīt, vīriešu dzimte</b1></p>""" + noun_analizer.noun_analizer(nep_v)
    except Exception as inst:
        pass
    try:
        if nep_s != []:
            output = output + """<p class="inside_box"><b1>Laiks nepiemīt, sieviešu dzimte</b1></p>""" + noun_analizer.noun_analizer(nep_s)
    except Exception as inst:
        pass
    try:
        if nep_nepiem != []:
            output = output + """<p class="inside_box"><b1>Laiks nepiemīt, dzimte nepiemīt</b1></p>""" + noun_analizer.noun_analizer(nep_nepiem)
    except Exception as inst:
        pass
    
    try:
        if nep_navsk_v != []:
            output = output + """<p class="inside_box"><b1>Laiks nepiemīt, skaitlis nepiemīts, vīriešu dzimte</b1></p>""" + noun_analizer_no_count.noun_analizer(nep_navsk_v)
    except Exception as inst:
        pass
    try:
        if nep_navsk_s != []:
            output = output + """<p class="inside_box"><b1>Laiks nepiemīt, skaitlis nepiemīt, sieviešu dzimte</b1></p>""" + noun_analizer_no_count.noun_analizer(nep_navsk_s)
    except Exception as inst:
        pass
    try:
        if nep_navsk_nepiem != []:
            output = output + """<p class="inside_box"><b1>Laiks nepiemīt, skaitlis nepiemīt, dzimte nepiemīt</b1></p>""" + noun_analizer_no_count.noun_analizer(nep_navsk_nepiem)
    except Exception as inst:
        pass
    try:
        for line in leftower:
            output = output + """<p style="max-width: 500px"> Leftower """
            for key in line:
                output = output + """<b1>""" + key + """</b1>""" + " - " + line[key] + "; "
            output = output + """</p>"""
    except Exception as inst:
        pass
    return output
