from website import table_gen_sk

def noun_analizer(input_data):
    output = ""
    dekl_1 = []
    dekl_2 = []
    dekl_3 = []
    dekl_4 = []
    dekl_5 = []
    dekl_6 = []
    no_dekl = []
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
                else:
                    no_dekl.append(line)
            except Exception as inst:
                pass
        #pārbauda, vai ir kaut kādi dati, kas atiecas uz attiecīgo deklināciju, ja tādi ir, izsauc f-ju, kas izveido HTML kodu locījumiem
        try:
            if dekl_1 != []:
                output = output + """<p class="inside_box"><b1>1. deklinācija:</b1></p>""" + table_gen_sk.table_gen_sk(dekl_1)
            if dekl_2 != []:
                output = output + """<p class="inside_box"><b1>2. deklinācija:</b1></p>""" + table_gen_sk.table_gen_sk(dekl_2)
            if dekl_3 != []:
                output = output + """<p class="inside_box"><b1>3. deklinācija:</b1></p>""" + table_gen_sk.table_gen_sk(dekl_3)
            if dekl_4 != []:
                output = output + """<p class="inside_box"><b1>4. deklinācija:</b1></p>""" + table_gen_sk.table_gen_sk(dekl_4)
            if dekl_5 != []:
                output = output + """<p class="inside_box"><b1>5. deklinācija:</b1></p>""" + table_gen_sk.table_gen_sk(dekl_5)
            if dekl_6 != []:
                output = output + """<p class="inside_box"><b1>6. deklinācija:</b1></p>""" + table_gen_sk.table_gen_sk(dekl_6)
            if no_dekl != []:
                output = output + """<p class="inside_box"><b1>Deklinācija nepiemīt:</b1></p>""" + table_gen_sk.table_gen_sk(no_dekl)
        except Exception as inst:
            pass
    except Exception as inst:
        pass

    return output
