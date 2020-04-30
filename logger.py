##############################################################
# Brian Ma
# AC Logger: Synchronized datalogging w/ frame capture for
#            use with neural network training
#
# To activate create a folder with the same name as this file
# in apps/python. Ex apps/python/tutorial01
# Then copy this file inside it and launch AC
##############################################################

import sys
import ac
import acsys

from lib.car_g import GReadout
from lib.car_speed import SpeedReadout

appWindow = 0
car_g = 0
car_speed = 0

def acMain(ac_version):
    global appWindow, car_g, car_speed

    # Start new application in session
    appWindow = ac.newApp("SyncLogger")
    ac.setSize(appWindow, 200, 100)
    
    # Print initial log confirmation
    ac.log("SyncLogger says hi!")
    ac.console("SyncLogger says hi!")
    
    # Init individual readouts
    car_g = GReadout(appWindow, 3, 30)
    car_speed = SpeedReadout(appWindow, 3, 45)
    
    return "SyncLogger"

def acUpdate(deltaT):
    global car_g, car_speed
    
    car_g.update()
    car_speed.update()