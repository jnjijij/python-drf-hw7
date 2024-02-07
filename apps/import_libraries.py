from flask import request, jsonify
from flask_restful import Resource
from your_models import User, db
import datetime
import secrets
from werkzeug.security import generate_password_hash
from itsdangerous import URLSafeTimedSerializer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])