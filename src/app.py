"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from sqlalchemy import select
from models import db, User, Favorites, FavoritePlanet, FavoriteCharacter, FavoriteStarship, Planet, Starship, Character
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# [GET] /people Listar todos los registros de people en la base de datos.
@app.route('/people', methods=['GET'])
def get_all_people():
    characters = db.session.execute(select(Character)).scalars().all()

    return jsonify({"people": [character.mostrar_informacion() for character in characters]}), 200


# [GET] /people/<int:people_id> Muestra la información de un solo personaje según su id.
@app.route('/people/<int:people_id>', methods=['GET'])
def get_character(people_id):
    character = db.session.get(Character, people_id)
        
    if not character:
        return jsonify({"details": "character not found"}), 404
    
    informacion = character.mostrar_informacion()
    return jsonify(informacion), 200



# [GET] /planets Listar todos los registros de planets en la base de datos.
@app.route('/planet', methods=['GET'])
def get_all_planets():
    planets = db.session.execute(select(Planet)).scalars().all()

    return jsonify({"planet": [planet.planet_informacion() for planet in planets]}), 200



# [GET] /planets/<int:planet_id> Muestra la información de un solo planeta según su id.
@app.route('/planet/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = db.session.get(Planet, planet_id)
        
    if not planet:
        return jsonify({"details": "planet not found"}), 404
    
    informacion = planet.planet_informacion()
    return jsonify(informacion), 200



# # [GET] /users Listar todos los usuarios del blog.
@app.route('/user', methods=['GET'])
def get_all_users():
    users = db.session.execute(select(User)).scalars().all()

    return jsonify({"user": [user.user_information() for user in users]}), 200



# [GET] /users/favorites Listar todos los favoritos que pertenecen al usuario actual.
@app.route('/users/favorites', methods=['GET'])
def get_users_favorites():
    user_id = 1

    user = db.session.get(User, user_id)

    if not user:
        return jsonify({"details": "user not found"}), 404
    
    favorites = user.favorites

    if not favorites:
        return jsonify({
            "planets": [],
            "characters": [],
            "starships": []
        }), 200
    
    favorites = favorites[0]

    return jsonify({
        "planets": [
            fav.planet.planet_informacion()
            for fav in favorites.favorites_planet
        ],
        "characters": [
            fav.character.mostrar_informacion()
            for fav in favorites.favorites_character
        ],
        "starships": [
            fav.starship.starship_informacion()
            for fav in favorites.favorites_starship
        ]
    }), 200




# # [POST] /favorite/planet/<int:planet_id> Añade un nuevo planet favorito al usuario actual con el id = planet_id.
# @app.route('/people', methods=['POST'])
# def all_people():
#     return




# # [POST] /favorite/people/<int:people_id> Añade un nuevo people favorito al usuario actual con el id = people_id.
# @app.route('/people', methods=['POST'])
# def all_people():
#     return




# # [DELETE] /favorite/planet/<int:planet_id> Elimina un planet favorito con el id = planet_id.
# @app.route('/people', methods=['DELETE'])
# def all_people():
#     return




# # [DELETE] /favorite/people/<int:people_id> Elimina un people favorito con el id = people_id.
# @app.route('/people', methods=['GET'])
# def all_people():
#     return








# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
