if __name__ == '__main__':
    context = ('your_cert.pem', 'your_key.pem')
    app.run(debug=False, ssl_context=context, threaded=True)