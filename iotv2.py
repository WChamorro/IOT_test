#!/usr/bin/python
# -*- coding: utf-8 -*-
# autor: Jefferson Rivera
# Abril de 2018
# email: riverajefer@gmail.com

import sys
from builtins import print
from time import sleep
import signal
import asyncio
#from gpiozero import LED, Button
from threading import Thread
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from kasa import SmartPlug

PAHT_CRED = '/home/william/PycharmProjects/smartPlug/iotv2-51d58-firebase-adminsdk-qqxyo-ddc8658b28.json'

URL_DB = 'https://iotv2-51d58-default-rtdb.firebaseio.com'
DB_INPUTS  = "entradas"
DB_OUTPUTS = "salidas"
DB_NAME    = "iot_test"
IN1_NAME    = "pulsador"
OUT1_NAME    = "led"



class IOT():

    def __init__(self):
        cred = credentials.Certificate(PAHT_CRED)  #path to json file
        firebase_admin.initialize_app(cred, {'databaseURL': URL_DB}) # database url


        #variables para el arbol de entradas / salidas
        self.dbname = db.reference(DB_INPUTS)
        self.dbinputs = self.dbname.child(DB_INPUTS)
        self.dboutputs =self.dbname.child(DB_OUTPUTS)
        self.led_a = self.dboutputs.child(OUT1_NAME)
        self.pulse_a = self.dbinputs.child(IN1_NAME)

        #funcion para definit la estructura del arbol
        self.estructuraInicialDB()
        print("created IOT object")


    def estructuraInicialDB(self):
        self.dbname.set({
            'entradas': {
                'pulsador':True,
            },
            'salidas':{
                'led':True,
            }
        })
        print("configured DB structure")

    def ledControlGPIO(self, estado):
        if estado:
            print("LED ON")


        else:
            print("LED OFF")


    def checkOutputsDB(self):
        estado_actual = self.led_a.get()
        #self.ledControlGPIO(estado_actual)
        return estado_actual

    def pulse_on(self):
        print("pulsador on")
        self.pulse_a.set(True)

    def pulse_off(self):
        print("pulsador off")
        self.pulse_a.set(False)

async  def mainLoop():
    iot = IOT()

    dev=SmartPlug("192.168.0.30")
    await dev.update()
    print("IOT smart plug name: "+dev.alias)
    state_prev = False
    while True:
        state = iot.checkOutputsDB()
        if state_prev != state:

            if state == True:
                await dev.update()
                await dev.turn_on()
                print("PLUG ON")
            else:
                await dev.update()
                await dev.turn_off()
                print("PLUG OFF")

        state_prev = state
        iot.pulse_on()
        await asyncio.sleep(1)
        iot.pulse_off()
        await asyncio.sleep(1)



if __name__=="__main__":
    asyncio.run(mainLoop())













