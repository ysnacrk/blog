from main import db , bcrypt
from main.models import User,Post
import sys

try:
  db.create_all()
except NameError:
  print("Unexpected error:", sys.exc_info()[0])


user = User( username = sys.argv[1] , password=bcrypt.generate_password_hash(sys.argv[2]))

if user:
  print("Tables and user created")	
  print(user.username)
  print(user.password)
else:
  exit()
db.session.add(user)
db.session.commit()
