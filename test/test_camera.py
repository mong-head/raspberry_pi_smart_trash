# test/test_camera.py
import time
import cv2
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module import Camera

def test_camera():
    # Initialize the camera (default index 0)
    camera = Camera(0)
    time.sleep(2)  # Wait for camera to initialize

    if camera.cap is None:
        print("Camera not initialized. Exiting test.")
        return

    try:
        print("Camera initialized successfully. Taking photos every 3 seconds...")
        
        # Take photos every 3 seconds for 15 seconds (for example)
        for i in range(5):
            frame = camera.capture_frame()  # Capture a frame
            if frame is not None:
                filename = f"photo_{i + 1}.jpg"
                cv2.imwrite(filename, frame)  # Save the captured frame
                print(f"Photo {i + 1} saved as {filename}")
            else:
                print("Failed to capture frame.")
            time.sleep(3)  # Wait for 3 seconds before taking the next photo

    except KeyboardInterrupt:
        print("Test interrupted by user.")
    finally:
        # Clean up the camera after the test
        camera.cleanup()
        print("Camera cleaned up.")

if __name__ == "__main__":
    test_camera()
