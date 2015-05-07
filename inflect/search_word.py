from website import speach_service
from inflect import get_from_page

def search_word(input_data, word):
    # Function that puts all searched words in to array (isn't case sensitive)
    speach_id = speach_service.get_id(word)
    if speach_id == '-1':
        speach_id = '-999'
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
    return {'output':output, 'speach_id':speach_id}

def return_centext_dict(input_data, word, speach_id):
    # No input_data means that no word was found
    if input_data == []:
        return {'content':word, 'automatic_output_data':get_from_page.inflect_word(word, speach_id)}
    
    # Looking for flags, wich don't need to infelct
    for i in input_data:
        try:
            if i['Header']['Lemma'] == word:
                for flag in i['Header']['Gram']['Flags']:
                    try:
                        if flag == 'Saīsinājums':
                            return {'content':word, 'automatic_output_data':get_from_page.inflect_word(word, speach_id, False, False)}
                        if flag == 'Vārds svešvalodā':
                            return {'content':word, 'automatic_output_data':get_from_page.inflect_word(word, speach_id, False, False)}
                    except Exception as inst:
                        pass
        except Exception as inst:
            pass
        try:
            for p in i['Header']['Gram']['AltLemmas']:
                for k in i['Header']['Gram']['AltLemmas'][p]:
                    if k['Lemma'].upper() == word.upper():
                        for flag in k['Flags']:
                            try:
                                if flag == 'Saīsinājums':
                                    return {'content':word, 'automatic_output_data':get_from_page.inflect_word(word, speach_id, False, False)}
                                if flag == 'Vārds svešvalodā':
                                    return {'content':word, 'automatic_output_data':get_from_page.inflect_word(word, speach_id, False, False)}
                            except Exception as inst:
                                pass
        except Exception as inst:
            pass
        try:
            for d in i['Derivatives']:
                if d['Header']['Lemma'].upper() == word.upper():
                    for flag in d['Header']['Gram']['Flags']:
                        try:
                            if flag == 'Saīsinājums':
                                return {'content':word, 'automatic_output_data':get_from_page.inflect_word(word, speach_id, False, False)}
                            if flag == 'Vārds svešvalodā':
                                return {'content':word, 'automatic_output_data':get_from_page.inflect_word(word, speach_id, False, False)}
                        except Exception as inst:
                            pass
        except Exception as inst:
            pass

    return {'content':word, 'automatic_output_data':get_from_page.inflect_word(word, speach_id)}
                
