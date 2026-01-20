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
def all_people():
    return














# [GET] /people/<int:people_id> Muestra la información de un solo personaje según su id.
@app.route('/people', methods=['GET'])
def all_people():
    return





# [GET] /planets Listar todos los registros de planets en la base de datos.
@app.route('/people', methods=['GET'])
def all_people():
    return





# [GET] /planets/<int:planet_id> Muestra la información de un solo planeta según su id.
@app.route('/people', methods=['GET'])
def all_people():
    return





# [GET] /users Listar todos los usuarios del blog.
@app.route('/people', methods=['GET'])
def all_people():
    return





# [GET] /users/favorites Listar todos los favoritos que pertenecen al usuario actual.
@app.route('/people', methods=['GET'])
def all_people():
    return




# [POST] /favorite/planet/<int:planet_id> Añade un nuevo planet favorito al usuario actual con el id = planet_id.
@app.route('/people', methods=['GET'])
def all_people():
    return




# [POST] /favorite/people/<int:people_id> Añade un nuevo people favorito al usuario actual con el id = people_id.
@app.route('/people', methods=['GET'])
def all_people():
    return




# [DELETE] /favorite/planet/<int:planet_id> Elimina un planet favorito con el id = planet_id.
@app.route('/people', methods=['GET'])
def all_people():
    return




# [DELETE] /favorite/people/<int:people_id> Elimina un people favorito con el id = people_id.
@app.route('/people', methods=['GET'])
def all_people():
    return








# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
