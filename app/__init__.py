from flask import Flask


def create_app(config_name="config"):
    app = Flask(__name__)
    app.config.from_pyfile("../config.py")

    with app.app_context():
        from . import views

        from .posts import post_bp
        app.register_blueprint(post_bp)

        from .users import bp as user_bp
        app.register_blueprint(user_bp, url_prefix="/users")

    return app