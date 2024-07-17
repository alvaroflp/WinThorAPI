from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from src.models.database import Database
from datetime import datetime

produto_bp = Blueprint('produto_bp', __name__)

def format_date(date):
    if date:
        return date.strftime("%d-%m-%Y %H:%M:%S")
    return None

@produto_bp.route('/produto/<int:codigo>', methods=['GET'])
@jwt_required()
def get_produto(codigo):
    db = Database()
    try:
        sql = """
            SELECT dtcadastro,
                dtultaltcom,
                dtultalter,
                dtexclusao,
                codfornec,
                codfab,
                codprod,
                codauxiliar,
                codauxiliar2,
                codauxiliartrib,
                descricao,
                embalagem,
                unidade,
                unidademaster,
                pesoliq,
                pesobruto,
                codepto,
                codsec,
                qtunit,
                qtunitcx,
                nbm as ncm,
                aceitavendafracao,
                usawms
            FROM pcprodut
            WHERE (
                    (codprod = :codigo) OR 
                    (codauxiliar = :codigo) OR 
                    (codauxiliar2 = :codigo)
                  )
        """
        
        result = db.query(sql, {"codigo": codigo})
        if result:
            produto = {
                "dtcadastro": format_date(result[0][0]),
                "dtultaltcom": format_date(result[0][1]),
                "dtultalter": format_date(result[0][2]),
                "dtexclusao": format_date(result[0][3]),
                "codfornec": result[0][4],
                "codfab": result[0][5],
                "codprod": result[0][6],
                "codauxiliar": result[0][7],
                "codauxiliar2": result[0][8],
                "codauxiliartrib": result[0][9],
                "descricao": result[0][10],
                "embalagem": result[0][11],
                "unidade": result[0][12],
                "unidademaster": result[0][13],
                "pesoliq": result[0][14],
                "pesobruto": result[0][15],
                "codepto": result[0][16],
                "codsec": result[0][17],
                "qtunit": result[0][18],
                "qtunitcx": result[0][19],
                "ncm": result[0][20],
                "aceitavendafracao": result[0][21],
                "usawms": result[0][22]
            }
            return jsonify(produto), 200
        else:
            return jsonify({"message": "Produto não encontrado"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    finally:
        db.close()
