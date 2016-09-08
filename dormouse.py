#!/usr/bin/python 

# Dormouse v1 by Mandrake Fernflower, 2016
# Free to use and modify - just leave this message intact
# Made for a RPI3 with a SenseHat
import os
import time
from sense_hat import SenseHat

sensebrd = SenseHat()
sensebrd.low_light = True
sensebrd.rotation = 180

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

while True:
   sensebrd.clear()
   sensebrd.show_message("CPU " + getCPUtemperature() + "C", text_colour=[0, 148, 200])
   time.sleep(8)
   etempraw = sensebrd.get_temperature_from_humidity()
   etemp = round(etempraw, 1)
   sensebrd.show_message("EXT " + str(etemp) + "C", text_colour=[240, 230, 140])
   time.sleep(8)
   rhraw = sensebrd.get_humidity()
   rh = round(rhraw, 1)
   sensebrd.show_message("RH % " + str(rh), text_colour=[0, 128, 0])
   time.sleep(30)
