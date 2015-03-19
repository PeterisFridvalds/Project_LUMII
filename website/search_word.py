from website import analizer

def search_word(input_data, word):
    # Function that puts all searched words in to array (isn't case sensitive)
    output = []
    try:
        for i in input_data:
            # Looking for words, wich has the same speling, between main Lemmas, ignoring upper and lower letters
            try:
                if i['Header']['Lemma'].upper() == word.upper():
                    output.append(i)
            except Exception as inst:
                pass
            # Looking for words, wich has the same speling, between AltLemmas, ignoring upper and lower letters
            try:
                for p in i['Header']['Gram']['AltLemmas']:
                    for k in i['Header']['Gram']['AltLemmas'][p]:
                        if k['Lemma'].upper() == word.upper():
                            output.append(i)       
            except Exception as inst:
                pass
            # Looking for words, wich has the same speling, between Derivatives, ignoring upper and lower letters
            try:
                for d in i['Derivatives']:
                    if d['Header']['Lemma'].upper() == word.upper():
                        output.append(i)
            except Exception as inst:
                pass
    except Exception as inst:
        pass
    return output

def return_centext_dict(input_data, word, homonim_id):
    # No input_data means that no word was found
    if input_data == []:
        return {'content':word, 'data':"No such word"}
    # Loop for finding if some word is exactly the same as input word
    for i in input_data:
        try:
            if i['Header']['Lemma'] == word:
##                return {'content':word, 'data':input_data, 'output_data':analizer.analizer(i)}
                if homonim_id == "0":
                    return {'content':word, 'data':input_data, 'output_data':analizer.analizer(i)}
                if homonim_id == i['ID']:
                    return {'content':word, 'data':input_data, 'output_data':analizer.analizer(i)}
        except Exception as inst:
            pass
        # Looking for words, wich has the same speling, between AltLemmas, ignoring upper and lower letters
        try:
            for p in i['Header']['Gram']['AltLemmas']:
                for k in i['Header']['Gram']['AltLemmas'][p]:
                    if k['Lemma'].upper() == word.upper():
                        return {'content':word, 'data':input_data, 'output_data':analizer.AltLemmas(k, i)}            
        except Exception as inst:
            pass
        # Looking for words, wich has the same speling, between Derivatives, ignoring upper and lower letters
        try:
            for d in i['Derivatives']:
                if d['Header']['Lemma'].upper() == word.upper():
                    return {'content':word, 'data':input_data, 'output_data':analizer.Derivatives(d, i)}
        except Exception as inst:
            pass
    # If function breaks the loop, then put the first word as input word
    for i in input_data:
        return {'content':i['Header']['Lemma'], 'data':input_data, 'output_data':analizer.analizer(i)}
