from flask import Flask
from flask_migrate import Migrate
from models import db
from mail import mail
from routes.heroes import heroes_bp
from routes.powers import powers_bp
from routes.hero_powers import hero_powers_bp

app = Flask(__name__)

# DB Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Email Config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'bismarckkip684@gmail.com'
app.config['MAIL_PASSWORD'] = 'sgwn xwyf ccce dzvc'
app.config['MAIL_DEFAULT_SENDER'] = 'bismarckkip684@gmail.com'

# Initialize extensions
db.init_app(app)
mail.init_app(app)
migrate = Migrate(app, db)

# Register blueprints
app.register_blueprint(heroes_bp)
app.register_blueprint(powers_bp)
app.register_blueprint(hero_powers_bp)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
