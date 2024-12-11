import digitalio
import board
import adafruit_character_lcd.character_lcd as characterlcd

class LCD:
    def __init__(self, rs, e, d4, d5, d6, d7, columns=16, rows=2):
        """
        Initialize the LCD.
        :param rs: Register Select GPIO pin number
        :param e: Enable GPIO pin number
        :param d4: Data pin 4 GPIO pin number
        :param d5: Data pin 5 GPIO pin number
        :param d6: Data pin 6 GPIO pin number
        :param d7: Data pin 7 GPIO pin number
        :param columns: Number of columns on the LCD (default: 16)
        :param rows: Number of rows on the LCD (default: 2)
        """
        # self.lcd_rs = rs
        # self.lcd_e = e
        # self.lcd_d4 = d4
        # self.lcd_d5 = d5
        # self.lcd_d6 = d6
        # self.lcd_d7 = d7
        
        # Use digitalio to initialize the pins as GPIO objects
        self.lcd_rs = digitalio.DigitalInOut(getattr(board, f'D{rs}'))
        self.lcd_e = digitalio.DigitalInOut(getattr(board, f'D{e}'))
        self.lcd_d4 = digitalio.DigitalInOut(getattr(board, f'D{d4}'))
        self.lcd_d5 = digitalio.DigitalInOut(getattr(board, f'D{d5}'))
        self.lcd_d6 = digitalio.DigitalInOut(getattr(board, f'D{d6}'))
        self.lcd_d7 = digitalio.DigitalInOut(getattr(board, f'D{d7}'))

        # Set the pin directions
        self.lcd_rs.direction = digitalio.Direction.OUTPUT
        self.lcd_e.direction = digitalio.Direction.OUTPUT
        self.lcd_d4.direction = digitalio.Direction.OUTPUT
        self.lcd_d5.direction = digitalio.Direction.OUTPUT
        self.lcd_d6.direction = digitalio.Direction.OUTPUT
        self.lcd_d7.direction = digitalio.Direction.OUTPUT

        # Initialize the LCD display
        self.lcd = characterlcd.Character_LCD_Mono(
            self.lcd_rs, self.lcd_e, self.lcd_d4, self.lcd_d5, self.lcd_d6, self.lcd_d7,
            columns, rows
        )
        print("LCD initialized successfully.")

    def display_text(self, text, line=0):
        """
        Display text on the LCD.
        :param text: Text to display (max 16).
        :param line: Line number (0 or 1)
        """
        if line not in (0, 1):
            raise ValueError("Line number must be 0 or 1.")

        if line == 1:
            text = "\n" + text  # Add newline for the second line

        self.lcd.message = text[:16]  # Limit to 16 characters per line
        print(f"Displayed on line {line}: {text[:16]}")

    def clear(self):
        self.lcd.clear()

    def cleanup(self):
        self.clear()  # Clear the display
        del self.lcd  # Delete LCD object to clean up resources
