class PasswordReset(Resource):
    def post(self):
        token = request.json.get('token')
        new_password = request.json.get('new_password')
        user = User.query.filter_by(recovery_token=token, recovery_token_expiry__gt=datetime.datetime.utcnow()).first()
        if user:
            user.password = new_password  # Hash the new password
            user.recovery_token = None
            user.recovery_token_expiry = None
            db.session.commit()
            return jsonify({'message': 'Password reset successful'}), 200
        else:
            return jsonify({'message': 'Invalid or expired token'}), 401