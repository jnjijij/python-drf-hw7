def post(self):
    email = request.json.get('email')
    if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({'message': 'Invalid email'}), 400
    user = User.query.filter_by(email=email).first()
    # ...