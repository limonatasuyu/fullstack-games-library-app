from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import uuid

app = Flask(__name__)

# for updating the app constantly
app.config.from_object(__name__)

CORS(app, origins='http://localhost:8080')

@app.route('/', methods=['GET'])
def greetings():
    return("Hi")

@app.route('/shark', methods=['GET'])
def shark():
    return ('Shark ><> !')

Games = [   
{'id': uuid.uuid4().hex, 'title': '2k21',            'genre': 'Sports', 'played': False},
{'id': uuid.uuid4().hex, 'title': 'Evil Within',     'genre': 'Horror', 'played': False},
{'id': uuid.uuid4().hex, 'title': 'GTA San Andreas', 'genre': 'Action', 'played': True },
]

# The GET and POST route handler
@app.route('/games', methods=['GET', 'POST'])
def games():
    response_object = {'status': 'success'}
    
    if request.method == "POST":
        post_data = request.get_json()
        Games.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played'),
        })
        response_object['message'] = 'Game Added!'
    else:
        response_object['games'] = Games
    
    return jsonify(response_object)


# The PUT and DELETE route handler
@app.route('/games/<game_id>', methods=['PUT', 'DELETE'])
def single_game(game_id):
    response_object = {'status': 'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        remove_game(game_id)
        Games.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played'),
        })
        response_object['message'] = 'Game Updated!'
    if request.method == "DELETE":
        remove_game(game_id)
        response_object['message'] = 'Game Removed'    
    return jsonify(response_object)

# Removing the game to update
def remove_game(game_id):
    for game in Games:
        if game['id'] == game_id:
            Games.remove(game)
            return True
    return False

if __name__ == '__main__':
    app.run(debug=True)
