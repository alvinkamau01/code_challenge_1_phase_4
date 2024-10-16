### Project structure
phase-4_code_challenge_1/
├── app.py
├── config.py
├── models/
│   ├── __init__.py
│   ├── hero.py
│   ├── power.py
│   └── heroes_powers.py
├── seed_data.py
└── instance/
    └── heroes.db


## Install dependencies
pip install Flask Flask-SQLAlchemy Flask-Migrate Flask-Marshmallow

## setup database
flask db init
flask db migrate
flask db upgrade

## Seed database
python seed_data.py


## API Endpoints

GET /heroes: Retrieve all heroes
GET /heroes/<id>: Retrieve a specific hero
GET /powers: Retrieve all powers
GET /powers/<id>: Retrieve a specific power
PATCH /powers/<id>: Update a power
POST /hero_powers: Create a new hero power association

The server will start, typically on `http://127.0.0.1:5000/`


## Models

Hero: Represents a superhero
Power: Represents a superpower
HeroPower: Represents the association between heroes and powers