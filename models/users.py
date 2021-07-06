from tcm_project import db


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), unique=False, nullable=False)
    last_name = db.Column(db.String(255), unique=False, nullable=False)
    date_of_birth = db.Column(db.String(255), unique=False, nullable=False)
    address = db.Column(db.String(255), unique=False, nullable=False)
    phone_number = db.Column(db.String(255), unique=False, nullable=False)
    gender = db.Column(db.String(255), unique=False, nullable=False)
    role_name = db.Column(db.String(255), unique=False, nullable=False)
    is_active = db.Column(db.Integer, unique=False, nullable=True)

    def __init__(self, user_id, first_name, last_name, date_of_birth, address, phone_number, gender, role_name, is_active):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone_number = phone_number
        self.gender = gender
        self.role_name = role_name
        self.is_active = is_active

    def to_json2(self):
        return {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_of_birth': self.date_of_birth,
            'address': self.address,
            'phone_number': self.phone_number,
            'gender': self.gender,
            'role_name': self.role_name,
            'is_active': self.is_active
        }

    def get_user_information(self):
        return {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_of_birth': self.date_of_birth,
            'address': self.address,
            'phone_number': self.phone_number,
            'gender': self.gender,
        }


class Doctors(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    doctor_id = db.Column(db.Integer, primary_key=True)

    def __init__(self, user_id, doctor_id):
        self.user_id = user_id
        self.doctor_id = doctor_id

    def to_json2(self):
        return {
            'user_id': self.user_id,
            'doctor_id': self.doctor_id
        }


class Patients(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    patient_id = db.Column(db.Integer, primary_key=True)

    def __init__(self, user_id, patient_id):
        self.user_id = user_id
        self.patient_id = patient_id

    def to_json2(self):
        return {
            'user_id': self.user_id,
            'patient_id': self.patient_id
        }
