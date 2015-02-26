from website import analizer
def search_word(input_data, word):
    # Function that puts all searched words in to array (is't case sensitive)
    output = []
    try:
        for i in input_data:
            if i['Header']['Lemma'].upper() == word.upper():
                output.append(i)
    except Exception as inst:
        pass
    return output

def return_centext_dict(input_data, word):
    # No input_data means that no word was found
    if input_data == []:
        return {'content':word, 'data':"No such word"}
    # Loop for finding if some word is exactly the same as input word
    for i in input_data:
        if i['Header']['Lemma'] == word:
            return {'content':word, 'data':input_data, 'output_data':analizer.analizer(i)}
    # If function breaks first loop, then put the first word as input word
    for i in input_data:
        return {'content':i['Header']['Lemma'], 'data':input_data, 'output_data':analizer.analizer(i)}
