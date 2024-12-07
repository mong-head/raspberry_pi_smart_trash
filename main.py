# main.py
from module import Camera, Switch, Servo, IRSensor
from config import GPIO_CONSTANT
import time

def main():
    # GPIO setup
    camera_index = 0  # Index for the USB camera
    
    # parameter
    

    try:
        # Initialize
        camera = Camera(camera_index)
        switch = Switch(GPIO_CONSTANT.PUSH_BUTTON)
        servoMotor = Servo(GPIO_CONSTANT.SERVO_MORTOR)
        irSensor = IRSensor(GPIO_CONSTANT.IR_SENSOR)

        print("Press the switch to capture an image. Press Ctrl+C to exit.")

        while True:
            # Check if the switch is pressed
            if switch.is_pressed():
                print("Switch pressed. Capturing image...")
                frame = camera.capture_frame()

                if frame is not None:
                    camera.save_image(frame, filename='/home/user/Pictures/capture.jpg')
                else:
                    print("No frame captured.")
            if irSensor.is_detected():
                servoMotor.move_to_angle(180)
            else:
                servoMotor.move_to_angle(0)
            time.sleep(0.1)  # Small delay to prevent CPU overload

    except KeyboardInterrupt:
        print("Program terminated by user.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Clean up resources
        if 'camera' in locals():
            camera.cleanup()
        if 'switch' in locals():
            switch.cleanup()
        if 'servoMotor' in locals():
            servoMotor.cleanup()
        if 'irSensor' in locals():
            irSensor.cleanup()

if __name__ == "__main__":
    main()
