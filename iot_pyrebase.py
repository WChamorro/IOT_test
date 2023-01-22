#!/usr/bin/python
# -*- coding: utf-8 -*-
# autor: William Chamorro


import sys
import time
from time import sleep
import signal
from gpiozero import LED, Button
import pyrebase

config = {
  "apiKey": "",
  "authDomain": "iotv2-51d58.firebaseapp.com",
  "databaseURL": "https://iotv2-51d58-default-rtdb.firebaseio.com/",
  "storageBucket": "iotv2-51d58.appspot.com"
}


class IOT():

    def __init__(self,db):
        self.db = db
        self.estructuraDB()

    def estructuraDB(self):
        self.db.child("devices").child("entradas").child("led_a").set(True)
        self.db.child("devices").child("entradas").child("led_b").set(True)
        self.db.child("devices").child("salidas").child("pulsador_a").set(True)
        self.db.child("devices").child("salidas").child("pulsador_b").set(True)

    def checkDB(self):
        data = {}
        data["led_a"] = self.db.child("devices").child("entradas").child("led_a").get().val()
        data["led_b"] = self.db.child("devices").child("entradas").child("led_b").get().val()
        return data

    def setDB(self,data):
        for k,v in data.items():
            self.db.child("devices").child("salidas").child(k).set(v)







if __name__=="__main__":
    my_firebase = pyrebase.initialize_app(config)
    db = my_firebase.database()
    iot = IOT(db)

    while True:
        entradas = iot.checkDB()
        for k,v in entradas.items():
             print(k)
             print(v)

        buttoms={}
        buttoms["pulsador_a"]=False
        buttoms["pulsador_b"]=True
        iot.setDB(buttoms)

        time.sleep(1)

