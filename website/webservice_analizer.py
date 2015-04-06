def noun_analizer(input_data):
    output = ""
    try:
        output = output + """<div class="inflect"><table id="auto_table"><tr><td><b1>Locījums</b1></td><td><b1>Viensk.</b1></td><td><b1>Daudzsk.</b1></td></tr><tr><td><b1>Nominatīvs</b1></td><td id="loc_tab">"""
        for line in input_data:
            try:
                if line['Locījums'] == "Nominatīvs":
                    if line['Skaitlis'] == "Vienskaitlis":
                        output = output + line['Vārds'] + "; "
            except Exception as inst:
                pass
        output = output + """</td><td id="loc_tab">"""
        for line in input_data:
            try:
                if line['Locījums'] == "Nominatīvs":
                    if line['Skaitlis'] == "Daudzskaitlis":
                        output = output + line['Vārds'] + "; "
            except Exception as inst:
                pass
        output = output + """</td></tr><tr><td><b1>Ģenitīvs</b1></td><td id="loc_tab">"""
        for line in input_data:
            try:
                if line['Locījums'] == "Ģenitīvs":
                    if line['Skaitlis'] == "Vienskaitlis":
                        output = output + line['Vārds'] + "; "
            except Exception as inst:
                pass
        output = output + """</td><td id="loc_tab">"""
        for line in input_data:
            try:
                if line['Locījums'] == "Ģenitīvs":
                    if line['Skaitlis'] == "Daudzskaitlis":
                        output = output + line['Vārds'] + "; "
            except Exception as inst:
                pass
        output = output + """</td></tr><tr><td><b1>Datīvs</b1></td><td id="loc_tab">"""
        for line in input_data:
            try:
                if line['Locījums'] == "Datīvs":
                    if line['Skaitlis'] == "Vienskaitlis":
                        output = output + line['Vārds'] + "; "
            except Exception as inst:
                pass
        output = output + """</td><td id="loc_tab">"""
        for line in input_data:
            try:
                if line['Locījums'] == "Datīvs":
                    if line['Skaitlis'] == "Daudzskaitlis":
                        output = output + line['Vārds'] + "; "
            except Exception as inst:
                pass
        output = output + """</td></tr><tr><td><b1>Akuzatīvs</b1></td><td id="loc_tab">"""
        for line in input_data:
            try:
                if line['Locījums'] == "Akuzatīvs":
                    if line['Skaitlis'] == "Vienskaitlis":
                        output = output + line['Vārds'] + "; "
            except Exception as inst:
                pass
        output = output + """</td><td id="loc_tab">"""
        for line in input_data:
            try:
                if line['Locījums'] == "Akuzatīvs":
                    if line['Skaitlis'] == "Daudzskaitlis":
                        output = output + line['Vārds'] + "; "
            except Exception as inst:
                pass
        output = output + """</td></tr><tr><td><b1>Lokatīvs</b1></td><td id="loc_tab">"""
        for line in input_data:
            try:
                if line['Locījums'] == "Lokatīvs":
                    if line['Skaitlis'] == "Vienskaitlis":
                        output = output + line['Vārds'] + "; "
            except Exception as inst:
                pass
        output = output + """</td><td id="loc_tab">"""
        for line in input_data:
            try:
                if line['Locījums'] == "Lokatīvs":
                    if line['Skaitlis'] == "Daudzskaitlis":
                        output = output + line['Vārds'] + "; "
            except Exception as inst:
                pass
        output = output + """</td></tr><tr><td><b1>Vokatīvs</b1></td><td id="loc_tab">"""
        for line in input_data:
            try:
                if line['Locījums'] == "Vokatīvs":
                    if line['Skaitlis'] == "Vienskaitlis":
                        output = output + line['Vārds'] + "; "
            except Exception as inst:
                pass
        output = output + """</td><td id="loc_tab">"""
        for line in input_data:
            try:
                if line['Locījums'] == "Vokatīvs":
                    if line['Skaitlis'] == "Daudzskaitlis":
                        output = output + line['Vārds'] + "; "
            except Exception as inst:
                pass
        output = output + """</td></tr></table></div>"""
    except Exception as inst:
        pass
    return output

def adverb_analizer(input_data):
    output = ""
    pamata_v = []
    paraka_v = []
    visparaka_v = []
    pamata_s = []
    paraka_s = []
    visparaka_s = []
    try:
        for line in input_data:
            if line['Pakāpe'] == "Pamata":
                if line['Dzimte'] == "Vīriešu":
                    pamata_v.append(line)
                if line['Dzimte'] == "Sieviešu":
                    pamata_s.append(line)
            if line['Pakāpe'] == "Pārākā":
                if line['Dzimte'] == "Vīriešu":
                    paraka_v.append(line)
                if line['Dzimte'] == "Sieviešu":
                    paraka_s.append(line)
            if line['Pakāpe'] == "Vispārākā":
                if line['Dzimte'] == "Vīriešu":
                    visparaka_v.append(line)
                if line['Dzimte'] == "Sieviešu":
                    visparaka_s.append(line)
    except Exception as inst:
        pass
    try:
        output = output + """<h3>Vīriešu dzimte, pamata pakāpe</h3>""" + noun_analizer(pamata_v)
    except Exception as inst:
        pass
    try:
        output = output + """<h3>Vīriešu dzimte, pārākā pakāpe</h3>""" + noun_analizer(paraka_v)
    except Exception as inst:
        pass
    try:
        output = output + """<h3>Vīriešu dzimte, vispārākā pakāpe</h3>""" + noun_analizer(visparaka_v)
    except Exception as inst:
        pass
    try:
        output = output + """<h3>Sieviesu dzimte, pamata pakāpe</h3>""" + noun_analizer(pamata_s)
    except Exception as inst:
        pass
    try:
        output = output + """<h3>Sieviesu dzimte, pārākā pakāpe</h3>""" + noun_analizer(paraka_s)
    except Exception as inst:
        pass
    try:
        output = output + """<h3>Sieviesu dzimte, vispārākā pakāpe</h3>""" + noun_analizer(visparaka_s)
    except Exception as inst:
        pass
    return output
