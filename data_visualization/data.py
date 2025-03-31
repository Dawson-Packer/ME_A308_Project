import time

import serial
from gui import TankLevelRegulatorGui

def get_data(app: TankLevelRegulatorGui):
    while app.is_running:
        ...