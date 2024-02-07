@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(str(e))
    return jsonify({'message': 'Internal server error'}), 500