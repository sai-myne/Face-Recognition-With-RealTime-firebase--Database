import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://faceattendancerealtime-b167b-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference('Students')

data = {
    "123456": {
        "name": "Sai None Myne",
        "major": "Electronics & Communication",
        "starting_year": 2015,
        "total_attendance": 6,
        "standing": "G",
        "year": 9,
        "last_attendance_time": "2023-08-13 09:00:00"
    },
    "852741": {
        "name": "Emily Blunt",
        "major": "Economics",
        "starting_year": 2018,
        "total_attendance": 12,
        "standing": "B",
        "year": 5,
        "last_attendance_time": "2023-08-13 09:00:00"
    },
    "963852": {
        "name": "Elon Musk",
        "major": "Physics",
        "starting_year": 2020,
        "total_attendance": 3,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2023-08-15 09:00:00"
    },
    "321654": {
        "name": "Murtaza Hassan",
        "major": "Robotics",
        "starting_year": 2017,
        "total_attendance": 6,
        "standing": "G",
        "year": 6,
        "last_attendance_time": "2023-08-15 09:00:00"
    }
}

for key, value in data.items():
    ref.child(key).set(value)

