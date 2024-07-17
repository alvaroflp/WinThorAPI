from flask import Flask
from flask_jwt_extended import JWTManager
from src.routes.cliente import cliente_bp
from src.routes.produto import produto_bp
from src.routes.auth import auth_bp
from config import JWT_SECRET_KEY

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY  # Configuração da chave secreta JWT
jwt = JWTManager(app)

app.register_blueprint(cliente_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(produto_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
