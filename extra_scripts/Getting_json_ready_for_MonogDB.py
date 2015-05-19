import json

def LabotAltLemmas(input_line):
    altlemmas = []
    try:
        if input_line['Header']['Gram']['AltLemmas']:
            for parad in input_line['Header']['Gram']['AltLemmas']:
                for lem in input_line['Header']['Gram']['AltLemmas'][parad]:
                    altlem = {}
                    try:
                        altlem['Lemma'] = lem['Lemma']
                    except Exception as inst:
                        pass
                    try:
                        altlem['Paradigm'] = []
                        altlem['Paradigm'].append(parad)
                    except Exception as inst:
                        pass
                    try:
                        altlem['Flags'] = lem['Flags']
                    except Exception as inst:
                        pass
                    altlemmas.append(altlem)
    except Exception as inst:
        pass
    gram = {}
    try:
        gram['Paradigm'] = input_line['Header']['Gram']['Paradigm']
    except Exception as inst:
        pass
    try:
        gram['AltLemmas'] = altlemmas
    except Exception as inst:
        pass
    try:
        gram['Flags'] = input_line['Header']['Gram']['Flags']
    except Exception as inst:
        pass
    try:
        gram['Leftovers'] = input_line['Header']['Gram']['Leftovers']
    except Exception as inst:
        pass
    try:
        gram['Original'] = input_line['Header']['Gram']['Original']
    except Exception as inst:
        pass
    header = {}
    try:
        header['Lemma'] = input_line['Header']['Lemma']
    except Exception as inst:
        pass
    try:
        header['Pronunciation'] = input_line['Header']['Pronunciation']
    except Exception as inst:
        pass
    try:
        header['Gram'] = gram
    except Exception as inst:
        pass
    line = {}
    try:
        line['Header'] = header
    except Exception as inst:
        pass
    try:
        if input_line['ID']:
            line['ID'] = input_line['ID']
    except Exception as inst:
        pass
    try:
        if input_line['Senses']:
            line['Senses'] = input_line['Senses']
    except Exception as inst:
        pass
    try:
        if input_line['Phrases']:
            line['Phrases'] = input_line['Phrases']
    except Exception as inst:
        pass
    try:
        if input_line['Derivatives']:
            line['Derivatives'] = input_line['Derivatives']
    except Exception as inst:
        pass
    try:
        if input_line['Sources']:
            line['Sources'] = input_line['Sources']
    except Exception as inst:
        pass
    return line

# Nolasa failu un pārveido uz python formātu
with open('tezaurs-full.json', encoding='utf-8') as f:
    document = json.load(f)
output = []
for line in document:
    try:
        if line['Header']['Gram']['AltLemmas']:
            output.append(LabotAltLemmas(line))
    except Exception as inst:
        output.append(line)

line_one = True
with open('tezaurs-full-for-MongoDB.json', 'w', encoding='utf-8') as f:
    f.write('[\n')
    for line in output:
        if line_one == False:
            f.write(',\n')
        data = json.dumps(line, ensure_ascii=False)
        line_one = False
        f.write(data)
    f.write('\n]')


