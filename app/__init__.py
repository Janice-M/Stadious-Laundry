from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail



#flask extensions
login_manager = LoginManager()
login_manager.session_protection = 'Strong'
login_manager.login_view = ' auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos', IMAGES)
mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    
    app.config.from_object(config_options[config_name])

    #initalize flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)


    # #config uploadset
    # configure_uploads(app, photos)

    #Registering bluprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    return app
