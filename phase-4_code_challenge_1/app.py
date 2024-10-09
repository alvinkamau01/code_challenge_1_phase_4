from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

# Initialize app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'

# Initialize DB, Marshmallow, and Migrate
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

# Import models after db is initialized
from .models.hero import Hero, heroes_schema, hero_schema
from .models.power import Power, powers_schema, power_schema
from .models.heroes_powers import HeroPower, heroes_power_schema, hero_power_schema
# Helper function for returning 404
def not_found_response(entity):
    return jsonify({"error": f"{entity} not found"}), 404

# Route: Get all heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    results = heroes_schema.dump(heroes)
    return jsonify(results)

# Route: Get hero by ID
@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        result = hero_schema.dump(hero)  # Corrected 'dumb' to 'dump'
        return jsonify(result)
    return not_found_response("Hero")

# Route: Get all powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    results = powers_schema.dump(powers)
    return jsonify(results)

# Route: Get power by ID
@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power:
        result = power_schema.dump(power)
        return jsonify(result)
    return not_found_response("Power")

# Route: Patch an existing power
@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if power:
        description = request.json['description']  # Changed to request.json
        power.description = description
        db.session.commit()
    else:
        return jsonify({"message": {"error": "Power not found"}}), 404
    return jsonify({"message": "Power updated successfully"})

# Route: Create a new HeroPower
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.json
    hero_id = data.get('hero_id')
    power_id = data.get('power_id')
    strength = data.get('strength')

    if not hero_id or not power_id:
        return jsonify({"errors": ["validation errors"]}), 404

    if strength not in ["Strong", "Weak", "Average"]:
        return jsonify({"errors": ["validation errors"]}), 404

    new_entry = HeroPower(hero_id=hero_id, power_id=power_id, strength=strength)
    db.session.add(new_entry)
    db.session.commit()

    return jsonify({"message": "Hero power created successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)