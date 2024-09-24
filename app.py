from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
db = SQLAlchemy(app)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    disease = db.Column(db.String(100), nullable=False)
    last_visit = db.Column(db.String(100), nullable=False)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    return "Welcome to the Patient Tracker Application"

with app.app_context():
    db.create_all()  # This will create the tables within the application context

@app.route('/add_test_data')
def add_test_data():
    # Adding test patients
    patient1 = Patient(name="John Doe", age=30, disease="Flu", last_visit="2024-09-16")
    patient2 = Patient(name="Jane Smith", age=25, disease="Asthma", last_visit="2024-09-10")
    db.session.add(patient1)
    db.session.add(patient2)

    # Adding test doctors
    doctor1 = Doctor(name="Dr. Strange", specialty="Cardiology")
    db.session.add(doctor1)

    db.session.commit()
    return "Test data added"

if __name__ == '__main__':
    app.run(debug=True)

