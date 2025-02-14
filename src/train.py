import tf_keras
import tensorflow_hub as hub

from data_loader import train_ds, val_ds

# Load the pretrained model    
pretrained_base = hub.KerasLayer("https://www.kaggle.com/models/google/inception-v1/TensorFlow2/classification/2", trainable=False)

# Build the model
model = tf_keras.models.Sequential([
    pretrained_base,
    tf_keras.layers.Flatten(),
    tf_keras.layers.Dense(6, activation='relu'),
    tf_keras.layers.Dense(6, activation='relu'),
    tf_keras.layers.Dense(6, activation='relu'),
    tf_keras.layers.Dropout(0.2),
    tf_keras.layers.Dense(1, activation='sigmoid')
])
# Compilar o modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Treinamento do modelo
history = model.fit(train_ds, validation_data=val_ds, epochs=30) # Ajuste o número de épocas conforme necessário

# Salvar o modelo treinado
model.save('models/model.keras', save_format='tf')  # Salvar o modelo em formato TensorFlow

# Confirmar que o processo foi concluído FIX
if __name__ == '__main__':
    print('Modelo treinado e salvo com sucesso!')
