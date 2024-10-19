import os
from dotenv import load_dotenv
import openrouteservice as ors

load_dotenv()
KEY: str = os.getenv('KEY')


def build_route(start_pos, end_pos):
    client: ors.Client = ors.Client(key=KEY)
    coordinates: list[list[float]] = [start_pos, end_pos]
    try:
        route: dict = client.directions(
            coordinates=coordinates,
            profile='foot-walking',
            format='geojson',
            options={"avoid_features": ["steps"]},
            validate=False,
        )
    except Exception as e:
        return {'error': e}

    return {'route': route['features'][0]['geometry']['coordinates']}
