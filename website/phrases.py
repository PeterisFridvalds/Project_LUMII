from website import grammer
# from website import senses

# Function for outputing phrases
def phrase(input_data):
    output = []
    try:
        if input_data['Text']:
            output.append(input_data['Text'])
    except Exception as inst:
        pass

    try:
        if input_data['Gram']:
            grammer.grammer(input_data['Gram'])
    except Exception as inst:
        pass

    try:
        if input_data['Senses']:
            senses.sense(input_data['Senses'])
    except Exception as inst:
        pass
    return output
