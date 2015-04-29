import json

def unrecognized(input_data):
    output = ""
    with open('neatpazītās_vārdšķiras.json', encoding='utf-8') as f:
        # transfer json elements to python elements
        document = json.load(f)

    unrecognized_parts = []
    for vardskira in document:
        unrecognized_parts.append(vardskira)
    try:
        for line in input_data:
            key_is_used = 0
            for vardskira in unrecognized_parts:
                if line['Vārdšķira'] == vardskira['Vārdšķira']:
                    key_is_used = 1
                    break
            if key_is_used == 0:
                unrecognized_parts.append(line)
    except Exception as inst:
        pass
    
    fout = open('neatpazītās_vārdšķiras.json', 'w', encoding='utf-8')

    output = output + "["
    for line in unrecognized_parts:
        output = output + '{"Vārds":"' + line['Vārds'] + '","Vārdšķira":"' + line['Vārdšķira'] + '"},\n'
    output = output + "]"
    fout.write(output.replace(",\n]", "]"))

    fout.close()
