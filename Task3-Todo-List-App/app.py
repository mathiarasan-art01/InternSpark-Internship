from __future__ import annotations

import logging
import os
from datetime import datetime, UTC
from logging.handlers import RotatingFileHandler

from flask import Flask, render_template

from config import Config
from models.task_model import init_db, close_db
from routes.task_routes import task_bp
from routes.api_routes import api_bp
from routes.auth_routes import auth_bp


def create_app(config_class=Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    # -------------------------
    # Logging
    # -------------------------
    os.makedirs(app.config["LOG_DIR"], exist_ok=True)

    handler = RotatingFileHandler(
        os.path.join(app.config["LOG_DIR"], "app.log"),
        maxBytes=200_000,
        backupCount=3,
    )

    handler.setFormatter(
        logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
    )

    handler.setLevel(logging.INFO)

    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    # -------------------------
    # DB
    # -------------------------
    with app.app_context():
        init_db()

    app.teardown_appcontext(close_db)

    # -------------------------
    # Blueprints
    # -------------------------
    app.register_blueprint(task_bp)
    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    # -------------------------
    # Error Handlers
    # -------------------------
    @app.errorhandler(404)
    def not_found(_e):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error(_e):
        app.logger.exception("500 error")
        return render_template("errors/500.html"), 500

    # -------------------------
    # Template filter
    # -------------------------
    @app.template_filter("nicedate")
    def nicedate(value):
        if not value:
            return "—"
        try:
            return datetime.fromisoformat(
                str(value).replace(" ", "T")
            ).strftime("%b %d, %Y")
        except Exception:
            return value

    # -------------------------
    # Globals
    # -------------------------
    @app.context_processor
    def inject_globals():
        return {
            "current_year": datetime.now(UTC).year,
            "app_name": "TaskNest",
        }

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)