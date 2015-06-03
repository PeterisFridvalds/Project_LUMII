# -*- coding: utf-8 -*-
import json
import codecs

## Funkcija, ka pārbauda vai atmiņā ir ielādēta informācija par nelokāmajiem vārdiem, ja nav, tad to ielādē
def document_init():
    try:
        document
    except Exception as inst:
        global document
        document = []
        if document == []:
            # open file and read from it
            try:
                with codecs.open('Paradigmas.json', encoding='utf-8') as f:
                    # transfer json elements to python elements
                    try:
                        document = json.load(f)
                    except Exception as inst:
                        document = []
            except Exception as inst:
                document = []
    return document

## Funkcija, ka pārbauda vai atmiņā ir ielādēta informācija par avotiem, ja nav, tad to ielādē
def sources_init():
    try:
        sources
    except Exception as inst:
        global sources
        sources = []
        if sources == []:
            # open file and read from it
            try:
                with codecs.open('tezaurs-sources.json', encoding='utf-8') as f:
                    # transfer json elements to python elements
                    try:
                        sources = json.load(f)
                    except Exception as inst:
                        sourcest = []
            except Exception as inst:
                sources = []
    return sources

## Funkcija, ka pārbauda vai atmiņā ir ielādēta informācija par arodziņiem, ja nav, tad to ielādē
def flags_init():
    try:
        flag_list
    except Exception as inst:
        global flag_list
        flag_list = []
        if flag_list == []:
            # open file and read from it
            try:
                with codecs.open('tezaurs-flags.json', encoding='utf-8') as f:
                    # transfer json elements to python elements
                    try:
                        flag_list = json.load(f)
                    except Exception as inst:
                        flag_list = []
            except Exception as inst:
                flag_list = []
    return flag_list

## Labojumus ievieto tiem paredzētajos laukos
def correct(old_elem, corrections):
    try:
        if old_elem[u'Header'][u'Gram']:
            try:
                doc = document_init()
                parad = []
                for line in doc:
                    try:
                        key = u'H_G_' + line['ID'] + u'_parad'
                        if corrections[key]:
                            parad.append(line['ID'])
                    except Exception as inst:
                        pass
                old_elem[u'Header'][u'Gram'][u'Paradigm'] = parad
            except Exception as inst:
                pass
            try:
                if old_elem[u'Header'][u'Gram'][u'AltLemmas']:
                    for altLem in old_elem[u'Header'][u'Gram'][u'AltLemmas']:
                        key = altLem[u'Lemma']
                        try:
                            flag_list = flags_init()
                            flags = []
                            for flag in flag_list:
                                try:
                                    key1 = key + flag
                                    if corrections[key1]:
                                        flags.append(flag)
                                except Exception as inst:
                                    pass
                            altLem[u'Flags'] = flags
                        except Exception as inst:
                            pass
                        try:
                            doc = document_init()
                            parad = []
                            for line in doc:
                                try:
                                    key1 = key + '_' + line['ID'] + u'_parad'
                                    if corrections[key1] == key1:
                                        parad.append(line['ID'])
                                except Exception as inst:
                                    pass
                            altLem[u'Paradigm'] = parad
                        except Exception as inst:
                            pass
            except Exception as inst:
                pass
            try:
                flag_list = flags_init()
                flags = []
                for flag in flag_list:
                    try:
                        key1 = u'H_G_' + flag
                        if corrections[key1]:
                            flags.append(flag)
                    except Exception as inst:
                        pass
                    old_elem[u'Header'][u'Gram'][u'Flags'] = flags
            except Exception as inst:
                pass
            try:
                if corrections[u'H_G_L']:
                    leftover = corrections[u'H_G_L'].split('; ')
                    old_elem[u'Header'][u'Gram'][u'Leftovers'] = leftover
            except Exception as inst:
                pass
    except Exception as inst:
        pass
    try:
        if corrections[u'hom_ID']:
            old_elem[u'ID'] = corrections[u'hom_ID']
    except Exception as inst:
        pass
    try:
        if old_elem[u'Senses']:
            for sense in old_elem[u'Senses']:
                key = sense[u'SenseID'] + u'_noz'
                try:
                    if sense['Gram']:
                        try:
                            doc = document_init()
                            parad = []
                            for line in doc:
                                try:
                                    key1 = key + '_' + line['ID'] + u'_parad'
                                    if corrections[key1] == key1:
                                        parad.append(line['ID'])
                                except Exception as inst:
                                    pass
                            sense['Gram'][u'Paradigm'] = parad
                        except Exception as inst:
                            pass
                        try:
                            flag_list = flags_init()
                            flags = []
                            for flag in flag_list:
                                try:
                                    key1 = key + flag
                                    if corrections[key1]:
                                        flags.append(flag)
                                except Exception as inst:
                                    pass
                            sense['Gram'][u'Flags'] = flags
                        except Exception as inst:
                            pass
                        try:
                            key1 = key + u'_L'
                            if corrections[key1]:
                                leftover = corrections[key1].split('; ')
                                sense[u'Gram'][u'Leftovers'] = leftover
                        except Exception as inst:
                            pass
                except Exception as inst:
                    pass
                try:
                    if corrections[key]:
                        sense[u'Gloss'] = corrections[key]
                except Exception as inst:
                    pass
    except Exception as inst:
        pass
    try:
        if old_elem[u'Derivatives']:
            for d in old_elem[u'Derivatives']:
                key = d[u'Header'][u'Lemma']
                try:
                    if d[u'Header']['Gram']:
                        try:
                            flag_list = flags_init()
                            flags = []
                            for flag in flag_list:
                                try:
                                    key1 = key + flag
                                    if corrections[key1]:
                                        flags.append(flag)
                                except Exception as inst:
                                    pass
                            d[u'Header']['Gram'][u'Flags'] = flags
                        except Exception as inst:
                            pass
                        try:
                            doc = document_init()
                            parad = []
                            for line in doc:
                                try:
                                    key1 = key + '_' + line['ID'] + u'_parad'
                                    if corrections[key1] == key1:
                                        parad.append(line['ID'])
                                except Exception as inst:
                                    pass
                            d[u'Header']['Gram'][u'Paradigm'] = parad
                        except Exception as inst:
                            pass
                        try:
                            key1 = key + u'_L'
                            if corrections[key1]:
                                leftover = corrections[key1].split('; ')
                                sense[u'Gram'][u'Leftovers'] = leftover
                        except Exception as inst:
                            pass
                except Exception as inst:
                    pass
    except Exception as inst:
        pass
    try:
        sources = sources_init()
        sour = []
        for s in sources:
            try:
                if corrections[s] == s:
                    sour.append(s)
            except Exception as inst:
                pass
        old_elem[u'Sources'] = sour
    except Exception as inst:
        pass
    return old_elem
