# test/test_switch.py
import time
import RPi.GPIO as GPIO
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module import Switch
from config import GPIO_CONSTANT

def test_switch():
    # Configure the GPIO pin
    SWITCH_PIN = 17  # You can change this to the actual pin number
    switch = Switch(pin=GPIO_CONSTANT.PUSH_BUTTON)
    
    try:
        print("Waiting for switch press...")
        while True:
            if switch.is_pressed():
                print("Switch is pressed!")
            else:
                print("Switch is not pressed.")
            time.sleep(0.1)  # Check every 100ms
    except KeyboardInterrupt:
        print("Test interrupted by user.")
    finally:
        GPIO.cleanup()  # Clean up GPIO setup

if __name__ == "__main__":
    test_switch()
