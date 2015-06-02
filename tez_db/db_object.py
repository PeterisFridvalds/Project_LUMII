# -*- coding: utf-8 -*-
from pymongo import Connection
import pymongo

## Funkcija datu bāzes attīrīšanai radīšanai no jauna
def create_db(input_data):
    db_name = "tezaurs_db"
    connection = Connection()
    db = connection[db_name]
    tezaur_table = db['tezaur_data']
    tezaur_table.remove()

    lem = []

    try:
        for line in input_data:
            tezaur_table.save(line)
    except Exception as inst:
        pass
    try:
        tezaur_table.create_index("Header.Lemma")
        tezaur_table.create_index("Header.Gram.AltLemma.Lemma")
        tezaur_table.create_index("Derivatives.Header.Lemma")
        lem.append("Index created")
    except Exception as inst:
        lem.append("Index not created")

    return lem

## Funkcija datu bāzes datu pievienošanai
def add_db_object(input_data):
    db_name = "tezaurs_db"
    connection = Connection()
    db = connection[db_name]
    tezaur_table = db['tezaur_data']

    lem = []

    try:
        for line in input_data:
            tezaur_table.save(line)
    except Exception as inst:
        pass
    try:
        tezaur_table.create_index("Header.Lemma")
        tezaur_table.create_index("Header.Gram.AltLemma.Lemma")
        tezaur_table.create_index("Derivatives.Header.Lemma")
        lem.append("Index created")
    except Exception as inst:
        lem.append("Index not created")

    return lem

## Funkcija meklēšanai datu bāzē
def find_word_in_db(word, ID):
    db_name = "tezaurs_db"
    connection = Connection()
    db = connection[db_name]
    tezaur_table = db['tezaur_data']
    try:
        data = tezaur_table.find({"Header.Lemma": word})
    except Exception as inst:
        data = []
    for i in data:
        if i[u'ID'] == ID:
            return i
    return None

## Funkcija datu bāzes  datu atjaunināšanai
def update_db_object(input_data, word, ID):
    db_name = "tezaurs_db"
    connection = Connection()
    db = connection[db_name]
    tezaur_table = db['tezaur_data']
    lem = []

    try:
        tezaur_table.remove({"Header.Lemma": word, "ID": ID})
        tezaur_table.save(input_data)
    except Exception as inst:
        pass
    try:
        tezaur_table.create_index("Header.Lemma")
        tezaur_table.create_index("Header.Gram.AltLemma.Lemma")
        tezaur_table.create_index("Derivatives.Header.Lemma")
        lem.append("Index created")
    except Exception as inst:
        lem.append("Index not created")

    return

## Funkcija kļūdu paziņojumu par tezaur datiem saglabāšanai
def add_correction(correction, word, word_ID):
    db_name = "tezaurs_db"
    connection = Connection()
    db = connection[db_name]
    corection_table = db['tezaur_corrections']
    data = {}

    elements = corection_table.find({"Lemma": word, "ID": word_ID})
    for elem in elements:
        if elem[u'ID'] == word_ID:
            data["Lemma"] = elem[u'Lemma']
            data["ID"] = elem[u'ID']
            data["info"] = [correction]
            for elem_info in elem[u'info']:
                data["info"].append(elem_info)
            corection_table.remove({"Lemma": word, "ID": word_ID})
            corection_table.save(data)
            return
    data = {'Lemma': word, 'ID': word_ID, 'info': [correction]}
    corection_table.save(data)

    return

## Funkcija kļūdu paziņojumu apkopšanai
def show_correction():
    db_name = "tezaurs_db"
    connection = Connection()
    db = connection[db_name]
    corection_table = db['tezaur_corrections']
    output = []

    for elem in corection_table.find():
        output.append({'Lemma':elem["Lemma"], 'ID':elem["ID"], 'info':elem["info"]})

    if output == []:
        return "no_correction"
    else:
        return output


    
