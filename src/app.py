from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash
from bson import ObjectId

app = Flask(__name__)
app.config['MONGO_URI']="mongodb://localhost/userpythondb"
mongo = PyMongo(app)



@app.route("/users", methods=['GET'])
def get_users():
    user_list = []
    data = mongo.db.users.find()
    for user in data:
        user['_id'] = str(user['_id'])
        user_list.append(user)
    return jsonify(user_list)


@app.route("/users/<user_id>", methods=['GET'])
def get_user(user_id):
    user_id_object = ObjectId(user_id)
    user_found = mongo.db.users.find_one({'_id': user_id_object})
    user_found['_id'] = str(user_found['_id'])
    if not user_found:
        return jsonify({"message": "El usuario no existe"})
    else: 
        return jsonify(user_found)


@app.route("/users", methods=['POST'])
def create_users():
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']

    user_found = mongo.db.users.find_one({"email" : email})
    if user_found:
        return jsonify({"message": "El email ya esta registrado"})
    if username and password and email:
        hashed_password = generate_password_hash(password)
        result = mongo.db.users.insert_one(
            {
                'username': username,
                'password': hashed_password,
                'email': email
            }
        )
        inserted_id = str(result.inserted_id)
      
        response = {
            'id': inserted_id,
            'username': username,
            'password': hashed_password, 
            'email': email
        }
        return response
    else: 
        return {"message": "Todos los campos son obligatorios"}


@app.route("/users/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    object_user_id = ObjectId(user_id)
    user_found = mongo.db.users.find_one_and_delete({'_id' : object_user_id}, projection= None, sort= None)
    if not user_found:
        return jsonify({"message": "El usuario no existe"})
    return jsonify({"message" : "Usuario eliminado con exito"})


@app.route("/users/<user_id>", methods=['PUT'])
def edit_user(user_id):
    user_id_object = ObjectId(user_id)
    user_found = mongo.db.users.find_one({'_id': user_id_object})
    user_found_id = str(user_found['_id'])
    user_found['_id'] = user_found_id
    if not user_found:
        return jsonify({"message": "El usuario no existe"})
    update_user = {
        'username': request.json.get('username', user_found.get('username')),
        'email': request.json.get('email', user_found.get('email'))
    }
    print(update_user)
    filter_config = {'_id': ObjectId(user_found_id) }
    edit_user = mongo.db.users.find_one_and_update(filter_config, {'$set': update_user}, return_document=True)
    return 'Usuario actualizado'

if __name__ == "__main__":
    app.run(debug=True)
    with app.app_context():
        print(f"Conectando a la base de datos: {mongo.db}")
    
