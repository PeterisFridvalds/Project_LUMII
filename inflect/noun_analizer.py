# -*- coding: utf-8 -*-
from inflect import table_gen

##Funkcija, kas analizē lietvārdus
def noun_analizer(input_data, keys = [u"Vārdšķira"]):
    output = ''
    dekl_1 = []
    dekl_2 = []
    dekl_3 = []
    dekl_4 = []
    dekl_5 = []
    dekl_6 = []
    no_dekl = []
    dekl = []
    keys.append(u'Deklinācija')
    try:
        #Ieadala iedotos datus pēc deklinācijām
        for line in input_data:
            try:
                if line[u'Deklinācija'] == u"1":
                    dekl_1.append(line)
                elif line[u'Deklinācija'] == u"2":
                    dekl_2.append(line)
                elif line[u'Deklinācija'] == u"3":
                    dekl_3.append(line)
                elif line[u'Deklinācija'] == u"4":
                    dekl_4.append(line)
                elif line[u'Deklinācija'] == u"5":
                    dekl_5.append(line)
                elif line[u'Deklinācija'] == u"6":
                    dekl_6.append(line)
                elif line[u'Deklinācija'] == u"0":
                    no_dekl.append(line)
                elif line[u'Deklinācija'] == u"Nepiemīt":
                    no_dekl.append(line)
                else:
                    dekl.append(line)
            except Exception as inst:
                dekl.append(line)
                
        #Pārbauda, vai ir kaut kādi dati, kas atiecas uz attiecīgo deklināciju, ja tādi ir, izsauc f-ju, kas izveido HTML kodu locījumiem
        output = output + u'<ul class="table_layout">'
        try:
            if dekl_1 != []:
                output = output + u'<li><p class="inside_box"><b1>1. deklinācija:</b1></p>' + table_gen.table_gen(dekl_1, keys) + u'</li>'
            if dekl_2 != []:
                output = output + u'<li><p class="inside_box"><b1>2. deklinācija:</b1></p>' + table_gen.table_gen(dekl_2, keys) + u'</li>'
            if dekl_3 != []:
                output = output + u'<li><p class="inside_box"><b1>3. deklinācija:</b1></p>' + table_gen.table_gen(dekl_3, keys) + u'</li>'
            if dekl_4 != []:
                output = output + u'<li><p class="inside_box"><b1>4. deklinācija:</b1></p>' + table_gen.table_gen(dekl_4, keys) + u'</li>'
            if dekl_5 != []:
                output = output + u'<li><p class="inside_box"><b1>5. deklinācija:</b1></p>' + table_gen.table_gen(dekl_5, keys) + u'</li>'
            if dekl_6 != []:
                output = output + u'<li><p class="inside_box"><b1>6. deklinācija:</b1></p>' + table_gen.table_gen(dekl_6, keys) + u'</li>'
            if no_dekl != []:
                output = output + u'<li><p class="inside_box"><b1>Deklinācija nepiemīt:</b1></p>' + table_gen.table_gen(no_dekl, keys) + u'</li>'
            if dekl != []:
                try:
                    for line in dekl:
                        output = output + u'<li><p class="inside_box"><b1>' + line[u'Deklinācija'] + u':</b1></p>' + table_gen.table_gen(dekl, keys) + u'</li>'
                        break
                except Exception as inst:
                    output = output + u'<li><p class="inside_box"><b1>Deklinācija nav norādīta:</b1></p>' + table_gen.table_gen(dekl, ["Vārdšķira"]) + u'</li>'
        except Exception as inst:
            pass
        output = output + u'</ul>'
    except Exception as inst:
        pass

    return output
