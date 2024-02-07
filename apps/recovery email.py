from flask import request, jsonify
from flask_restful import Resource
from your_models import User, db
import datetime
import secrets

class PasswordRecoveryEmail(Resource):
    def post(self):
        email = request.json.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            user.recovery_token = secrets.token_hex(16)
            user.recovery_token_expiry = datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
            db.session.commit()
            # Send the password recovery email with the token and a link to the reset endpoint
            pass
        else:
            return jsonify({'message': 'User not found'}), 404