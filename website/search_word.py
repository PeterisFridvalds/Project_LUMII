def search_word(input_data, word):
    output = []
    try:
        for i in input_data:
            if i['Header']['Lemma'].upper() == word.upper():
                output.append(i)
    except Exception as inst:
        pass
    return output
