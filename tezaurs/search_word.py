# -*- coding: utf-8 -*-
from pymongo import Connection
from inflect import speach_service
from tezaurs import analizer
from inflect import get_from_page
import re

## Funkcija vārda meklēšanai datu bāzē
def search_word(word, word_ID):
    ## Pieprasa vārda izrunas sintēzes servisam identifikatoru
    speach_id = speach_service.get_id(word)
    lemmas = []
    altlemmas = []
    derivatives = []
    output = []
    word_list = []
    name_found = False

    ## Pieslēdzas datu bāzes kolekcijai
    db_name = "tezaurs_db"
    connection = Connection()
    db = connection[db_name]
    tezaur_table = db['tezaur_data']

    ## Mēģina atras vārus, kuri sadtus burku kombināciju, kas glabājas mainīgajā "word" (neņem vērā lielos mazos burtus)
    try:
        lemmas = tezaur_table.find({"Header.Lemma": re.compile(re.escape(word), re.IGNORECASE)})
        altlemmas = tezaur_table.find({"Header.Gram.AltLemmas.Lemma": re.compile(re.escape(word), re.IGNORECASE)})
        derivatives = tezaur_table.find({"Derivatives.Header.Lemma": re.compile(re.escape(word), re.IGNORECASE)})
    except Exception as inst:
        pass
    ## Sakārto informāciju par šiem vērdiem
    for i in lemmas:
        element = {u'Lemma':i[u'Header'][u'Lemma'], u'ID':i[u'ID'], u'from':u'Lemmas'}
        word_list.append(element)
    for i in altlemmas:
        for lem in i[u'Header'][u'Gram'][u'AltLemmas']:
            element = {u'Lemma':lem[u'Lemma'], u'ID':i[u'ID'], u'from':u'AltLemmas'}
            word_list.append(element)
    for i in derivatives:
        for der in i[u'Derivatives']:
            element = {u'Lemma':der[u'Header'][u'Lemma'], u'ID':i[u'ID'], u'from':u'Derivatives'}
            word_list.append(element)

    ## Meklē vārdu, krua rakstība precīi sarīt ar "word" un sakrīt ari homonīma identifikators
    for w in word_list:
        if w[u'Lemma'] == word:
            try:
                if w[u'ID'] == word_ID:
                    name_found = True
                    if w[u'from'] == u'Lemmas':
                        output = {u'data':tezaur_table.find({"Header.Lemma": word, "ID":word_ID}), u'from':u'Lemmas'}
                    elif w[u'from'] == u'AltLemmas':
                        output = {u'data':tezaur_table.find({"Header.Gram.AltLemmas.Lemma": word, "ID":word_ID}), u'from':u'AltLemmas'}
                    elif w[u'from'] == u'Derivatives':
                        output = {u'data':tezaur_table.find({"Derivatives.Header.Lemma": word, "ID":word_ID}), u'from':u'Derivatives'}
            except Exception as inst:
                pass
    if name_found == False:
        for w in word_list:
            if w[u'Lemma'] == word:
                output = {u'data':tezaur_table.find({"Header.Lemma":word}), u'from':u'Lemmas'}
            elif w[u'from'] == u'AltLemmas':
                output = {u'data':tezaur_table.find({"Header.Gram.AltLemmas.Lemma": word}), u'from':u'AltLemmas'}
            elif w[u'from'] == u'Derivatives':
                output = {u'data':tezaur_table.find({"Derivatives.Header.Lemma": word}), u'from':u'Derivatives'}
    if name_found == False:
        for w in word_list:
            output = {u'data':tezaur_table.find({"Header.Lemma":w[u'Lemma']}), u'from':u'Lemmas'}
            break
        
    return {'output':output, 'word_list':word_list, 'speach_id':speach_id}

## Funkcija izvadamo mainīgo sagatavošanai
def return_centext_dict(input_data, word, homonim_id, speach_id, word_list, not_for_infl):
    ## Ja "input_data" ir tukšs masīvs, vārds netika atrasts
    if input_data == []:
        return {'content':word, 'content_ID':u'-1', 'data':u"No such word", 'output_data':u"<p>Vārds netika atrasts</p>", 'automatic_output_data':get_from_page.inflect_word(word, speach_id)}

    ## Analizē atrasto informāciju par škirkli (pirmais, pārbauda, vai homonīma identifikatri sakrīt)
    if input_data[u'from'] == u'Lemmas':
        for i in input_data[u'data']:
            for not_infl in not_for_infl:
                try:
                    if not_infl[u'Lemma'] == word:
                        return {'content':word, 'content_ID':homonim_id, 'data':input_data, 'word_list':word_list, 'output_data':analizer.analizer(i), 'automatic_output_data':get_from_page.inflect_word(word, speach_id, False, False)}
                except Exception as inst:
                    pass
            return {'content':word, 'content_ID':homonim_id, 'data':input_data, 'word_list':word_list, 'output_data':analizer.analizer(i), 'automatic_output_data':get_from_page.inflect_word(word, speach_id)}
    elif input_data[u'from'] == u'AltLemmas':
        for i in input_data[u'data']:
            for not_infl in not_for_infl:
                try:
                    if not_infl[u'Lemma'] == word:
                        return {'content':word, 'content_ID':homonim_id, 'data':input_data, 'word_list':word_list, 'output_data':analizer.AltLemmas(i, word), 'automatic_output_data':get_from_page.inflect_word(word, speach_id, False, False)}
                except Exception as inst:
                    pass
            return {'content':word, 'data':input_data, 'word_list':word_list, 'output_data':analizer.AltLemmas(i, word), 'automatic_output_data':get_from_page.inflect_word(word, speach_id)}
    elif input_data[u'from'] == u'Derivatives':
        for i in input_data[u'data']:
            for not_infl in not_for_infl:
                try:
                    if not_infl[u'Lemma'] == word:
                        return {'content':word, 'content_ID':homonim_id, 'data':input_data, 'word_list':word_list, 'output_data':analizer.Derivatives(i, word), 'automatic_output_data':get_from_page.inflect_word(word, speach_id, False, False)}
                except Exception as inst:
                    pass
            return {'content':word, 'data':input_data, 'word_list':word_list, 'output_data':analizer.Derivatives(i, word), 'automatic_output_data':get_from_page.inflect_word(word, speach_id)}
    for i in input_data[u'data']:
        return {'content':word, 'content_ID':homonim_id, 'data':input_data, 'word_list':word_list, 'output_data':analizer.analizer(i), 'automatic_output_data':get_from_page.inflect_word(word, speach_id)}
