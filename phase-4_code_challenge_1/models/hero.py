from ..app import ma,db

class Hero(db.Model):
    __tablename__ = 'heroes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    super_name = db.Column(db.String(100), nullable=False)
    powers = db.relationship('HeroPower', backref='hero', cascade="all, delete-orphan", lazy=True)

class HeroSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'super_name', 'powers')

hero_schema = HeroSchema()
heroes_schema = HeroSchema(many=True)