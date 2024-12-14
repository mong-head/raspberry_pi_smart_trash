# camera.py
import cv2
import numpy as np

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
    
    def crop_and_resize_with_padding(self, frame, x, y, w, h, output_size=(244, 244)):
        """
        Crop the given frame, resize to the specified size, and pad with white.
        :param frame: The frame to crop
        :param x: The x-coordinate of the top-left corner
        :param y: The y-coordinate of the top-left corner
        :param w: The width of the crop
        :param h: The height of the crop
        :param output_size: The target size (width, height)
        :return: The padded frame resized to the target size
        """
        if frame is None:
            print("No frame to process.")
            return None

        # Crop the frame
        cropped_frame = frame[y:y+h, x:x+w]

        # Get the aspect ratio of the cropped image
        crop_h, crop_w = cropped_frame.shape[:2]
        aspect_ratio = crop_w / crop_h

        # Calculate padding for resizing to the output size
        target_w, target_h = output_size
        if aspect_ratio > 1:  # Width is greater than height
            scale = target_w / crop_w
            new_w = target_w
            new_h = int(crop_h * scale)
        else:  # Height is greater than or equal to width
            scale = target_h / crop_h
            new_w = int(crop_w * scale)
            new_h = target_h

        # Resize the cropped frame
        resized_frame = cv2.resize(cropped_frame, (new_w, new_h), interpolation=cv2.INTER_AREA)

        # Create a blank white image with the target size
        padded_frame = np.ones((target_h, target_w, 3), dtype=np.uint8) * 255

        # Center the resized image on the white background
        x_offset = (target_w - new_w) // 2
        y_offset = (target_h - new_h) // 2
        padded_frame[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = resized_frame

        return padded_frame

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
