import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

def load_and_preprocess_data(data_dir):
    images = []
    labels = []
    for label in os.listdir(data_dir):
        label_dir = os.path.join(data_dir, label)
        for image_file in os.listdir(label_dir):
            image_path = os.path.join(label_dir, image_file)
            image = cv2.imread(image_path)
            image = cv2.resize(image, (128, 128))  # Resize to 128x128
            images.append(image)
            labels.append(label)
    images = np.array(images)
    labels = np.array(labels)
    return train_test_split(images, labels, test_size=0.2, random_state=42)

if __name__ == "__main__":
    data_dir = '../data/raw'
    X_train, X_test, y_train, y_test = load_and_preprocess_data(data_dir)
    print(f"Train data: {len(X_train)}, Test data: {len(X_test)}")
