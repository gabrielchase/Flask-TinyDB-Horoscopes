from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse
from tinydb import Query

import database
import json

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('animal', type=str, help='Name of animal to be inserted/updated.')
parser.add_argument('characteristics', type=str, help='Characteristics of animal to be inserted.')
parser.add_argument('position', type=int, help='The position of the animal in the calendar.')

parser.add_argument('symbol', type=str)
parser.add_argument('start', type=dict)
parser.add_argument('end', type=dict)
parser.add_argument('reading', type=str)

# Chinese Zodiac
# This is the resource for getting, updating, or deleting individual zodiac animals.
class ChineseZodiac(Resource):
    # get  animal
    def get(self, name):
        print('name: ', name, type(name))
        animal = database.find_animal(name)
        print('animal: ', animal)
        if animal is not None:
            print('2animal: ', animal)
            return animal, 200
        abort(404, message="Animal {} doesn't exist!".format(name))

    # update animal
    def put(self, name):
        kwargs = {}
        args = parser.parse_args()
        for key in args.keys():
            if args[key] is not None:
                kwargs[key] = args[key]
        animal = database.update_animal(name, **kwargs)
        if animal is not None:
            return animal, 200
        abort(404, message="Animal {} doesn't exist!".format(name))

    # delete animal
    def delete(self, name):
        success = database.delete_animal(name)
        if (success):
            return None, 200
        abort(404, message="Animal {} doesn't exist!".format(name))


# This is the resource for getting and updating the list of zodiac animals.
class ChineseZodiacList(Resource):
    # get list of animals
    def get(self):
        animals = database.get_animals()
        return animals, 200

    # post a new animal in the list
    def post(self):
        args = parser.parse_args()
        name = args["animal"]
        characteristics = args["characteristics"]
        position = args["position"]
        animal = database.insert_animal(name, characteristics, position)
        return animal, 200

api.add_resource(ChineseZodiacList, '/zodiac/chinese')
api.add_resource(ChineseZodiac, '/zodiac/chinese/<string:name>')


class WesternZodiac(Resource):
    def get(self, name):
        symbol = database.find_symbol(name)
        if symbol is not None:
            return symbol, 200
        abort(404, message="Symbol {} doesn't exist!".format(name))

    def put(self, name):
        kwargs = {}
        args = parser.parse_args()
        for key in args.keys():
            if args[key] is not None:
                kwargs[key] = args[key]
        symbol = database.update_symbol(name, **kwargs)
        if symbol is not None:
            return symbol, 200
        abort(404, message="Symbol {} doesn't exist!".format(name))

    def delete(self, name):
        success = database.delete_symbol(name)
        if (success):
            return None, 200
        abort(404, message="Symbol {} doesn't exist!".format(name))


class WesternZodiacList(Resource):
    def get(self):
        symbols = database.get_symbols()
        return symbols, 200

    def post(self):
        args = parser.parse_args()
        symbol = args["symbol"]
        start = args["start"]
        end = args["end"]
        reading = args["reading"]
        
        symbol = database.insert_symbol(symbol, start, end, reading)
        return symbol, 200

class WesternZodiacExtended(Resource):
    def get(self, year, month, day):
        symbols = database.get_symbols()
        chinese_zodiac = get_chinese_zodiac_year(year)
        print('chinese_zodiac: ', chinese_zodiac)
        western_zodiac = {}
        context = {}
        print('symbols: ', symbols)

        for idx, s in enumerate(symbols):
            print('s: ', s)
            start = s.get("start")
            print('start: ', start)
            start_month = start.get("month")
            start_day = start.get("day")
            
            if (start_month == month and day <= start_day):
                western_zodiac = symbols[(idx-1) % 12]
            elif (start_month == month and day >= start_day):
                print('RETURNING', s)
                western_zodiac =  s
        
        print('western_zodiac: ', western_zodiac)
        context = {
            'chinese_zodiac': chinese_zodiac,
            'western_zodiac': western_zodiac
        }
        print(context)

        return context, 200

def get_chinese_zodiac_year(year): 
    zodiac_array = ['dragon', 'snake', 'horse', 'sheep', 'monkey', 'rooster', 'dog', 'pig', 'rat', 'ox', 'tiger', 'hare']
    # zodiac_dict = {
    #     '0': 'dragon',
    #     '1': 'snake',
    #     '2': 'horse',
    #     '3': 'sheep',
    #     '4': 'monkey',
    #     '5': 'rooster',
    #     '6': 'dog',
    #     7: 'pig',
    #     8: 'rat',
    #     9: 'ox',
    #     10: 'tiger',
    #     11: 'hare'
    # }
    n = (year - 2000) % 12
    print('n: ', n)
    name = zodiac_array[n]
    print('name: ', name)
    return database.find_animal(name) 
    

api.add_resource(WesternZodiacList, '/zodiac/western')
api.add_resource(WesternZodiac, '/zodiac/western/<string:name>')
api.add_resource(WesternZodiacExtended, '/zodiac/reading/<int:year>/<string:month>/<int:day>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)