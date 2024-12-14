import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from classifiers import Classifier

"""
Specialized classifier for garbage classification tasks.
"""
class GarbageClassifier(Classifier):
   
    def __init__(self):
        train_gen_label_map = {0: 'cardboard', 1: 'glass', 2: 'metal', 3: 'paper', 4: 'plastic', 5: 'trash'}
        self.model_path = "/home/user/project/models/garbage_classifiaction_mobilenetv2.tflite"
        self.class_names = [train_gen_label_map[key] for key in sorted(train_gen_label_map.keys())]
        super().__init__(self.model_path)

    def classify_garbage(self, image_path, target_size=(224, 224)):
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
