from flask import Flask
from app_blueprint import app_blueprint

app = Flask(__name__)

def create_app():
    # Ici, tu pourrais éventuellement ajouter d'autres configurations ou extensions Flask

    # Enregistre le blueprint dans l'application Flask
    app.register_blueprint(app_blueprint)

    return app

if __name__ == '__main__':
    create_app().run(debug=True, port=8080)
