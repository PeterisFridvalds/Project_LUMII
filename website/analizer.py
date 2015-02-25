from website import grammer
from website import senses
from website import phrases

# Function for outputing all data about input word
def analizer(input_data):
    output = []
    try:
        if i['Header']['Gram']:
            output.append(grammer.grammer(i['Header']['Gram']))
    except Exception as inst:
          pass
    try:
        if input_data['ID']:
            output.append("ID " + i['ID'])
    except Exception as inst:
        pass
    try:
        for s in i['Senses']:
            out = senses.sense(s)
            output.append(out)
    except Exception as inst:
        pass
    try:
        for p in i['Phrases']['Phrase']:
            output.append(phrases.phrase(p))
    except Exception as inst:
        pass
    try:
        for source in input_data['Sources']:
            output.append("Avoti " + source)
    except Exception as inst:
        pass
    return output

