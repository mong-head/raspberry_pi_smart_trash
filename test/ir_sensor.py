import time
import RPi.GPIO as GPIO
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module import IRSensor
from config import GPIO_CONSTANT

def test_ir_receiver():
    GPIO.setmode(GPIO.BCM)
    
    ir_sensor = IRSensor(pin=GPIO_CONSTANT.IR_SENSOR)  
    
    try:
        print("Testing IR receiver for object detection...")
        while True:
            if ir_sensor.is_detected():  
                print("Object detected!")
            else:
                print("No object detected.")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Test interrupted by user.")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    test_ir_receiver()
