from flask import Flask, render_template, request

from main.data_base import db
from main.definitions import SQLALCHEMY_DATABASE_URI, \
    SQLALCHEMY_TRACK_MODIFICATIONS
from main.grls_drugs_finder import GRLS_drugs_finder


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = \
        SQLALCHEMY_TRACK_MODIFICATIONS

    @app.route("/")
    @app.route("/index")
    def index(message="search"):
        return render_template('index.tpl', message=message)

    @app.route("/variants", methods=['GET'])
    def variants():
        search = request.args.get('search')
        grls_search = GRLS_drugs_finder(search)
        search_list = grls_search.find()
        if not len(search_list):
            return index("FOUND NOTHING! But you can search another!")
        return render_template('variants.tpl', message=search,
                               search_list=search_list)

    @app.route("/result", methods=['POST'])
    def result():
        # заглушка окончательного поиска
        return render_template('result.tpl')

    @app.errorhandler(404)
    def page404(_):
        return index("Previous page not found - 404. "
                     "But you can search another!")

    db.init_app(app)
    return app
