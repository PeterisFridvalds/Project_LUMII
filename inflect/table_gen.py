# -*- coding: utf-8 -*-
from inflect import unknown_analizer

##Ģenerē tabulu izvadei
def table_gen(input_data, keys = []):
    output = ''
    N = []
    G = []
    D = []
    A = []
    L = []
    V = []
    No_loc = []
    vsk = False
    dsk = False
    no_sk = False
    keys.append(u'Locījums')

    for line in input_data:
        #Pārbauda, kādi skaitļi ir iedotajiem datiem
        try:
            if line[u'Skaitlis'] == u"Vienskaitlis":
                vsk = True
            elif line[u'Skaitlis'] == u"Daudzskaitlis":
                dsk = True
            else:
                no_sk = True
        except Exception as inst:
            no_sk = True

        #Pārbauda, kādi locījumi ir iedotajiem datiem un iedala datus pēc locijumiem
        try:
            if line[u'Locījums'] == u"Nominatīvs":
                N.append(line)
            elif line[u'Locījums'] == u"Ģenitīvs":
                G.append(line)
            elif line[u'Locījums'] == u"Datīvs":
                D.append(line)
            elif line[u'Locījums'] == u"Akuzatīvs":
                A.append(line)
            elif line[u'Locījums'] == u"Lokatīvs":
                L.append(line)
            elif line[u'Locījums'] == u"Vokatīvs":
                V.append(line)
            else:
                No_loc.append(line)
        except Exception as inst:
            No_loc.append(line)

    #Ja ir kāds locijums, ģenerē tabulas galvu nepieciesamo kolonnu skaitu, katrai tabulas rinadi izsauc funkciju, kas ģenerē attiecīgo rindu
    try:
        if (N != []) or (G != []) or (D != []) or (A != []) or (L != []) or (V != []):
            output = output + u'<div class="inflect"><table id="auto_table"><tr><td><b1>Locījums</b1></td>'
            if vsk == True:
                output = output + u'<td><b1>Viensk.</b1></td>'
            if dsk == True:
                output = output + u'<td><b1>Daudzsk.</b1></td>'
            if no_sk == True:
                output = output + u'<td><b1>Skaitlis nepiemīt</b1></td>'
            output = output + u'</tr>'
            if N != []:
                output = output + u'<tr><td><b1>Nominatīvs</b1></td>' + loc_gen(N, vsk, dsk, no_sk, keys) + u'</tr>'
            if G != []:
                output = output + u'<tr><td><b1>Ģenitīvs</b1></td>' + loc_gen(G, vsk, dsk, no_sk, keys) + u'</tr>'
            if D != []:
                output = output + u'<tr><td><b1>Datīvs</b1></td>' + loc_gen(D, vsk, dsk, no_sk, keys) + u'</tr>'
            if A != []:
                output = output + u'<tr><td><b1>Akuzatīvs</b1></td>' + loc_gen(A, vsk, dsk, no_sk, keys) + u'</tr>'
            if L != []:
                output = output + u'<tr><td><b1>Lokatīvs</b1></td>' + loc_gen(L, vsk, dsk, no_sk, keys) + u'</tr>'
            if V != []:
                output = output + u'<tr><td><b1>Vokatīvs</b1></td>' + loc_gen_v(V, vsk, dsk, no_sk, keys) + u'</tr>'
            output = output + u'</table><br></div>'
    except Exception as inst:
        pass

    #Ja vārdus, kuriem nepiemīt locījums, nodod funkcijai, kas apstrādā šos datus
    try:
        if No_loc != []:
            output = output + unknown_analizer.unknown_analizer(No_loc, keys)
    except Exception as inst:
        pass
    
    return output

#Funkcija, kas ģenerē
def loc_gen(input_data, vsk, dsk, no_sk, keys = []):
    output = ''
    if vsk == True:
        output = output + u'<td id="loc_tab">'
        try:
            for line in input_data:
                if line[u'Skaitlis'] == u"Vienskaitlis":
                    output = output + line[u'Vārds'] + u"; "
        except Exception as inst:
            pass
        output = output + u'</td>'
    if dsk == True:
        output = output + u'<td id="loc_tab">'
        try:
            for line in input_data:
                if line[u'Skaitlis'] == u"Daudzskaitlis":
                    output = output + line[u'Vārds'] + u"; "
        except Exception as inst:
            pass
        output = output + u'</td>'
    if no_sk == True:
        output = output + u'<td id="loc_tab">'
        try:
            for line in input_data:
                if line[u'Skaitlis'] == u"Vienskaitlis":
                    pass
                elif line[u'Skaitlis'] == u"Daudzskaitlis":
                    pass
                else:
                    output = output + line[u'Vārds'] + u"; "
        except Exception as inst:
            pass
        output = output + u'</td>'
    output = output.replace('; </td>', '</td>')
    output = output.replace('<td id="loc_tab"></td>', '<td id="loc_tab"> - </td>')
    return output

def loc_gen_v(input_data, vsk, dsk, no_sk, keys = []):
    output = ''
    if vsk == True:
        output = output + u'<td id="loc_tab">'
        try:
            for line in input_data:
                if line[u'Skaitlis'] == u"Vienskaitlis":
                    output = output + line[u'Vārds'] + u"! "
        except Exception as inst:
            pass
        output = output + u'</td>'
    if dsk == True:
        output = output + u'<td id="loc_tab">'
        try:
            for line in input_data:
                if line[u'Skaitlis'] == u"Daudzskaitlis":
                    output = output + line[u'Vārds'] + u"! "
        except Exception as inst:
            pass
        output = output + u'</td>'
    if no_sk == True:
        output = output + u'<td id="loc_tab">'
        try:
            for line in input_data:
                if line[u'Skaitlis'] == u"Vienskaitlis":
                    pass
                elif line[u'Skaitlis'] == u"Daudzskaitlis":
                    pass
                else:
                    output = output + line[u'Vārds'] + u"! "
        except Exception as inst:
            pass
        output = output + u'</td>'
    output = output.replace(u'<td id="loc_tab"></td>', u'<td id="loc_tab"> - </td>')
    return output
