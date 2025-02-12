from tensorflow import keras
from data_loader import val_ds

# Load the model
model = keras.saving.load_model("models/model.keras")

print('Model loaded!')

# Evaluate the model
model.evaluate(val_ds)
