import cv2
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('../models/tire_detection_model.h5')

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (128, 128))
    image = np.expand_dims(image, axis=0)
    return image

def predict(image_path):
    image = preprocess_image(image_path)
    predictions = model.predict(image)
    return np.argmax(predictions, axis=1)[0]

if __name__ == "__main__":
    image_path = '../data/raw/example_tire.jpg'
    prediction = predict(image_path)
    print(f"Predicted class: {prediction}")
