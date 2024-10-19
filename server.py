from flask import Flask
from flask_restful import Api
import find_toponym_resource
import get_route

app = Flask(__name__)
api = Api(app)


if __name__ == '__main__':
    # API для получения координат и адреса о нужном месте для пользователя
    api.add_resource(find_toponym_resource.FindToponymResource, '/api/find_toponym')
    # API для отправки маршрута
    api.add_resource(get_route.GetRoute, '/api/get_route')
    app.run(debug=True)
