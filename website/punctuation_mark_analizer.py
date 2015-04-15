def punctuation_mark_analizer(input_data):
    output = ""
    for line in input_data:
        try:
            output = output + """<p style="max-width: 500px"><b1>" """ + line['Vārds'] + """ ": </b1>"""
            for key in line:
                if key != "Vārds":
                    output = output + key + " - " + line[key] + "; "
            output = output + """</p>"""
        except Exception as inst:
            pass
    return output
