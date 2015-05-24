# -*- coding: utf-8 -*-
from pymongo import Connection
from inflect import speach_service
from tezaurs import analizer
from inflect import get_from_page
import re

def search_word(word, word_ID):
    # Function that puts all searched words in to array (isn't case sensitive)
    speach_id = speach_service.get_id(word)
    lemmas = []
    altlemmas = []
    derivatives = []
    output = []
    word_list = []
    name_found = False

    db_name = "tezaurs_db"
    connection = Connection()
    db = connection[db_name]
    tezaur_table = db['tezaur_data']

    try:
        lemmas = tezaur_table.find({"Header.Lemma": re.compile(re.escape(word), re.IGNORECASE)})
        altlemmas = tezaur_table.find({"Header.Gram.AltLemmas.Lemma": re.compile(re.escape(word), re.IGNORECASE)})
        derivatives = tezaur_table.find({"Derivatives.Header.Lemma": re.compile(re.escape(word), re.IGNORECASE)})
    except Exception as inst:
        pass
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
    for w in word_list:
        if w[u'Lemma'] == word:
            if w[u'ID'] == word_ID:
                name_found = True
                if w[u'from'] == u'Lemmas':
                    output = {u'data':tezaur_table.find({"Header.Lemma": word}), u'from':u'Lemmas'}
                elif w[u'from'] == u'AltLemmas':
                    output = {u'data':tezaur_table.find({"Header.Gram.AltLemmas.Lemma": word}), u'from':u'AltLemmas'}
                elif w[u'from'] == u'Derivatives':
                    output = {u'data':tezaur_table.find({"Derivatives.Header.Lemma": word}), u'from':u'Derivatives'}
    if name_found == False:
        for w in word_list:
            if w[u'Lemma'] == word:
                output = tezaur_table.find({"Header.Lemma":word})
    if output == []:
        for w in word_list:
            output = tezaur_table.find({"Header.Lemma":w[u'Lemma']})
            break
        
    return {'output':output, 'word_list':word_list, 'speach_id':speach_id}

def return_centext_dict(input_data, word, homonim_id, speach_id, word_list):
    # No input_data means that no word was found
    if input_data == []:
        return {'content':word, 'data':"No such word", 'output_data':"<p>Vārds netika atrasts</p>",'automatic_output_data':get_from_page.inflect_word(word, speach_id)}
    # Loop for finding if some word is exactly the same as input word
    if input_data[u'from'] == u'Lemmas':
        for i in input_data[u'data']:
            return {'content':word, 'data':input_data, 'word_list':word_list, 'output_data':analizer.analizer(i), 'automatic_output_data':get_from_page.inflect_word(word, speach_id)}
    elif input_data[u'from'] == u'AltLemmas':
        for i in input_data[u'data']:
            return {'content':word, 'data':input_data, 'word_list':word_list, 'output_data':analizer.AltLemmas(i, word), 'automatic_output_data':get_from_page.inflect_word(word, speach_id)}
    elif input_data[u'from'] == u'Derivatives':
        for i in input_data[u'data']:
            return {'content':word, 'data':input_data, 'word_list':word_list, 'output_data':analizer.Derivatives(i, word), 'automatic_output_data':get_from_page.inflect_word(word, speach_id)}
    else:
        return {'content':word, 'data':"No such word", 'output_data':"<p>Vārds netika atrasts</p>",'automatic_output_data':get_from_page.inflect_word(word, speach_id)}
    
