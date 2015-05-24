from pymongo import Connection

def show_db():
    db_name = "tezaurs_db"
    connection = Connection()
    lem = []

    db = connection[db_name]

    tezaur_table = db['tezaur_data']
    
    for data_field in tezaur_table.find():
        lem.append(data_field["Header"]["Lemma"])

    return lem
