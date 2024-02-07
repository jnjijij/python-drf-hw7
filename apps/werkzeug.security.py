from werkzeug.security import generate_password_hash

user = User(email=email, password=generate_password_hash(password))