##        return {'content':word, 'data':input_data, 'output_data':analizer.analizer(i), 'automatic_output_data':get_from_page.inflect_word(word, speach_id), 'hom_id':i[u'ID']}
##    AltLemmas_out = []
##    for i in input_data:
##        try:
##            for p in i[u'Header'][u'Gram'][u'AltLemmas']:
##                for k in i[u'Header'][u'Gram'][u'AltLemmas'][p]:
##                    out_lemma = {'lemma':i[u'Header'][u'Lemma'], 'altLemma':k[u'Lemma']}
##                    AltLemmas_out.append(out_lemma)
##        except Exception as inst:
##            pass
##    for i in input_data:
##        try:
##            if i[u'Header'][u'Lemma'] == word:
##                if homonim_id == "0":
##                    for flag in i[u'Header'][u'Gram'][u'Flags']:
##                        try:
##                            if flag == u'Saīsinājums':
##                                return {'content':word, 'data':input_data, 'output_data':analizer.analizer(i), 'AltLemmas_out':AltLemmas_out, 'automatic_output_data':get_from_page.inflect_word(word, speach_id, "neloka", "bad"), 'hom_id':i[u'ID']}
##                            if flag == u'Vārds svešvalodā':
##                                return {'content':word, 'data':input_data, 'output_data':analizer.analizer(i), 'AltLemmas_out':AltLemmas_out, 'automatic_output_data':get_from_page.inflect_word(word, speach_id, "neloka", "bad"), 'hom_id':i[u'ID']}
##                        except Exception as inst:
##                            pass
##                    return {'content':word, 'data':input_data, 'output_data':analizer.analizer(i), 'AltLemmas_out':AltLemmas_out, 'automatic_output_data':get_from_page.inflect_word(word, speach_id), 'hom_id':i[u'ID']}
##                if homonim_id == i[u'ID']:
##                    for flag in i[u'Header'][u'Gram'][u'Flags']:
##                        try:
##                            if flag == u'Saīsinājums':
##                                return {'content':word, 'data':input_data, 'output_data':analizer.analizer(i), 'AltLemmas_out':AltLemmas_out, 'automatic_output_data':get_from_page.inflect_word(word, speach_id, "neloka", "bad"), 'hom_id':i[u'ID']}
##                            if flag == u'Vārds svešvalodā':
##                                return {'content':word, 'data':input_data, 'output_data':analizer.analizer(i), 'AltLemmas_out':AltLemmas_out, 'automatic_output_data':get_from_page.inflect_word(word, speach_id, "neloka", "bad"), 'hom_id':i[u'ID']}
##                        except Exception as inst:
##                            pass
##                    return {'content':word, 'data':input_data, 'output_data':analizer.analizer(i), 'AltLemmas_out':AltLemmas_out, 'automatic_output_data':get_from_page.inflect_word(word), 'hom_id':i[u'ID']}
##        except Exception as inst:
##            pass
##        # Looking for words, wich has the same speling, between AltLemmas, ignoring upper and lower letters
##        try:
##            for k in i[u'Header'][u'Gram'][u'AltLemmas']:
##                if k[u'Lemma'].upper() == word.upper():
##                    if homonim_id == "0":
##                        for flag in k[u'Flags']:
##                            try:
##                                if flag == u'Saīsinājums':
##                                    return {'content':word, 'data':input_data, 'output_data':analizer.AltLemmas(k, i), 'AltLemmas_out':AltLemmas_out, 'automatic_output_data':get_from_page.inflect_word(word, speach_id, "neloka", "bad"), 'hom_id':i[u'ID']}
##                                if flag == u'Vārds svešvalodā':
##                                    return {'content':word, 'data':input_data, 'output_data':analizer.AltLemmas(k, i), 'AltLemmas_out':AltLemmas_out, 'automatic_output_data':get_from_page.inflect_word(word, speach_id, "neloka", "bad"), 'hom_id':i[u'ID']}
##                            except Exception as inst:
##                                pass
##                        return {'content':word, 'data':input_data, 'output_data':analizer.AltLemmas(k, i), 'AltLemmas_out':AltLemmas_out, 'automatic_output_data':get_from_page.inflect_word(word, speach_id), 'hom_id':i[u'ID']}
##                    if homonim_id == i[u'ID']:
##                        for flag in k[u'Flags']:
##                            try:
##                                if flag == u'Saīsinājums':
##                                    return {'content':word, 'data':input_data, 'output_data':analizer.AltLemmas(k, i), 'AltLemmas_out':AltLemmas_out, 'automatic_output_data':get_from_page.inflect_word(word, speach_id, "neloka", "bad"), 'hom_id':i[u'ID']}
##                                if flag == u'Vārds svešvalodā':
##                                    return {'content':word, 'data':input_data, 'output_data':analizer.AltLemmas(k, i), 'AltLemmas_out':AltLemmas_out, 'automatic_output_data':get_from_page.inflect_word(word, speach_id, "neloka", "bad"), 'hom_id':i[u'ID']}
##                            except Exception as inst:
##                                pass
##                        return {'content':word, 'data':input_data, 'output_data':analizer.AltLemmas(k, i), 'AltLemmas_out':AltLemmas_out, 'automatic_output_data':get_from_page.inflect_word(word, speach_id), 'hom_id':i[u'ID']}
##        except Exception as inst:
##            pass
##        # Looking for words, wich has the same speling, between Derivatives, ignoring upper and lower letters
##        try:
##            for d in i[u'Derivatives']:
##                if d[u'Header'][u'Lemma'].upper() == word.upper():
##                    if homonim_id == "0":
##                        for flag in d[u'Header'][u'Gram'][u'Flags']:
##                            try:
##                                if flag == u'Saīsinājums':
##                                    return {'content':word, 'data':input_data, 'output_data':analizer.Derivatives(d, i), 'AltLemmas_out':AltLemmas_out, 'automatic_output_data':get_from_page.inflect_word(word, speach_id, "neloka", "bad"), 'hom_id':i[u'ID']}
##                                if flag == u'Vārds svešvalodā':
##                                    return {'content':word, 'data':input_data, 'output_data':analizer.Derivatives(d, i), 'AltLemmas_out':AltLemmas_out, 'automatic_output_data':get_from_page.inflect_word(word, speach_id, "neloka", "bad"), 'hom_id':i[u'ID']}
##                            except Exception as inst:
##                                pass
##                        return {'content':word, 'data':input_data, 'output_data':analizer.Derivatives(d, i), 'AltLemmas_out':AltLemmas_out, 'automatic_output_data':get_from_page.inflect_word(word, speach_id), 'hom_id':i[u'ID']}
##                    if homonim_id == i[u'ID']:
##                        for flag in d[u'Header'][u'Gram'][u'Flags']:
##                            try:
##                                if flag == u'Saīsinājums':
##                                    return {'content':word, 'data':input_data, 'output_data':analizer.Derivatives(d, i), 'AltLemmas_out':AltLemmas_out, 'automatic_output_data':get_from_page.inflect_word(word, speach_id, "neloka", "bad"), 'hom_id':i[u'ID']}
##                                if flag == u'Vārds svešvalodā':
##                                    return {'content':word, 'data':input_data, 'output_data':analizer.Derivatives(d, i), 'AltLemmas_out':AltLemmas_out, 'automatic_output_data':get_from_page.inflect_word(word, speach_id, "neloka", "bad"), 'hom_id':i[u'ID']}
##                            except Exception as inst:
##                                pass
##                        return {'content':word, 'data':input_data, 'output_data':analizer.Derivatives(d, i), 'AltLemmas_out':AltLemmas_out, 'automatic_output_data':get_from_page.inflect_word(word, speach_id), 'hom_id':i[u'ID']}
##        except Exception as inst:
##            pass
##    # If function breaks the loop, then put the first word as input word
##    for i in input_data:
##        return {'content':i[u'Header'][u'Lemma'], 'data':input_data, 'output_data':analizer.analizer(i), 'AltLemmas_out':AltLemmas_out, 'automatic_output_data':get_from_page.inflect_word(i[u'Header'][u'Lemma'], speach_id), 'hom_id':i[u'ID']}
