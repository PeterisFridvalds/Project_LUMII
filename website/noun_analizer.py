from website import table_gen

#Funkcija, kas analizē lietvārdus
def noun_analizer(input_data, keys = ["Vārdšķira"]):
    output = ""
    dekl_1 = []
    dekl_2 = []
    dekl_3 = []
    dekl_4 = []
    dekl_5 = []
    dekl_6 = []
    no_dekl = []
    dekl = []
    keys.append('Deklinācija')
    try:
        #Ieadala iedotos datus pēc deklinācijām
        for line in input_data:
            try:
                if line['Deklinācija'] == "1":
                    dekl_1.append(line)
                elif line['Deklinācija'] == "2":
                    dekl_2.append(line)
                elif line['Deklinācija'] == "3":
                    dekl_3.append(line)
                elif line['Deklinācija'] == "4":
                    dekl_4.append(line)
                elif line['Deklinācija'] == "5":
                    dekl_5.append(line)
                elif line['Deklinācija'] == "6":
                    dekl_6.append(line)
                elif line['Deklinācija'] == "0":
                    no_dekl.append(line)
                elif line['Deklinācija'] == "Nepiemīt":
                    no_dekl.append(line)
                else:
                    dekl.append(line)
            except Exception as inst:
                dekl.append(line)
                
        #Pārbauda, vai ir kaut kādi dati, kas atiecas uz attiecīgo deklināciju, ja tādi ir, izsauc f-ju, kas izveido HTML kodu locījumiem
        try:
            if dekl_1 != []:
                output = output + """<p class="inside_box"><b1>1. deklinācija:</b1></p>""" + table_gen.table_gen(dekl_1, keys)
            if dekl_2 != []:
                output = output + """<p class="inside_box"><b1>2. deklinācija:</b1></p>""" + table_gen.table_gen(dekl_2, keys)
            if dekl_3 != []:
                output = output + """<p class="inside_box"><b1>3. deklinācija:</b1></p>""" + table_gen.table_gen(dekl_3, keys)
            if dekl_4 != []:
                output = output + """<p class="inside_box"><b1>4. deklinācija:</b1></p>""" + table_gen.table_gen(dekl_4, keys)
            if dekl_5 != []:
                output = output + """<p class="inside_box"><b1>5. deklinācija:</b1></p>""" + table_gen.table_gen(dekl_5, keys)
            if dekl_6 != []:
                output = output + """<p class="inside_box"><b1>6. deklinācija:</b1></p>""" + table_gen.table_gen(dekl_6, keys)
            if no_dekl != []:
                output = output + """<p class="inside_box"><b1>Deklinācija nepiemīt:</b1></p>""" + table_gen.table_gen(no_dekl, keys)
            if dekl != []:
                try:
                    for line in dekl:
                        output = output + """<p class="inside_box"><b1>""" + line['Deklinācija'] + """:</b1></p>""" + table_gen.table_gen(dekl, keys)
                        break
                except Exception as inst:
                    output = output + """<div class="inside_box">""" + table_gen.table_gen(dekl, ["Vārdšķira"]) + "</div>"
        except Exception as inst:
            pass
    except Exception as inst:
        pass

    return output
