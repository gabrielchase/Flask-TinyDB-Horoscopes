import json
from tinydb import TinyDB, Query

db = TinyDB('database.json')

cz_table = db.table('chinese_zodiac')
wz_table = db.table('western_zodiac')


def insert_animal(name, characteristics, position):
    animal = {
        "animal": name,
        "characteristics": characteristics,
        "position": position
    }
    cz_table.insert(animal)
    return animal

def find_animal(name):
    animal_query = Query()
    result = cz_table.search(animal_query.animal.matches(name))
    if (len(result) > 0):
        return result[0]
    return None

def update_animal(name, **kwargs):
    animal_query = Query()
    result = cz_table.search(animal_query.animal.matches(name))

    # update the first entry
    if len(result) > 0:
        target = result[0]
        target_id = target.doc_id
        animal = kwargs.get("animal", target["animal"])
        characteristics = kwargs.get("characteristics", target["characteristics"])
        position = kwargs.get("position", target["position"])
        updated_record = {
            "animal": animal,
            "characteristics": characteristics,
            "position": position
        }
        cz_table.update(updated_record, doc_ids=[target_id])
        return updated_record
    return None

def delete_animal(name):
    animal_query = Query()
    result = cz_table.search(animal_query.animal.matches(name))

    # delete the first entry
    if len(result) > 0:
        target = result[0]
        target_id = target.doc_id
        cz_table.remove(doc_ids=[target_id])
        return True
    return False

def get_animals():
    return cz_table.all()












def insert_symbol(name, start, end, reading):
    # start = {
    #     "month": start_month,
    #     "day": start_day,
    # }
    # end = {
    #     "month": end_month,
    #     "day": end_day,
    # }
    symbol = {
        "symbol": name,
        "start": start,
        "end": end,
        "reading": reading
    }
    wz_table.insert(symbol)
    return symbol

def find_symbol(name):
    symbol_query = Query()
    result = wz_table.search(symbol_query.symbol.matches(name))
    if (len(result) > 0):
        return result[0]
    return None

def update_symbol(name, **kwargs):
    symbol_query = Query()
    result = wz_table.search(symbol_query.symbol.matches(name))

    # update the first entry
    if len(result) > 0:
        target = result[0]
        target_id = target.doc_id
        symbol = kwargs.get("symbol", target["symbol"])
        start = kwargs.get("start", target["start"])
        end = kwargs.get("end", target["end"])
        reading = kwargs.get("reading", target["reading"])
        updated_record = {
            "symbol": symbol,
            "start": start,
            "end": end,
            "reading": reading
        }
        wz_table.update(updated_record, doc_ids=[target_id])
        return updated_record
    return None

def delete_symbol(name):
    query = Query()
    result = wz_table.search(query.symbol.matches(name))

    # delete the first entry
    if len(result) > 0:
        target = result[0]
        target_id = target.doc_id
        wz_table.remove(doc_ids=[target_id])
        return True
    return False

def get_symbols():
    return wz_table.all()