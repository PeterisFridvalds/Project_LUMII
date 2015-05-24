class TezaursRouter(object): 
    def db_for_read(self, model, **hints):
        "Point all operations on tezaurs models to 'tezaurs_db'"
        if model._meta.app_label == 'tezaurs':
            return 'tezaurs_db'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on tezaurs models to 'tezaurs_db'"
        if model._meta.app_label == 'tezaurs':
            return 'tezaurs_db'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in tezaurs app"
        if obj1._meta.app_label == 'tezaurs' and obj2._meta.app_label == 'tezaurs':
            return True
        # Allow if neither is tezaurs app
        elif 'tezaurs' not in [obj1._meta.app_label, obj2._meta.app_label]: 
            return True
        return False
    
    def allow_syncdb(self, db, model):
        if db == 'tezaurs_db' or model._meta.app_label == "tezaurs":
            return False # we're not using syncdb on our legacy database
        else: # but all other models/databases are fine
            return True
