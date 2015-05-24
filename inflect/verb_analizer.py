# -*- coding: utf-8 -*-
from inflect import person_analizer
from inflect import divdab_analizer

##Funkcija, kas analizē darbības vārdus
def verb_analizer(input_data, keys = [u"Vārdšķira"]):
    output = ""
    divdabis = []
    isten_izt = []
    atst_izt = []
    vele_izt = []
    vajadz_izt = []
    pav_izt = []
    nenot = []
    leftower = []
    keys.append(u"Izteiksme")
    try:
        ##Iedala iegūto informāciju pēc izteiksmēm
        for line in input_data:
            try:
                if line[u'Izteiksme'] == u"Nenoteiksme":
                    nenot.append(line)
                elif line[u'Izteiksme'] == u"Īstenības":
                    isten_izt.append(line)
                elif line[u'Izteiksme'] == u"Atstāstījuma":
                    atst_izt.append(line)
                elif line[u'Izteiksme'] == u"Vēlējuma":
                    vele_izt.append(line)
                elif line[u'Izteiksme'] == u"Vajadzības":
                    vajadz_izt.append(line)
                elif line[u'Izteiksme'] == u"Pavēles":
                    pav_izt.append(line)
                elif line[u'Izteiksme'] == u"Divdabis":
                    divdabis.append(line)
                else:
                    leftower.append(line)
            except Exception as inst:
                pass
    except Exception as inst:
        pass

    ##checkbox, lai varētu apskatīt tikai interesējošās izteiksmes un pārējās paslēpt
    output = output + u'<table><tr><td style="vertical-align:top">'
    try:
        output = output + u'<div class="inside_box">'
        if nenot != []:
            output = output + u'<label><input type="checkbox" value="nenot" checked> Nonoteiksme</label>'
        if isten_izt != []:
            output = output + u'<label><input type="checkbox" value="isten_izt" checked> Īstenības izteiksme</label>'
        if atst_izt != []:
            output = output + u'<label><input type="checkbox" value="atst_izt" checked> Atstāstījuma izteiksme</label>'
        if vele_izt != []:
            output = output + u'<label><input type="checkbox" value="vele_izt" checked> Vēlējuma izteiksme</label>'
        if vajadz_izt != []:
            output = output + u'<label><input type="checkbox" value="vajadz_izt" checked> Vajadzibas izteiksme</label>'
        if pav_izt != []:
            output = output + u'<label><input type="checkbox" value="pav_izt" checked> Pavēles izteiksme</label>'
        if divdabis != []:
            output = output + u'<label><input type="checkbox" value="divdabis" checked> Divdabji</label>'
        if leftower != []:
            output = output + u'<label><input type="checkbox" value="leftower" checked> Citi</label>'
        output = output + u'<br></div>'
    except Exception as inst:
        pass
    output = output + u'</td></tr><tr><td>'
    
    ##HTML kods katai izteikmei, izsauc nepieciešamās f-jas dažādām izteiksmēm
    output = output + u'<table>'
    try:
        if nenot != []:
            for line in nenot:
                output = output + u'<tr><td><div class="nenot"><p><b1>Darbības vārds nenoteiksmē: </b1>' + line[u'Vārds'] + u'</p><br></div></tr></td>'
        if isten_izt != []:
            output = output + u'<tr><td><div class="isten_izt"><p><b1>Darbības vārds īstenības izteiksmē</b1></p><ul class="table_layout">' + person_analizer.person_analizer(isten_izt, keys) + u'</ul><br></div></tr></td>'
        if atst_izt != []:
            output = output + u'<tr><td><div class="atst_izt"><p><b1>Darbības vārds atstāstījuma izteiksmē</b1></p><ul class="table_layout">' + person_analizer.person_analizer(atst_izt, keys) + u'</ul><br></div></tr></td>'
        if vele_izt != []:
            output = output + u'<tr><td><div class="vele_izt"><p><b1>Darbības vārds vēlējuma izteiksmē</b1></p><ul class="table_layout">' + person_analizer.person_analizer(vele_izt, keys) + u'</ul><br></div></tr></td>'
        if vajadz_izt != []:
            output = output + u'<tr><td><div class="vajadz_izt"><p><b1>Darbības vārds vajadzības izteiksmē</b1></p><ul class="table_layout">' + person_analizer.person_analizer(vajadz_izt, keys) + u'</ul><br></div></tr></td>'
        if pav_izt != []:
            output = output + u'<tr><td><div class="pav_izt"><p><b1>Darbības vārds pavēles izteiksmē</b1></p><ul class="table_layout">' + person_analizer.person_analizer(pav_izt, keys) + u'</ul><br></div></tr></td>'
        if divdabis != []:
            output = output + u'<tr><td><div class="divdabis"><p><b1>Darbības vārda divdabja formas</b1></p><ul class="table_layout">' + divdab_analizer.divdab_analizer(divdabis, keys) + u'</ul><br></div></tr></td>'
        if leftower != []:
            output = output + u'<tr><td><div class="leftower"><p><b1>Cita darbības vārda forma</b1></p><ul class="table_layout">' + person_analizer.person_analizer(leftower, keys) + u'</ul><br></div></tr></td>'
    except Exception as inst:
        pass
    output = output + u'</table>'

    output = output + u'</td></tr></table>'
    
    return output
