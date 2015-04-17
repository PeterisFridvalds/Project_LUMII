from website import unknown_analizer

def punctuation_mark_analizer(input_data):
    output = ""
    try:
        output = output + unknown_analizer.unknown_analizer(input_data)
    except Exception as inst:
        pass
    return output
