from flask import Flask
import json
import urllib3

def create_app():
    app = Flask(__name__)

    with open('/etc/config.json') as config_file:
        config = json.load(config_file)

    app.config['SECRET_KEY'] = config.get('SECRET_KEY')
    

    from .views import views, electronics
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(electronics, url_prefix="/electronics/")
    app.register_blueprint(auth, url_prefix="/auth/")

    return app
    
app = create_app()