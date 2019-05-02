from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1> PROBADOR PROBANDERO</h1>"


# to check DB connection:
@app.route("/users", methods=['GET'])
def users_route():
  return "<h1>Usuarios</h1>"


if __name__ == "__main__":
    # app.run(host="localhost", debug=True)
    app.run(host="0.0.0.0", debug=True)
