from fastapi import FastAPI
import sys
import os

# Adiciona o diretório raiz (onde está o "src") ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.predict import predict  # Ajuste a importação de acordo com a estrutura do seu projeto

app = FastAPI()

@app.get("/predict/")
def get_prediction():
    return {"prediction": predict()}
