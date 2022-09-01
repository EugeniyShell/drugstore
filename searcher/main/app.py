import logging
from logging.handlers import TimedRotatingFileHandler

from flask import Flask, render_template, request
from flask.logging import default_handler

# версия мануального парсинга сайта грлс
# from main.grls_drugs_finder import GRLS_drugs_finder
from main.drugstore_crawler import crawl_it
from logs.logger import get_logger
from main.definitions import SQLALCHEMY_DATABASE_URI, \
        LOGGING_LEVEL, SQLALCHEMY_TRACK_MODIFICATIONS
from main.data_base import db, base_search


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = \
        SQLALCHEMY_TRACK_MODIFICATIONS
    # используем встроенный логгер фласка
    # log_formatter = logging.Formatter(fmt=LOG_STRING_FORMAT,
    #                                   datefmt=LOG_DATE_FORMAT)
    # log_handler = TimedRotatingFileHandler(LOGPATH, encoding='utf8',
    #                                        interval=1, when='D')
    # log_handler.setFormatter(log_formatter)
    # app.logger.removeHandler(default_handler)
    # app.logger.addHandler(log_handler)
    # app.logger.setLevel(LOGGING_LEVEL)
    app.logger = get_logger(LOGGING_LEVEL)

    @app.route("/")
    @app.route("/index")
    def index(message="Начните поиск"):
        app.logger.info('index page')
        return render_template('index.tpl', message=message)

    @app.route("/variants", methods=['GET'])
    def variants():
        search = request.args.get('search')
        app.logger.info(f'variants page: {search}')
        if not search:
            return index('Вы ничего не ввели, будьте внимательнее')
        search_list = base_search(search)
        if not len(search_list):
            return index(f'Не удалось найти "{search}", '
                         f'попробуйте другое ключевое слово')
        return render_template('variants.tpl', message=search,
                               search_list=search_list)

    @app.route("/result", methods=['POST'])
    def result():
        search_list = request.form.getlist('search')
        app.logger.info(f'result page: {search_list}')
        result_list = crawl_it(search_list)
        return render_template('result.tpl', search_list=search_list,
                               result_list=result_list)

    @app.errorhandler(404)
    def page404(_):
        return index('Произошла чудовищная ошибка, попробуйте поискать снова')

    db.init_app(app)
    app.logger.info('app started!!!')
    return app
