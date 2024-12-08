# test/test_servo.py
import time
import RPi.GPIO as GPIO
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from modules import Servo
from config import GPIO_CONSTANT

def test_servo():
    # Set up servo on GPIO pin 
    servo = Servo(pin=GPIO_CONSTANT.SERVO_MORTOR, start_angle=0, end_angle=0)

    try:
        # Move servo to 0 degrees
        print("Moving servo to 0 degrees...")
        servo.move_to_angle(0)
        time.sleep(1)

        # Move servo to 90 degrees
        print("Moving servo to 90 degrees...")
        servo.move_to_angle(90)
        time.sleep(1)

        # Move servo to 180 degrees
        print("Moving servo to 180 degrees...")
        servo.move_to_angle(180)
        time.sleep(1)

        # Sweep the servo
        print("Sweeping the servo...")
        servo.sweep()

    except KeyboardInterrupt:
        print("Test interrupted by user.")
    finally:
        servo.cleanup()  # Clean up GPIO settings

if __name__ == "__main__":
    test_servo()
