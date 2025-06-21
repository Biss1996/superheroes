from flask import Blueprint, jsonify, request
from models import Power, db

powers_bp = Blueprint('powers', __name__)

@powers_bp.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

@powers_bp.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict())

@powers_bp.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    try:
        power.description = data.get("description", power.description)
        db.session.commit()
        return jsonify(power.to_dict())
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400
