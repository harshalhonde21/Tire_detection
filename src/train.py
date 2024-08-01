import numpy as np
from data_preprocessing import load_and_preprocess_data
from model import build_model

data_dir = '../data/raw'
X_train, X_test, y_train, y_test = load_and_preprocess_data(data_dir)

model = build_model()
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))
model.save('../models/tire_detection_model.h5')
