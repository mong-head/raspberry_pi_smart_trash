import RPi.GPIO as GPIO

class IRSensor:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN)  # Set the GPIO pin as input

    def is_detected(self):
        """
        Checks if the IR sensor detects an object.
        :return: True if an object is detected.
        """
        if GPIO.input(self.pin) == GPIO.LOW:  # LOW means object detected
            return True
        else:
            return False

    def cleanup(self):
        GPIO.cleanup()