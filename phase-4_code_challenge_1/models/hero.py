from config import ma,db
from .heroes_powers import HeroPower

class Hero(db.Model):
    __tablename__ = 'heroes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    super_name = db.Column(db.String(100), nullable=False)
    # Use string reference for the relationship
    Power = db.relationship('HeroPower', backref='hero', cascade="all, delete-orphan", lazy=True)

# Schema for Hero
class HeroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Hero
        load_instance = True
        fields = ('id', 'name', 'super_name', 'powers')

hero_schema = HeroSchema()
heroes_schema = HeroSchema(many=True)