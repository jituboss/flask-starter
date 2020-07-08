import logging
from flask import Flask
from config import Config
from raven.contrib.flask import Sentry
from flask_mongoengine import MongoEngine
from flask_bootstrap import Bootstrap

# initialize flask app
app = Flask(__name__, static_folder='static', static_url_path='')
app.config.from_object(Config)

# initialize bootstrap template
Bootstrap(app)

# initialize system logger
logger = logging.getLogger()

# initialize Database (MongoDB)
db = MongoEngine()
db.init_app(app)

#initialize sentry for error reporting
sentry_dsn = app.config["SENTRY_DSN"]
if sentry_dsn:
    sentry = Sentry(app, dsn=sentry_dsn)
else:
    logger.warning('sentry is not configured!')

# loading routes
from application import routes