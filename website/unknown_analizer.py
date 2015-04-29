#Fjunkcija, kas izvada visus atslēgvārdus, kuri nav menēti tai padotajā sarakstā, kā ari to vērtības
def unknown_analizer(input_data, keys = ["Vārdšķira"]):
    output = ""
    key_is_used = 0
    counting_keys = 0
    try:
        for line in input_data:
            #Saskaita, cik atslēg vārdi jāizvada
            counting_keys = 0
            try:
                for key in line:
                    if key != "Vārds":
                        key_is_used = 0
                        for used_key in keys:
                            if key == used_key:
                                key_is_used = 1
                                break
                        if key_is_used == 0:
                            counting_keys = counting_keys + 1
            except Exception as inst:
                pass

            #Ja izvadāmo atslēgvārdu skaits ir 0, tad izvada tikai vārdu
            if counting_keys == 0:
                output = output + """<p style="max-width: 500px"><b1>""" + line['Vārds'] + """</b1></p>"""
            #Ja izvadāmo atslēgvārdu skaits lielāks 0, tad izvada tikai vārdu un aiz tā uzskaita tam atbilstošos atslēgvārdus un to vērtības
            elif counting_keys > 0:
                output = output + """<p style="max-width: 500px"><b1>""" + line['Vārds'] + """: </b1></p>"""
                for key in line:
                    if key != "Vārds":
                        key_is_used = 0
                        for used_key in keys:
                            if key == used_key:
                                key_is_used = 1
                                break
                        if key_is_used == 0:
                            output = output + """<p class="inside_box">""" + key + ": " + line[key].lower() + ";</p>"
                output = output + "<br>"
    except Exception as inst:
        pass
    return output
