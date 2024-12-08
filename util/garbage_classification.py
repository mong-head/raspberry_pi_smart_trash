import tflite_runtime.interpreter as tflite
from PIL import Image
import numpy as np

def load_image_as_array(image_path, target_size=None):
    """
    Load an image and convert it to a numpy array.
    
    Args:
        image_path (str): Path to the image file.
        target_size (tuple): Desired image size as (width, height).
        
    Returns:
        numpy.ndarray: Image as a numpy array.
    """
    # Open the image file
    img = Image.open(image_path).convert('RGB')  # Convert to RGB to ensure 3 channels
    if target_size:
        img = img.resize(target_size, Image.ANTIALIAS)  # Resize if target_size is provided
    img_array = np.array(img, dtype=np.uint8)  # Convert to numpy array
    return img_array

# Mapping of class numbers to labels
number_to_class = ['cardboard',
                   'glass',
                   'metal',
                   'paper',
                   'plastic',
                   'trash']

# Load the TensorFlow Lite model
interpreter = tflite.Interpreter(model_path='/home/user/project/util/garbage_classifcation_model.tflite')
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Example input images
# test_img = '/home/user/project/util/plastic_002.jpg'
test_img = '/home/user/project/util/paper_005.jpg'
img = load_image_as_array(test_img, target_size=(32,32))
img = np.array(img) / 255.0  # Normalize to range [0, 1]

# # Ensure input shape is correct
input_data = img[np.newaxis, ...].astype(np.float32)

# # Set the input tensor
interpreter.set_tensor(input_details[0]['index'], input_data)

# # Run inference
interpreter.invoke()

# # Get the prediction
prediction = interpreter.get_tensor(output_details[0]['index'])[0]
print("Output:", prediction)

# # Post-process the result
probability = np.max(prediction)
predicted_class = number_to_class[np.argmax(prediction)]
print("Probability:", probability)
print("Classified:", predicted_class, '\n')