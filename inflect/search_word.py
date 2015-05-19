# -*- coding: utf-8 -*-
from inflect import speach_service
from inflect import get_from_page

def search_word(input_data, word):
    # Function that puts all searched words in to array (isn't case sensitive)
    speach_id = speach_service.get_id(word)
    output = []
    
    try:
        for i in input_data:
            try:
                if i['Lemma'].upper() == word.upper():
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
            if i['Lemma'] == word:
                return {'content':word, 'automatic_output_data':get_from_page.inflect_word(word, speach_id, False, False)}
        except Exception as inst:
            pass

    return {'content':word, 'automatic_output_data':get_from_page.inflect_word(word, speach_id)}
                
