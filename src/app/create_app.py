from flask import Flask

from src.app.emoji.views import emoji_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(emoji_bp)
    return app

if __name__ == '__main__':
    create_app().run(debug=True)