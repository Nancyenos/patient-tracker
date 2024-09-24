from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes import api
from flask_login import LoginManager
from models import db, User

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
# Register the API routes from routes.py
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)
