# module/servo.py
import RPi.GPIO as GPIO
import time
import sys
import os
import pigpio # https://luigibox.tistory.com/entry/%EB%9D%BC%EC%A6%88%EB%B2%A0%EB%A6%AC%ED%8C%8C%EC%9D%B44-%EC%84%9C%EB%B3%B4%EB%AA%A8%ED%84%B0-SG-90-%EB%96%A8%EB%A6%BC%ED%9D%94%EB%93%A4%EB%A6%BC-jittershaking-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%95%B4%EA%B2%B0-GPIO%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

class Servo:
    def __init__(self, pin, min_angle=0, max_angle=180, freq=50, start_angle=0, end_angle=0):
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
        self.start_angle = start_angle
        self.end_angle = end_angle
        self.current_angle = -1
        self.pi = pigpio.pi()

        # Set up GPIO mode
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

        # Set up PWM with the specified frequency
        self.pi.set_PWM_frequency(self.pin, self.freq)
        self.move_to_angle(self.start_angle);
        # self.pwm = GPIO.PWM(self.pin, self.freq)
        # self.pwm.start(self.start_angle)  # Start PWM with 0% duty cycle (servo at 0 degrees)
    def angle_to_duty_cycle(self, angle):
        """Convert an angle to PWM duty cycle.
        
        Args:
            angle (int): The angle to be converted (0-180 degrees).
        
        Returns:
            float: Corresponding duty cycle for the given angle.
        """
        return (angle / 18) + 2
    
    def angle_to_pig_piod_angle(self, angle):
        pig_piod_angle = 11.11 * (angle - 4) + 500
        if pig_piod_angle > 2500 :
            return 2500
        if pig_piod_angle < 500 : 
            return 500
        return pig_piod_angle

    def move_to_angle(self, angle):
        if angle == self.current_angle:
            return
        if self.min_angle <= angle <= self.max_angle:
            # duty_cycle = self.angle_to_duty_cycle(angle)
            # self.pwm.ChangeDutyCycle(duty_cycle)
            self.pi.set_servo_pulsewidth(self.pin, self.angle_to_pig_piod_angle(angle)) 
            self.current_angle = angle
            print(f"Servo moving to {angle} degrees.")
            time.sleep(1)  # Wait for the servo to reach the position
        else:
            print(f"Angle {angle} is out of range! Please specify an angle between {self.min_angle} and {self.max_angle}.")

    def sweep(self):
        """Sweep the servo from min angle to max angle degrees and back."""
        for angle in range(self.min_angle, self.max_angle + 1, 10):  # Sweep forward
            self.move_to_angle(angle)
        for angle in range(self.max_angle, self.min_angle - 1, -10):  # Sweep backward
            self.move_to_angle(angle)

    def cleanup(self):
        self.move_to_angle(self.end_angle)
        self.pi.set_servo_pulsewidth(self.pin, 0)
        # self.pwm.stop()
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
