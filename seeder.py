
###
### RUN THIS TO RESET THE VALUES IN THE DATABASE.
###
### python3 seeder.py
###
import json
from tinydb import TinyDB

with TinyDB("database.json") as db:
    db.purge_tables()

    chinese_table = db.table("chinese_zodiac")
    with open("chinesezodiac.json") as chinesezodiac:
        animals = json.load(chinesezodiac)
        for animal in animals:
            chinese_table.insert(animal)

    western_table = db.table("western_zodiac")
    with open("westernzodiac.json") as westernzodiac:
        symbols = json.load(westernzodiac)
        for symbol in symbols:
            western_table.insert(symbol)