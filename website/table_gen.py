from website import unknown_analizer

#Ģenerē tabulu izvadei
def table_gen(input_data, keys = []):
    output = ""
    N = []
    G = []
    D = []
    A = []
    L = []
    V = []
    No_loc = []
    vsk = 0
    dsk = 0
    no_sk = 0

    for line in input_data:
        #Pārbauda, kādi skaitļi ir iedotajiem datiem
        try:
            if line['Skaitlis'] == "Vienskaitlis":
                vsk = 1
            elif line['Skaitlis'] == "Daudzskaitlis":
                dsk = 1
            else:
                no_sk = 1
        except Exception as inst:
            no_sk = 1

        #Pārbauda, kādi locījumi ir iedotajiem datiem un iedala datus pēc locijumiem
        try:
            if line['Locījums'] == "Nominatīvs":
                N.append(line)
            elif line['Locījums'] == "Ģenitīvs":
                G.append(line)
            elif line['Locījums'] == "Datīvs":
                D.append(line)
            elif line['Locījums'] == "Akuzatīvs":
                A.append(line)
            elif line['Locījums'] == "Lokatīvs":
                L.append(line)
            elif line['Locījums'] == "Vokatīvs":
                V.append(line)
            else:
                No_loc.append(line)
        except Exception as inst:
            No_loc.append(line)

    #Ja ir kāds locijums, ģenerē tabulas galvu nepieciesamo kolonnu skaitu, katrai tabulas rinadi izsauc funkciju, kas ģenerē attiecīgo rindu
    try:
        if (N != []) or (G != []) or (D != []) or (A != []) or (L != []) or (V != []):
            output = output + """<div class="inflect"><table id="auto_table">
                        <tr><td><b1>Locījums</b1></td>"""
            if vsk == 1:
                output = output + """<td><b1>Viensk.</b1></td>"""
            if dsk == 1:
                output = output + """<td><b1>Daudzsk.</b1></td>"""
            if no_sk == 1:
                output = output + """<td><b1>Skaitlis nepiemīt</b1></td>"""
            output = output + """</tr>"""
            if N != []:
                output = output + """<tr><td><b1>Nominatīvs</b1></td>""" + loc_gen(N, vsk, dsk, no_sk) + """</tr>"""
            if G != []:
                output = output + """<tr><td><b1>Ģenitīvs</b1></td>""" + loc_gen(G, vsk, dsk, no_sk) + """</tr>"""
            if D != []:
                output = output + """<tr><td><b1>Datīvs</b1></td>""" + loc_gen(D, vsk, dsk, no_sk) + """</tr>"""
            if A != []:
                output = output + """<tr><td><b1>Akuzatīvs</b1></td>""" + loc_gen(A, vsk, dsk, no_sk) + """</tr>"""
            if L != []:
                output = output + """<tr><td><b1>Lokatīvs</b1></td>""" + loc_gen(L, vsk, dsk, no_sk) + """</tr>"""
            if V != []:
                output = output + """<tr><td><b1>Vokatīvs</b1></td>""" + loc_gen_v(V, vsk, dsk, no_sk) + """</tr>"""
            output = output + "</table></div>"
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
def loc_gen(input_data, vsk, dsk, no_sk):
    output = ""
    if vsk == 1:
        output = output + """<td id="loc_tab">"""
        try:
            for line in input_data:
                if line['Skaitlis'] == "Vienskaitlis":
                    output = output + line['Vārds'] + "; "
        except Exception as inst:
            pass
        output = output + """</td>"""
    if dsk == 1:
        output = output + """<td id="loc_tab">"""
        try:
            for line in input_data:
                if line['Skaitlis'] == "Daudzskaitlis":
                    output = output + line['Vārds'] + "; "
        except Exception as inst:
            pass
        output = output + """</td>"""
    if no_sk == 1:
        output = output + """<td id="loc_tab">"""
        try:
            for line in input_data:
                if line['Skaitlis'] == "Vienskaitlis":
                    pass
                elif line['Skaitlis'] == "Daudzskaitlis":
                    pass
                else:
                    output = output + line['Vārds'] + "; "
        except Exception as inst:
            pass
        output = output + """</td>"""
    output = output.replace("""; </td>""", """</td>""")
    output = output.replace("""<td id="loc_tab"></td>""", """<td id="loc_tab"> - </td>""")
    return output

def loc_gen_v(input_data, vsk, dsk, no_sk):
    output = ""
    if vsk == 1:
        output = output + """<td id="loc_tab">"""
        try:
            for line in input_data:
                if line['Skaitlis'] == "Vienskaitlis":
                    output = output + line['Vārds'] + "! "
        except Exception as inst:
            pass
        output = output + """</td>"""
    if dsk == 1:
        output = output + """<td id="loc_tab">"""
        try:
            for line in input_data:
                if line['Skaitlis'] == "Daudzskaitlis":
                    output = output + line['Vārds'] + "! "
        except Exception as inst:
            pass
        output = output + """</td>"""
    if no_sk == 1:
        output = output + """<td id="loc_tab">"""
        try:
            for line in input_data:
                if line['Skaitlis'] == "Vienskaitlis":
                    pass
                elif line['Skaitlis'] == "Daudzskaitlis":
                    pass
                else:
                    output = output + line['Vārds'] + "! "
        except Exception as inst:
            pass
        output = output + """</td>"""
    output = output.replace("""<td id="loc_tab"></td>""", """<td id="loc_tab"> - </td>""")
    return output
