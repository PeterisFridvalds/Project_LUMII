# Function for outputing grammer
def grammer(input_data):
    output = []
    try:
        for p in input_data['Paradigm']:
            output.append("Pradigma " + p)
    except Exception as inst:
        pass
        
    try:
        for f in input_data['Flags']:
            output.append("Karodziņi " + f)
    except Exception as inst:
        try:
            if input_data['Original']:
                output.append(input_data['Original'])
        except Exception as inst:
            pass
        
    try:
        for l in input_data['Leftowers']:
            output.append(l)
    except Exception as inst:
        pass
    return output
