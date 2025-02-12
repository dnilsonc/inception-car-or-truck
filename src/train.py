import tf_keras 
import tensorflow_hub as hub

from data_loader import train_ds, val_ds

# Load the pretrained model
pretrained_base = hub.KerasLayer("https://www.kaggle.com/models/google/inception-v1/TensorFlow2/classification/2", trainable=False)

# Build the model
model = tf_keras.models.Sequential([
    pretrained_base,
    tf_keras.layers.Dense(6, activation='relu'),
    tf_keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(train_ds, validation_data=val_ds, epochs=1)

# Save the model
model.save("models/model.keras")

if __name__ == '__main__':
    print('Done!')