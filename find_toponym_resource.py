from flask import jsonify
from flask_restful import abort, Resource, reqparse
from geocoding import geocoding


parser = reqparse.RequestParser()
# Координаты пользователя
parser.add_argument('coordinates', required=True, type=str)
# Запрос пользователя
parser.add_argument('request', required=True, type=str)


class FindToponymResource(Resource):
    def post(self):
        try:
            args = parser.parse_args()
            # Проверка на правильный тип данных
            list(map(float, args['coordinates'].split(', ')))
        except ValueError:
            abort(400, message={'status': 'unsuccess', 'message': 'Неверный формат или тип данных'})
            return
        except Exception as e:
            abort(404, message={'status': 'unsuccess', 'message': e})
            return
        try:
            toponym = geocoding(
                args['coordinates'],
                args['request']
            )
        except Exception as e:
            abort(404, message={'status': 'unsuccess', 'message': e})
            return

        result = {
            'status': 'success',
            'message': 'Топоним найден.',
            'data': {
                'coordinates': toponym['coordinates'],
                'request': toponym['address']
            }
        }
        return jsonify(result)
