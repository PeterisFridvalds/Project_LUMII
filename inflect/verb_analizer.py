from website import person_analizer
from website import divdab_analizer

#Funkcija, kas analizē darbības vārdus
def verb_analizer(input_data, keys = ["Vārdšķira"]):
    output = ""
    divdabis = []
    isten_izt = []
    atst_izt = []
    vele_izt = []
    vajadz_izt = []
    pav_izt = []
    nenot = []
    leftower = []
    keys.append("Izteiksme")
    try:
        #Iedala iegūto informāciju pēc izteiksmēm
        for line in input_data:
            try:
                if line['Izteiksme'] == "Nenoteiksme":
                    nenot.append(line)
                elif line['Izteiksme'] == "Īstenības":
                    isten_izt.append(line)
                elif line['Izteiksme'] == "Atstāstījuma":
                    atst_izt.append(line)
                elif line['Izteiksme'] == "Vēlējuma":
                    vele_izt.append(line)
                elif line['Izteiksme'] == "Vajadzības":
                    vajadz_izt.append(line)
                elif line['Izteiksme'] == "Pavēles":
                    pav_izt.append(line)
                elif line['Izteiksme'] == "Divdabis":
                    divdabis.append(line)
                else:
                    leftower.append(line)
            except Exception as inst:
                pass
    except Exception as inst:
        pass

    #checkbox, lai varētu apskatīt tikai interesējošās izteiksmes un pārējās paslēpt
    output = output + '<table><tr><td style="vertical-align:top">'
    try:
        output = output + """<div class="inside_box">"""
        if nenot != []:
            output = output + """<label><input type="checkbox" value="nenot" checked> Nonoteiksme</label><br>"""
        if isten_izt != []:
            output = output + """<label><input type="checkbox" value="isten_izt" checked> Īstenības izteiksme</label><br>"""
        if atst_izt != []:
            output = output + """<label><input type="checkbox" value="atst_izt" checked> Atstāstījuma izteiksme</label><br>"""
        if vele_izt != []:
            output = output + """<label><input type="checkbox" value="vele_izt" checked> Vēlējuma izteiksme</label><br>"""
        if vajadz_izt != []:
            output = output + """<label><input type="checkbox" value="vajadz_izt" checked> Vajadzibas izteiksme</label><br>"""
        if pav_izt != []:
            output = output + """<label><input type="checkbox" value="pav_izt" checked> Pavēles izteiksme</label><br>"""
        if divdabis != []:
            output = output + """<label><input type="checkbox" value="divdabis" checked> Divdabji</label><br>"""
        if leftower != []:
            output = output + """<label><input type="checkbox" value="leftower" checked> Citi</label><br>"""
        output = output + """<br></div>"""
    except Exception as inst:
        pass
    output = output + '</td><td>'
    
    #HTML kods katai izteikmei, izsauc nepieciešamās f-jas dažādām izteiksmēm
    output = output + '<table>'
    try:
        if nenot != []:
            for line in nenot:
                output = output + """<tr><td><div class="nenot"><p><b1>Darbības vārds nenoteiksmē: </b1>""" + line['Vārds'] + """</p><br></div></tr></td>"""
        if isten_izt != []:
            output = output + """<tr><td><div class="isten_izt"><p><b1>Darbības vārds īstenības izteiksmē</b1></p><ul class="table_layout">""" + person_analizer.person_analizer(isten_izt, keys) + """</ul><br></div></tr></td>"""
        if atst_izt != []:
            output = output + """<tr><td><div class="atst_izt"><p><b1>Darbības vārds atstāstījuma izteiksmē</b1></p><ul class="table_layout">""" + person_analizer.person_analizer(atst_izt, keys) + """</ul><br></div></tr></td>"""
        if vele_izt != []:
            output = output + """<tr><td><div class="vele_izt"><p><b1>Darbības vārds vēlējuma izteiksmē</b1></p><ul class="table_layout">""" + person_analizer.person_analizer(vele_izt, keys) + """</ul><br></div></tr></td>"""
        if vajadz_izt != []:
            output = output + """<tr><td><div class="vajadz_izt"><p><b1>Darbības vārds vajadzības izteiksmē</b1></p><ul class="table_layout">""" + person_analizer.person_analizer(vajadz_izt, keys) + """</ul><br></div></tr></td>"""
        if pav_izt != []:
            output = output + """<tr><td><div class="pav_izt"><p><b1>Darbības vārds pavēles izteiksmē</b1></p><ul class="table_layout">""" + person_analizer.person_analizer(pav_izt, keys) + """</ul><br></div></tr></td>"""
        if divdabis != []:
            output = output + """<tr><td><div class="divdabis"><p><b1>Darbības vārda divdabja formas</b1></p><ul class="table_layout">""" + divdab_analizer.divdab_analizer(divdabis, keys) + """</ul><br></div></tr></td>"""
        if leftower != []:
            output = output + """<tr><td><div class="leftower"><p><b1>Cita darbības vārda forma</b1></p><ul class="table_layout">""" + person_analizer.person_analizer(leftower, keys) + """</ul><br></div></tr></td>"""
    except Exception as inst:
        pass
    output = output + '</table>'

    output = output + '</td></tr></table>'
    
    return output
