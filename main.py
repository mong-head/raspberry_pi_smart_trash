# main.py
from modules import Camera, Switch, Servo, IRSensor, LCD
from classifiers import GarbageClassifier
from config import GPIO_CONSTANT
import time
import cv2

def main():
    # GPIO setup
    camera_index = 0  # Index for the USB camera
    
    #parameter
    is_detected = False
    try:
        # Initialize
        camera = Camera(camera_index)
        switch = Switch(GPIO_CONSTANT.PUSH_BUTTON)
        servoMotor = Servo(pin = GPIO_CONSTANT.SERVO_MORTOR, start_angle=90, end_angle=90)
        irSensor = IRSensor(GPIO_CONSTANT.IR_SENSOR)
        lcd = LCD(rs=GPIO_CONSTANT.LCD_RS, e=GPIO_CONSTANT.LCD_E, d4=GPIO_CONSTANT.LCD_D4, d5=GPIO_CONSTANT.LCD_D5, d6=GPIO_CONSTANT.LCD_D6, d7=GPIO_CONSTANT.LCD_D7)
        garbageClassifier = GarbageClassifier()

        print("Press the switch to capture an image. Press Ctrl+C to exit.")

        while True:
            # Check if the switch is pressed
            if irSensor.is_detected() or switch.is_pressed():
                time.sleep(1)
                frame = camera.capture_frame()
                is_detected = True
                if frame is not None:
                    cv2.imshow('USB Camera', frame)
                    imagePath = '/home/user/Pictures/capture.jpg'
                    camera.save_image(frame, filename=imagePath)
                    garbageClassResult = garbageClassifier.classify_garbage(imagePath)
                    print("Classified:", garbageClassResult["class"])
                    print("Probability:", garbageClassResult["probability"])
                    lcd.display_text(text=garbageClassResult["class"], line=0)
                    if garbageClassResult["class"] in ['cardboard', 'glass', 'metal', 'plastic'] :
                        servoMotor.move_to_angle(150)
                    else : 
                        servoMotor.move_to_angle(30)
                else:
                    print("No frame captured.")
            else:
                if is_detected == True :
                    servoMotor.move_to_angle(90)
                    lcd.clear()
                    cv2.destroyAllWindows()
                    is_detected = False
            time.sleep(1)  # Small delay to prevent CPU overload

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
        if 'lcd' in locals():
            lcd.cleanup()

if __name__ == "__main__":
    main()
