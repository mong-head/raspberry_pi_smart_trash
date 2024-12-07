# module/servo.py
import RPi.GPIO as GPIO
import time
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from config import GPIO_CONSTANT

class Servo:
    def __init__(self, pin, min_angle=0, max_angle=180, freq=50):
        """Initialize the Servo motor.
        
        Args:
            pin (int): The GPIO pin to which the servo is connected.
            min_angle (int): The minimum angle the servo can move to (default 0).
            max_angle (int): The maximum angle the servo can move to (default 180).
            freq (int): The PWM frequency for the servo (default 50 Hz).
        """
        self.pin = pin
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.freq = freq

        # Set up GPIO mode
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

        # Set up PWM with the specified frequency
        self.pwm = GPIO.PWM(self.pin, self.freq)
        self.pwm.start(0)  # Start PWM with 0% duty cycle (servo at 0 degrees)

    def angle_to_duty_cycle(self, angle):
        """Convert an angle to PWM duty cycle.
        
        Args:
            angle (int): The angle to be converted (0-180 degrees).
        
        Returns:
            float: Corresponding duty cycle for the given angle.
        """
        return (angle / 18) + 2

    def move_to_angle(self, angle):
        """Move the servo to a specific angle.
        
        Args:
            angle (int): The target angle (0-180 degrees).
        """
        if self.min_angle <= angle <= self.max_angle:
            duty_cycle = self.angle_to_duty_cycle(angle)
            self.pwm.ChangeDutyCycle(duty_cycle)
            print(f"Servo moving to {angle} degrees.")
            time.sleep(1)  # Wait for the servo to reach the position
        else:
            print(f"Angle {angle} is out of range! Please specify an angle between {self.min_angle} and {self.max_angle}.")

    def sweep(self):
        """Sweep the servo from 0 to 180 degrees and back."""
        for angle in range(self.min_angle, self.max_angle + 1, 10):  # Sweep forward
            self.move_to_angle(angle)
        for angle in range(self.max_angle, self.min_angle - 1, -10):  # Sweep backward
            self.move_to_angle(angle)

    def cleanup(self):
        """Stop PWM and clean up GPIO settings."""
        self.pwm.stop()
        GPIO.cleanup()

# if __name__ == "__main__":
#     # Example usage
#     servo = Servo(pin=GPIO_CONSTANT.SERVO_MORTOR)  # Connect servo to GPIO pin
#     try:
#         servo.move_to_angle(90)  # Move servo to 90 degrees
#         time.sleep(2)
#         servo.sweep()  # Sweep the servo from 0 to 180 degrees and back
#     except KeyboardInterrupt:
#         print("Test interrupted by user.")
#     finally:
#         servo.cleanup()  # Cleanup GPIO settings when done
