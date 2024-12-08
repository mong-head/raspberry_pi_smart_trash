# switch.py
import RPi.GPIO as GPIO
import time

class Switch:
    def __init__(self, pin, debounce_time=0.1):
        """
        Initialize the switch.
        :param pin: GPIO pin number connected to the switch
        :param debounce_time: Debouncing time in seconds (default: 0.1 seconds)
        """
        self.pin = pin
        self.debounce_time = debounce_time

        # Set up GPIO pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print(f"Switch connected to GPIO pin {pin}.")

    def is_pressed(self):
        """
        Check if the switch is pressed.
        :return: True if pressed, False otherwise
        """
        if GPIO.input(self.pin) == GPIO.LOW:  # LOW means the switch is pressed
            time.sleep(self.debounce_time)  # Debounce to avoid multiple triggers
            return GPIO.input(self.pin) == GPIO.LOW
        return False

    def cleanup(self):
        """
        Release GPIO resources for the switch.
        """
        GPIO.cleanup(self.pin)
        print(f"GPIO pin {self.pin} resources released.")
