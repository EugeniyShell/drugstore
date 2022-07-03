from flask import Flask, render_template


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/")
    @app.route("/index")
    def index(message="search"):
        return render_template('index.tpl', message=message)

    @app.route("/result")
    def result():
        return render_template('result.tpl', message="your result")

    @app.errorhandler(404)
    def page404(_):
        return index("Previous page not found - 404. "
                     "But you can search another!")


    return app
