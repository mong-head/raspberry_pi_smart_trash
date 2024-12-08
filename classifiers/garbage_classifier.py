import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from classifiers import Classifier

"""
Specialized classifier for garbage classification tasks.
"""
class GarbageClassifier(Classifier):
   
    def __init__(self):
        self.model_path = "/home/user/project/models/garbage_classifcation_model.tflite"
        self.class_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']
        super().__init__(self.model_path)

    def classify_garbage(self, image_path, target_size=(32, 32)):
        """
        Classify the type of garbage in the given image.

        Args:
            image_path (str): Path to the image to classify.
            target_size (tuple): Size to resize the image for the model input.

        Returns:
            dict: A dictionary containing the predicted class and its probability.
        """
        prediction, probability = self.predict(image_path, target_size)
        predicted_class = self.class_names[prediction]
        return {
            "class": predicted_class,
            "probability": probability
        }
