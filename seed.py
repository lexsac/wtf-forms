"""Seed file to make sample data for db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Make a bunch of pets
p1 = Pet(name="Mia", species="dog", age="5", available=True)
p2 = Pet(name="Patrick", species="turtle", age="100", available=True)
p3 = Pet(name="Scooter", species="dog", age="1", available=True)
p4 = Pet(name="Calvin", species="cat", age="9", available=True)
p5 = Pet(name="Sarah", species="snake", age="3", available=True)

# commit to pets database
db.session.add_all([p1, p2, p3, p4, p5])
db.session.commit()

