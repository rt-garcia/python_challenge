from sqlalchemy.ext.hybrid import hybrid_property
from app.api.db import db
from app.api.model.cuboid import Cuboid


class Bag(db.Model):
    __tablename__ = "bags"

    id = db.Column(db.Integer, primary_key=True)
    volume = db.Column(db.Integer)
    title = db.Column(db.String(255), nullable=True)
    cuboids = db.relationship(Cuboid, backref="bag")

    @hybrid_property
    def payload_volume(self):
        volume = 0
        for cuboid in self.cuboids:
            volume += cuboid.volume
        return volume

    @hybrid_property
    def available_volume(self):
        return self.volume - self.payload_volume
