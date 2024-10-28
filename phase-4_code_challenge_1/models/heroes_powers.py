from config import ma, db


class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(20), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)


# Schema for HeroPower
class HeroPowerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = HeroPower
        load_instance = True

hero_power_schema = HeroPowerSchema()
heroes_power_schema = HeroPowerSchema(many=True)
