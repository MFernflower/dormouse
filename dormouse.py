# Dormouse by Mandrake Fernflower, 2016
# Free to use and modify - just leave this message intact
# Made for a RPI3 with a SenseHat
# todo: add support for psutil
import os
import time
from sense_hat import SenseHat
cyan = (0, 148, 255)
purple = (238, 130, 238)
yellow  = (240, 230, 140)
sensebrd = SenseHat()
sensebrd.low_light = True

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

while True:
   sensebrd.clear()
   sensebrd.show_message("CPU " + getCPUtemperature() + "C", text_colour=cyan)
   time.sleep(8)
   sensebrd.clear()
   etempraw = sensebrd.get_temperature_from_humidity()
   etemp = round(etempraw, 1)
   sensebrd.show_message("EXT " + str(etemp) + "C", text_colour=yellow)
   time.sleep(8)
   sensebrd.clear()
   rhraw = sensebrd.get_humidity()
   rh = round(rhraw, 1)
   sensebrd.show_message("RH % " + str(rh), text_colour=purple)
   sensebrd.clear()
   time.sleep(30)
