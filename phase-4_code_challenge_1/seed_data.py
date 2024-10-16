from models.hero import Hero
from models.power import Power
from models.heroes_powers import HeroPower
from app import db

def seed_data():
    hero1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    power1 = Power(name="super strength", description="gives the wielder super-human strengths")
    db.session.add(hero1)
    db.session.add(power1)
    db.session.commit()

    hero_power = HeroPower(hero_id=hero1.id, power_id=power1.id, strength="Strong")
    db.session.add(hero_power)
    db.session.commit()

if __name__ == '__main__':
    from app import app
    with app.app_context():
        db.create_all()
        seed_data()
        print("Seed data added!")
