from config import ma,db
from .heroes_powers import HeroPower

class Power(db.Model):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    # Use string reference for the relationship
    Hero = db.relationship('HeroPower', backref='power', lazy=True)

# Schema for Power
class PowerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Power
        load_instance = True
        fields = ('id', 'name', 'description', 'heroes')

power_schema = PowerSchema()
powers_schema = PowerSchema(many=True)