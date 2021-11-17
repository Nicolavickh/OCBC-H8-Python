import os
from config import db
from models import Directors, Movies

# Create the database
db.create_all()

db.session.commit()