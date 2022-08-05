from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

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
{'title': '2k21',            'genre': 'Sports', 'played': False},
{'title': 'Evil Within',     'genre': 'Horror', 'played': False},
{'title': 'GTA San Andreas', 'genre': 'Action', 'played': True },
]

@app.route('/games', methods=['GET', 'POST'])
def games():
    response_object = {'status': 'success'}
    
    if request.method == "POST":
        post_data = request.get_json()
        Games.append({
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played'),
        })
        response_object['message'] = 'Game Added!'
    else:
        response_object['games'] = Games
    
    return jsonify(response_object)

if __name__ == '__main__':
    app.run(debug=True)
