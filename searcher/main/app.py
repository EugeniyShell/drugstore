from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/")
    @app.route("/index")
    def index(message="index"):
        return f"{message}"

    @app.route("/result")
    def result():
        return "result"

    @app.errorhandler(404)
    def page404(_):
        return index("Previous page not found - 404. "
                     "But you can search another!")

    return app
