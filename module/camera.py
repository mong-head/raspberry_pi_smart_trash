# camera.py
import cv2

class Camera:
    def __init__(self, camera_index=0):
        """
        Initialize the camera.
        :param camera_index: Index of the camera to use (default: 0)
        """
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(camera_index)
        if not self.cap.isOpened():
            raise Exception(f"Unable to open camera {camera_index}")
        print(f"Camera {camera_index} initialized successfully.")

    def capture_frame(self):
        """
        Capture a single frame from the camera.
        :return: The captured frame (numpy array) or None
        """
        ret, frame = self.cap.read()
        if not ret:
            print("Failed to capture frame.")
            return None
        return frame

    def save_image(self, frame, filename='capture.jpg'):
        """
        Save the captured frame to a file.
        :param frame: The frame to save
        :param filename: The file name to save the frame as
        """
        if frame is not None:
            cv2.imwrite(filename, frame)
            print(f"Image saved as {filename}.")
        else:
            print("No frame to save.")

    def cleanup(self):
        """
        Release camera resources and close any open windows.
        """
        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()
        print("Camera resources released.")
