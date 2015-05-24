# -*- coding: utf-8 -*-
import json
import codecs

def unrecognized(input_data):
    output = ''
    try:
        with codecs.open('neatpazītās_vārdšķiras.json', encoding='utf-8') as f:
            # transfer json elements to python elements
            document = json.load(f)
    except Exception as inst:
        document = []

    unrecognized_parts = []
    try:
        for vardskira in document:
            unrecognized_parts.append(vardskira)
    except Exception as inst:
        pass
    try:
        for line in input_data:
            key_is_used = 0
            for vardskira in unrecognized_parts:
                if line[u'Vārdšķira'] == vardskira[u'Vārdšķira']:
                    key_is_used = 1
                    break
            if key_is_used == 0:
                unrecognized_parts.append(line)
    except Exception as inst:
        pass
    
    fout = codecs.open('neatpazītās_vārdšķiras.json', 'w', encoding='utf-8')

    output = output + u"["
    for line in unrecognized_parts:
        output = output + u'{"Vārds":"' + line[u'Vārds'] + u'","Vārdšķira":"' + line[u'Vārdšķira'] + u'"},\n'
    output = output + u"]"
    fout.write(output.replace(",\n]", "]"))

    fout.close()
