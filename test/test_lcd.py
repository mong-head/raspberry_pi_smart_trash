import time
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from modules import LCD
from config import GPIO_CONSTANT

def test_lcd():
    lcd = None
    try:
        # Initialize LCD with GPIO pins
        lcd = LCD(rs=GPIO_CONSTANT.LCD_RS, e=GPIO_CONSTANT.LCD_E, d4=GPIO_CONSTANT.LCD_D4, d5=GPIO_CONSTANT.LCD_D5, d6=GPIO_CONSTANT.LCD_D6, d7=GPIO_CONSTANT.LCD_D7)

        # Display text on the first line
        lcd.display_text("Hello, World!", line=0)
        time.sleep(2)

        # Display text on the second line
        lcd.display_text("Raspberry Pi", line=1)
        time.sleep(2)

        # Clear the display
        lcd.clear()
        time.sleep(1)

        # Display text alternately
        for i in range(3):
            lcd.display_text("Testing Line 1", line=0)
            time.sleep(1)
            lcd.display_text("Testing Line 2", line=1)
            time.sleep(1)
            lcd.clear()

    except KeyboardInterrupt:
        print("Test interrupted by user.")

    finally:
        lcd.cleanup()

if __name__ == "__main__":
    test_lcd()
