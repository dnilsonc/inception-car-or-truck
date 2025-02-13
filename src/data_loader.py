import kagglehub
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory

path = kagglehub.dataset_download("ryanholbrook/car-or-truck")

# Load the data
ds_train_ = image_dataset_from_directory(
    path + '/train', 
    labels='inferred',
    label_mode='binary',
    image_size=[128, 128],
    interpolation='nearest',
    batch_size=64,
    shuffle=True,
)

ds_val_ = image_dataset_from_directory(
    path + '/valid', 
    labels='inferred',
    label_mode='binary',
    image_size=[128, 128],
    interpolation='nearest',
    batch_size=64,
    shuffle=False,
)

# Data Pipeline
def convert_to_float(image, label):
    return tf.image.convert_image_dtype(image, tf.float32), label

train_ds = ds_train_.map(convert_to_float)
val_ds = ds_val_.map(convert_to_float)

if __name__ == '__main__':
    print('Done!')