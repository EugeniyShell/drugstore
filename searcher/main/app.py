from flask import Flask, render_template, request

from main.grls_parser import grls_finder


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/")
    @app.route("/index")
    def index(message="search"):
        return render_template('index.tpl', message=message)

    @app.route("/result", methods=['GET'])
    def result():
        search = request.args.get('search')
        search_list = grls_finder(search)
        if not len(search_list):
            return index("FOUND NOTHING! But you can search another!")
        return render_template('result.tpl', message=search,
                               search_list=search_list)

    @app.errorhandler(404)
    def page404(_):
        return index("Previous page not found - 404. "
                     "But you can search another!")

    return app
