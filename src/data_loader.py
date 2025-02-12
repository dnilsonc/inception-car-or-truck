import kagglehub
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory

path = kagglehub.dataset_download("ryanholbrook/car-or-truck")

# Load the data
ds_train_ = image_dataset_from_directory(
    path + '/train', 
    image_size=(224, 224), 
    batch_size=32,
    shuffle=True
)

ds_val_ = image_dataset_from_directory(
    path + '/valid', 
    image_size=(224, 224), 
    batch_size=32,
    shuffle=True
)

# Data Pipeline
def convert_to_float(image, label):
    return tf.image.convert_image_dtype(image, tf.float32), label

train_ds = ds_train_.map(convert_to_float)
val_ds = ds_val_.map(convert_to_float)

if __name__ == '__main__':
    print('Done!')