import tf_keras
import tensorflow_hub as hub
import numpy as np

from tensorflow.keras.preprocessing import image # type: ignore

# Carregar o modelo salvo
try:
    model = tf_keras.models.load_model('models/model.keras', custom_objects={'KerasLayer': hub.KerasLayer})
    print("Modelo carregado com sucesso!")
except Exception as e:
    print(f"Erro ao carregar o modelo: {e}")
    exit(1)


def preprocess_image(img_path):
    """Carrega e pré-processa a imagem para a entrada do modelo."""
    try:
        img = image.load_img(img_path, target_size=(128, 128))  # Ajuste para o tamanho esperado
        img_array = image.img_to_array(img) #/ 255.0  # Normalizar para [0,1]
        img_array = np.expand_dims(img_array, axis=0)  # Adiciona dimensão de batch
        return img_array
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")
        return None


def predict(img_path = "data/valid/Car/05118.jpeg"):
    """Recebe uma imagem e retorna a classe prevista pelo modelo."""
    img_array = preprocess_image(img_path)
    
    if img_array is None:
        return {"error": "Falha no pré-processamento da imagem."}
    
    prediction = model.predict(img_array)

    # Se for um problema binário (0 ou 1), aplicar threshold de decisão
    predicted_class = 1 if prediction[0] > 0.5 else 0  

    return {"prediction": predicted_class, "confidence": float(prediction[0])}


# Exemplo de uso
if __name__ == '__main__':
    img_path = "data/valid/Car/05118.jpeg"  # Caminho da imagem de teste
    result = predict(img_path)
    print(result)
