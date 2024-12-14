import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from classifiers import GarbageClassifier

def test():
    try:
        garbage_classifier = GarbageClassifier()
        # Test with an image
        test_image = "/home/user/project/test/test_image/plastic_002.jpg"
        result = garbage_classifier.classify_garbage(test_image)
        print("Classified:", result["class"])
        print("Probability:", result["probability"])

    except KeyboardInterrupt:
        print("Test interrupted by user.")

if __name__ == "__main__":
    test()
