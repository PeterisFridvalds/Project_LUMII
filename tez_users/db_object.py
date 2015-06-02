from pymongo import Connection
import pymongo

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

def add_db_object(input_data):
    db_name = "tezaurs_db"
    connection = Connection()
    db = connection[db_name]
    tezaur_table = db['tezaur_data']

    lem = []

    try:
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

    return lem

def update_db_object(input_data, word, ID):
    db_name = "tezaurs_db"
    connection = Connection()
    db = connection[db_name]
    tezaur_table = db['tezaur_data']

    try:
        tezaur_table.save(input_data)
    except Exception as inst:
        pass

    return
