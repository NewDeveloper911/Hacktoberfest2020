from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
'''
db = SQLAlchemy()

def create_app():
    """Construct the core application."""
    app = Flask(__name__)
    #Sets up my configuration files for my website to hide private information as well
    if app.config['ENV'] == "production":
        app.config.from_object("config.ProductionConfig")
    elif app.config['ENV'] == "development":
        app.config.from_object("config.DevelopmentConfig")
    else:
        app.config.from_object("config.TestingConfig")

    db.init_app(app)

    app.register_blueprint(blueprint, url_prefix="/admin")
    app.register_blueprint(todo, url_prefix="/todo")

    with app.app_context():
        from . import hello  # Import routes
        db.create_all()  # Create sql tables for our data models

        return app
'''

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    #remove = db.Column(db.Boolean)

# The app package is defined by the app directory and the __init__.py script
from app import routes

#Sets up my configuration files for my website to hide private information as well
