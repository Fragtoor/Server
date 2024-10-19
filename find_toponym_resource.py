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
        args = parser.parse_args()
        toponym = geocoding(
            args['coordinates'],
            args['request']
        )

        if 'error' in toponym:
            return abort(404, message=toponym['error'])

        result = {
            'status': 'success',
            'message': 'Топоним найден.',
            'data': {
                'coordinates': toponym['coordinates'],
                'request': toponym['address']
            }
        }
        return jsonify(result)
