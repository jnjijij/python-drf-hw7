from flask_limiter import Limiter

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)

@app.route('/your_endpoint', methods=['POST'])
@limiter.limit('1/minute')
def your_endpoint():
    # ...