from website import grammer
from website import phrases

# Function for outputing senses
def sense(input_data):
    output = []
    try:
        if input_data['SenseID']:
            output.append(input_data['SenseID'] + ". nozīme")
    except Exception as inst:
        pass
        
    try:
        if input_data['Gram']:
            grammer.grammer(input_data['Gram'])
    except Exception as inst:
        pass
        
    try:
        if input_data['Gloss']:
            output.append("Skaidrojums " + input_data['Gloss'])
    except Exception as inst:
        pass
        
    try:
        for p in input_data['Examples']['Phrase']:
            phrases.phrase(p)
    except Exception as inst:
        pass
            
    try:
        if input_data['Senses']:
            sense(input_data['Senses'])
    except Exception as inst:
        pass
    return output
