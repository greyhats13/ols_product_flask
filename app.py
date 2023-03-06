from app.routes import app

if __name__ == '__main__':
    app.run(debug=app.config['FLASK_DEBUG'], host=app.config['FLASK_RUN_HOST'], port=app.config['FLASK_RUN_PORT'])