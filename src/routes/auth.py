from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from src.models.database import Database

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get("usuario")
    senha = data.get("senha")

    db = Database()
    try:
        sql = """
        SELECT USUARIOBD, NOME
          FROM PCEMPR
         WHERE USUARIOBD = :USUARIOBD
           AND DECRYPT(SENHABD, USUARIOBD) = :SENHABD
        """
        result = db.query(sql, {"USUARIOBD": usuario, "SENHABD": senha})
        if result:
            access_token = create_access_token(identity={"usuario": usuario})
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({"message": "Usuário ou senha inválidos"}), 401
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    finally:
        db.close()
