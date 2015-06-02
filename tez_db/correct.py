# -*- coding: utf-8 -*-

## Labojumus ievieto tiem paredzētajos laukos
def correct(old_elem, corrections):
    try:
        if old_elem[u'Header'][u'Gram']:
            try:
                if corrections[u'H_G_F']:
                    flags = corrections[u'H_G_F'].split('; ')
                    old_elem[u'Header'][u'Gram'][u'Flags'] = flags
            except Exception as inst:
                pass
            try:
                if old_elem[u'Header'][u'Gram'][u'AltLemmas']:
                    for altLem in old_elem[u'Header'][u'Gram'][u'AltLemmas']:
                        key = altLem[u'Lemma']
                        if corrections[key]:
                            flags = corrections[key].split('; ')
                            altLem[u'Flags'] = flags
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
                            key1 = key + u'_F'
                            if corrections[key1]:
                                flags = corrections[key1].split('; ')
                                sense[u'Gram'][u'Flags'] = flags
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
                            key1 = key +u'_F'
                            if corrections[key1]:
                                flags = corrections[key1].split('; ')
                                d[u'Header']['Gram'][u'Flags'] = flags
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
        if corrections[u'sources']:
            source = corrections[u'sources'].split('; ')
            old_elem[u'Sources'] = source
    except Exception as inst:
        pass
    return old_elem
