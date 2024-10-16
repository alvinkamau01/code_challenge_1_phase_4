from config import ma,db

class Power(db.Model):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    heroes = db.relationship('HeroPower', backref='power', lazy=True)

class PowerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'heroes')

power_schema = PowerSchema()
powers_schema = PowerSchema(many=True)