from flask import Flask, request, jsonify
from database import db
from models.user import User
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

@app.route("/login", methods=['POST'])
def login():
  data = request.json
  username = data.get("username")
  password = data.get("password")
  if username and password:
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        return jsonify({"message": "Autenticação realizada com sucesso!"})
  return jsonify({"message": "Usuário ou senha inválidos"}), 400


@app.route("/", methods=['GET'])
def test():
  return "teste"

if __name__ == '__main__':
  app.run(debug=True)