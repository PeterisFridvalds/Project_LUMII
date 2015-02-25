import string

def search_word(input_data, word):
    try:
        for i in input_data:
            if i['Header']['Lemma'].upper() == word.upper():
                return i
    except Exception as inst:
        return "no data"
