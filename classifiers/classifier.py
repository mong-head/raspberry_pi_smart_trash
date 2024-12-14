import tflite_runtime.interpreter as tflite
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

class Classifier:
    """
    General TFLite Classifier for image-based tasks.
    """
    def __init__(self, model_path):
        """
        Initialize the classifier with a TFLite model.

        Args:
            model_path (str): Path to the TFLite model file.
        """
        self.interpreter = tflite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

    def preprocess_image(self, image_path, target_size):
        """
        Load and preprocess an image for classification.

        Args:
            image_path (str): Path to the image file.
            target_size (tuple): Target size for resizing the image.

        Returns:
            numpy.ndarray: Preprocessed image as a numpy array.
        """
        img = cv2.imread(image_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, target_size, interpolation=cv2.INTER_AREA)
        plt.imshow(img)
        plt.axis('off')
        plt.show()
        # time.sleep(1)
        plt.close('all')
        img_array = np.array(img, dtype=np.uint8)  # Normalize to [0, 1]
        return img_array[np.newaxis, ...].astype(np.float32)

    def predict(self, image_path, target_size):
        """
        Run inference on the given image.

        Args:
            image_path (str): Path to the image file.
            target_size (tuple): Target size for resizing the image.

        Returns:
            tuple: Predicted class index and probability.
        """
        input_data = self.preprocess_image(image_path, target_size)
        self.interpreter.set_tensor(self.input_details[0]['index'], input_data)
        self.interpreter.invoke()
        prediction = self.interpreter.get_tensor(self.output_details[0]['index'])[0]
        return np.argmax(prediction), np.max(prediction)
