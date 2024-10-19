from flask import Flask, jsonify
from flask_restful import Api
import find_toponym_resource
import get_route

app = Flask(__name__)
api = Api(app)


# Обработчик ошибок для JSON
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'status': 'error', 'message': error.description}), 400


@app.errorhandler(404)
def not_found(error):
    return jsonify({'status': 'error', 'message': error.description}), 404


if __name__ == '__main__':
    # API для получения координат и адреса о нужном месте для пользователя
    api.add_resource(find_toponym_resource.FindToponymResource, '/api/find_toponym')
    # API для отправки маршрута
    api.add_resource(get_route.GetRoute, '/api/get_route')
    app.run(debug=True)
