import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('/home/william/PycharmProjects/smartPlug/iotv2-51d58-firebase-adminsdk-qqxyo-e7bfe743f8.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iotv2-51d58-default-rtdb.firebaseio.com'
})

ref = db.reference('message')

print(ref.get())

print ('Ok !')
