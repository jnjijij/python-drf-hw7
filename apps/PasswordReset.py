def post(self):
    token = request.json.get('token')
    new_password = request.json.get('new_password')
    if not token or not new_password or not re.match(r"^[a-zA-Z0-9]{8,}$", new_password):
        return jsonify({'message': 'Invalid token or password'}), 400
    user = User.query.filter_by(recovery_token=token, recovery_token_expiry__gt=datetime.datetime.utcnow()).first()
    # ...