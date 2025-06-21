from flask import Blueprint, request, jsonify
from flask_mail import Message
from models import HeroPower, Hero, Power, db
from mail import mail

hero_powers_bp = Blueprint('hero_powers', __name__)

@hero_powers_bp.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    strength = data.get("strength")
    power_id = data.get("power_id")
    hero_id = data.get("hero_id")

    # Validate strength
    if strength not in ["Strong", "Weak", "Average"]:
        return jsonify({"errors": ["Strength must be 'Strong', 'Weak', or 'Average'"]}), 400

    # Check Hero and Power existence
    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)
    if not hero or not power:
        return jsonify({"errors": ["Hero or Power not found"]}), 404

    try:
        hero_power = HeroPower(strength=strength, hero_id=hero_id, power_id=power_id)
        db.session.add(hero_power)
        db.session.commit()

        # Send mail
        msg = Message(
            subject="New Hero Power Assigned",
            recipients=["bismarckkip684@gmail.com"],
            body=f"{hero.name} ({hero.super_name}) has been assigned the power '{power.name}' with strength {strength}."
        )
        mail.send(msg)

        return jsonify({
            "id": hero_power.id,
            "hero_id": hero.id,
            "power_id": power.id,
            "strength": hero_power.strength,
            "hero": {
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name
            },
            "power": {
                "id": power.id,
                "name": power.name,
                "description": power.description
            }
        }), 201
    except Exception as e:
        print("Error:", e)
        return jsonify({"errors": ["validation errors"]}), 400
