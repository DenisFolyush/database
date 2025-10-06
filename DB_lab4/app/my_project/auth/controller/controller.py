from flask import Blueprint, request, jsonify
from app.my_project.auth.service.country_service import CountryService
from app.my_project.auth.service.city_service import CityService

controller = Blueprint('controller', __name__)

# --------------------
# Countries
# --------------------

@controller.route('/countries', methods=['GET'])
def get_countries():
    """
    Get all countries
    ---
    tags: [Countries]
    responses:
      200:
        description: List of countries
        schema:
          type: array
          items:
            type: object
            properties:
              id:   {type: integer, example: 1}
              name: {type: string,  example: "Ukraine"}
              code: {type: string,  example: "UA"}
    """
    countries = CountryService.get_all_countries()
    return jsonify([{"id": c.id_country, "name": c.name, "code": c.code} for c in countries])


@controller.route('/countries/<int:id_country>', methods=['GET'])
def get_country(id_country):
    """
    Get country by id
    ---
    tags: [Countries]
    parameters:
      - in: path
        name: id_country
        type: integer
        required: true
        description: Country id
    responses:
      200:
        description: Country
        schema:
          type: object
          properties:
            id:   {type: integer}
            name: {type: string}
            code: {type: string}
      404:
        description: Not found
    """
    country = CountryService.get_country_by_id(id_country)
    if country:
        return jsonify({"id": country.id_country, "name": country.name, "code": country.code})
    return jsonify({"error": "Country not found"}), 404


@controller.route('/countries', methods=['POST'])
def create_country():
    """
    Create country
    ---
    tags: [Countries]
    consumes: [application/json]
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [name, code]
          properties:
            name: {type: string, example: "Ukraine"}
            code: {type: string, example: "UA"}
    responses:
      201: {description: Created}
      400: {description: Bad request}
    """
    data = request.json
    country = CountryService.create_country(data)
    return jsonify({"id": country.id_country, "name": country.name, "code": country.code}), 201


@controller.route('/countries/<int:id_country>', methods=['PUT'])
def update_country(id_country):
    """
    Update country
    ---
    tags: [Countries]
    consumes: [application/json]
    parameters:
      - in: path
        name: id_country
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name: {type: string}
            code: {type: string}
    responses:
      200: {description: Updated}
      404: {description: Not found}
    """
    data = request.json
    country = CountryService.update_country(id_country, data)
    if country:
        return jsonify({"id": country.id_country, "name": country.name, "code": country.code})
    return jsonify({"error": "Country not found"}), 404


@controller.route('/countries/<int:id_country>', methods=['DELETE'])
def delete_country(id_country):
    """
    Delete country
    ---
    tags: [Countries]
    parameters:
      - in: path
        name: id_country
        type: integer
        required: true
    responses:
      200: {description: Deleted}
      404: {description: Not found}
    """
    CountryService.delete_country(id_country)
    return jsonify({"message": "Country deleted successfully"})


@controller.route('/countries/<int:id_country>/cities', methods=['GET'])
def get_cities_by_country(id_country):
    """
    Get cities by country id
    ---
    tags: [Cities]
    parameters:
      - in: path
        name: id_country
        type: integer
        required: true
        description: Country id
    responses:
      200:
        description: Cities of a country
        schema:
          type: array
          items:
            type: object
            properties:
              id:        {type: integer}
              name:      {type: string}
              longitude: {type: number, format: float}
              latitude:  {type: number, format: float}
      404: {description: No cities found}
    """
    cities = CityService.get_cities_by_country(id_country)
    if cities:
        return jsonify([{"id": c.id_city, "name": c.name, "longitude": c.longitude, "latitude": c.latitude} for c in cities])
    return jsonify({"error": "No cities found for this country"}), 404


# --------------------
# Cities
# --------------------

@controller.route('/cities', methods=['GET'])
def get_cities():
    """
    Get all cities
    ---
    tags: [Cities]
    responses:
      200:
        description: List of cities
        schema:
          type: array
          items:
            type: object
            properties:
              id:        {type: integer, example: 1}
              name:      {type: string,  example: "Kyiv"}
              longitude: {type: number,  format: float, example: 30.52}
              latitude:  {type: number,  format: float, example: 50.45}
    """
    cities = CityService.get_all_cities()
    return jsonify([{"id": c.id_city, "name": c.name, "longitude": c.longitude, "latitude": c.latitude} for c in cities])


@controller.route('/cities/<int:id_city>', methods=['GET'])
def get_city(id_city):
    """
    Get city by id
    ---
    tags: [Cities]
    parameters:
      - in: path
        name: id_city
        type: integer
        required: true
    responses:
      200:
        description: City
        schema:
          type: object
          properties:
            id:        {type: integer}
            name:      {type: string}
            longitude: {type: number, format: float}
            latitude:  {type: number, format: float}
      404: {description: Not found}
    """
    city = CityService.get_city_by_id(id_city)
    if city:
        return jsonify({"id": city.id_city, "name": city.name, "longitude": city.longitude, "latitude": city.latitude})
    return jsonify({"error": "City not found"}), 404


@controller.route('/cities', methods=['POST'])
def create_city():
    """
    Create city
    ---
    tags: [Cities]
    consumes: [application/json]
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [name, longitude, latitude]
          properties:
            name:      {type: string,  example: "Kyiv"}
            longitude: {type: number,  format: float, example: 30.52}
            latitude:  {type: number,  format: float, example: 50.45}
    responses:
      201: {description: Created}
      400: {description: Bad request}
    """
    data = request.json
    city = CityService.create_city(data)
    return jsonify({"id": city.id_city, "name": city.name, "longitude": city.longitude, "latitude": city.latitude}), 201


@controller.route('/cities/<int:id_city>', methods=['PUT'])
def update_city(id_city):
    """
    Update city
    ---
    tags: [Cities]
    consumes: [application/json]
    parameters:
      - in: path
        name: id_city
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:      {type: string}
            longitude: {type: number, format: float}
            latitude:  {type: number, format: float}
    responses:
      200: {description: Updated}
      404: {description: Not found}
    """
    data = request.json
    city = CityService.update_city(id_city, data)
    if city:
        return jsonify({"id": city.id_city, "name": city.name, "longitude": city.longitude, "latitude": city.latitude})
    return jsonify({"error": "City not found"}), 404


@controller.route('/cities/<int:id_city>', methods=['DELETE'])
def delete_city(id_city):
    """
    Delete city
    ---
    tags: [Cities]
    parameters:
      - in: path
        name: id_city
        type: integer
        required: true
    responses:
      200: {description: Deleted}
      404: {description: Not found}
    """
    CityService.delete_city(id_city)
    return jsonify({"message": "City deleted successfully"})
