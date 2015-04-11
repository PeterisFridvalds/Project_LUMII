from website import person_analizer
from website import noun_analizer
from website import noun_analizer_no_count

def verb_analizer(input_data):
    output = ""
    divdabis = []
    isten_izt = []
    atst_izt = []
    vele_izt = []
    vajadz_izt = []
    pav_izt = []
    nenot = []
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
            except Exception as inst:
                pass
    except Exception as inst:
        pass
    output = output + """<div class="inside_box">""" #checkbox, lai varētu apskatīt tikai interesējošās izteiksmes un pārējās paslēpt
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
    output = output + """<br></div>"""
    #HTML kods katai izteikmei, izsauc nepieciešamās f-jas dažādām izteiksmēm
    if nenot != []:
        for line in nenot:
            output = output + """<div class="nenot"><p><b1>Darbības vārds nenoteiksmē: </b1>""" + line['Vārds'] + """</p><br></div>"""
    if isten_izt != []:
        output = output + """<div class="isten_izt"><p><b1>Darbības vārds īstenības izteiksmē</b1></p>""" + person_analizer.person_analizer(isten_izt) + """<br></div>"""
    if atst_izt != []:
        output = output + """<div class="atst_izt"><p><b1>Darbības vārds atstāstījuma izteiksmē</b1></p>""" + person_analizer.person_analizer(atst_izt) + """<br></div>"""
    if vele_izt != []:
        output = output + """<div class="vele_izt"><p><b1>Darbības vārds vēlējuma izteiksmē</b1></p>""" + person_analizer.person_analizer(vele_izt) + """<br></div>"""
    if vajadz_izt != []:
        output = output + """<div class="vajadz_izt"><p><b1>Darbības vārds vajadzības izteiksmē</b1></p>""" + person_analizer.person_analizer(vajadz_izt) + """<br></div>"""
    if pav_izt != []:
        output = output + """<div class="pav_izt"><p><b1>Darbības vārds pavēles izteiksmē</b1></p>""" + person_analizer.person_analizer(pav_izt) + """<br></div>"""
        
    return output
