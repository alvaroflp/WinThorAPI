from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from src.models.database import Database
from datetime import datetime

cliente_bp = Blueprint('cliente_bp', __name__)

def format_date(date):
    if date:
        return date.strftime("%d-%m-%Y %H:%M:%S")
    return None

@cliente_bp.route('/clientes/<int:codcli>', methods=['GET'])
@jwt_required()
def get_cliente(codcli):
    db = Database()
    try:
        sql = """
        SELECT codcli,
               cliente,
               cgcent    cpfcnpj,
               ieent     ie,
               fantasia,
               limcred,
               dtcadastro,
               dtprimcompra,
               dtultcomp,
               municent,
               bairroent,
               cepent,
               enderent
          FROM pcclient
         WHERE codcli = :codcli
        """
        result = db.query(sql, {"codcli": codcli})
        if result:
            cliente = {
                "codcli": result[0][0],
                "cliente": result[0][1],
                "cpfcnpj": result[0][2],
                "ie": result[0][3],
                "fantasia": result[0][4],
                "limcred": result[0][5],
                "dtcadastro": format_date(result[0][6]),
                "dtprimcompra": format_date(result[0][7]),
                "dtultcomp": format_date(result[0][8]),
                "municent": result[0][9],
                "bairroent": result[0][10],
                "cepent": result[0][11],
                "enderent": result[0][12]
            }
            return jsonify(cliente), 200
        else:
            return jsonify({"message": "Cliente não encontrado"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    finally:
        db.close()
