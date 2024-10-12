from geocoding import geocoding
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/find_toponym', methods=['POST'])
def find_toponym():
    try:
        data = request.get_json()
        coordinates = data.get('coordinates')
        request_text = data.get('request')

        toponym = geocoding(coordinates, request_text)
        if 'error' in toponym:
            raise Exception('Not Found')
        result = {
            'status': 'success',
            'message': 'Топоним найден.',
            'data': {
                'coordinates': toponym[1],
                'request': toponym[0]
            }
        }
    except Exception as e:
        # Если возникла ошибка, можно вернуть сообщение об ошибке
        result = {
          'status': 'error',
          'message': str(e)
        }

    return jsonify(result)


if __name__ == '__main__':
    app.run()
