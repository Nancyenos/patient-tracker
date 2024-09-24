from flask import Blueprint, request, jsonify
from models import Patient, Doctor, db  # Import models as needed

api = Blueprint('api', __name__)

# Get patient records
@api.route('/api/patient/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = Patient.query.get(patient_id)
    if patient:
        return jsonify({
            'id': patient.id,
            'name': patient.name,
            'disease': patient.disease,
            'last_visit': patient.last_visit,
        }), 200
    else:
        return jsonify({'message': 'Patient not found'}), 404

# Create a new patient record
@api.route('/api/patient', methods=['POST'])
def create_patient():
    data = request.get_json()
    new_patient = Patient(
        name=data['name'],
        disease=data['disease'],
        last_visit=data['last_visit']
    )
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({'message': 'New patient created'}), 201

# Get doctor details
@api.route('/api/doctor/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    doctor = Doctor.query.get(doctor_id)
    if doctor:
        return jsonify({
            'id': doctor.id,
            'name': doctor.name,
            'specialization': doctor.specialization,
        }), 200
    else:
        return jsonify({'message': 'Doctor not found'}), 404

# Update patient details
@api.route('/api/patient/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    data = request.get_json()
    patient = Patient.query.get(patient_id)
    if patient:
        patient.name = data['name']
        patient.disease = data['disease']
        patient.last_visit = data['last_visit']
        db.session.commit()
        return jsonify({'message': 'Patient updated'}), 200
    else:
        return jsonify({'message': 'Patient not found'}), 404
