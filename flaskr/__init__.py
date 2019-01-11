import os

from flask import Flask


def create_app(test_config=None):
    '''
    文档：https://dormousehole.readthedocs.io/en/latest/tutorial/factory.html
    :param test_config:
    :return:
    '''
    print(__name__)
    # create and configure the app
    # 创建Flask实例
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        print(__name__)
        return 'Hello, World ibunao!'

    from . import db
    db.init_app(app)

    # 注册蓝图
    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app