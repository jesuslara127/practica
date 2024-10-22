from flask import Flask, jsonify, make_response

app = Flask(__name__)

data = [
    {
        "id": 1,
        "nombre": "Jesus",
        "descripcion": "Descripción del elemento 1"
    },
    {
        "id": 2,
        "nombre": "Alejandro",
        "descripcion": "Descripción del elemento 2"
    }
]

@app.route('/api/datos', methods=['GET'])
def get_data():
    return jsonify(data)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "No se encontro"}), 404)

if __name__ == '__main__':
    app.run(debug=True)
