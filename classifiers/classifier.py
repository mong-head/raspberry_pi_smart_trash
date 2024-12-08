import tflite_runtime.interpreter as tflite
from PIL import Image
import numpy as np

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
        img = Image.open(image_path).convert('RGB')
        img = img.resize(target_size, Image.ANTIALIAS)
        img_array = np.array(img, dtype=np.uint8) / 255.0  # Normalize to [0, 1]
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
