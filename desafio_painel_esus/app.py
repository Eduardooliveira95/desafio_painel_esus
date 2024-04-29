from flask import Flask
from pony.flask import Pony
from pony.orm import Database
from config import Config
db = Database()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Pony(app)
    db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

    from controladores.ControladoraConsulta import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/api/v1')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8001)


