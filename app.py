from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes import api

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Register the API routes from routes.py
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)
