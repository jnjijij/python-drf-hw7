import jwt

def generate_password_reset_token(user_id):
    payload = {'user_id': user_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10)}
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token