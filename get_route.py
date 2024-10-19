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
        args = parser.parse_args()
        start_pos = list(map(float, args['start_pos'].split(',')))
        end_pos = list(map(float, args['end_pos'].split(',')))
        route = build_route(start_pos, end_pos)

        if 'error' in route:
            return abort(404, message=route['error'])

        result = {
            'status': 'success',
            'message': 'Маршрут построен.',
            'data': {
                'route': route['route']
            }
        }
        return jsonify(result)
