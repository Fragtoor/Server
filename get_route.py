from flask import jsonify
from flask_restful import abort, Resource, reqparse
from build_route import build_route

parser = reqparse.RequestParser()
# Координаты начальной точки
parser.add_argument('start_pos', required=True, type=str)
# Координаты конечной точки
parser.add_argument('end_pos', required=True, type=str)


class GetRoute(Resource):
    def post(self):
        try:
            args = parser.parse_args()
            start_pos = list(map(float, args['start_pos'].split(', ')))
            end_pos = list(map(float, args['end_pos'].split(', ')))
        except ValueError:
            abort(400, message={'status': 'unsuccess', 'message': 'Неверный тип или формат данных'})
            return
        except Exception as e:
            abort(404, message={'status': 'unsuccess', 'message': e})
            return

        try:
            route = build_route(start_pos, end_pos)
        except Exception as e:
            abort(404, message={'status': 'unsuccess', 'message': e})
            return

        result = {
            'status': 'success',
            'message': 'Маршрут построен.',
            'route': route['route']
        }
        return jsonify(result)
