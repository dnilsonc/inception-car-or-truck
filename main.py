from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
import sys

# Adiciona o diretório raiz ao PYTHONPATH para importar módulos internos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.predict import predict  # Importa sua função de predição

app = FastAPI()

# Configura CORS (permite comunicação com o frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve arquivos estáticos (frontend)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    # Salva a imagem temporariamente
    temp_path = f"temp_{file.filename}"
    
    try:
        # Salva o arquivo recebido
        with open(temp_path, "wb") as buffer:
            buffer.write(await file.read())
        
        # Chama a função de predição
        result = predict(temp_path)
        
        return result
    
    except Exception as e:
        return {"error": str(e)}
    
    finally:
        # Limpa o arquivo temporário
        if os.path.exists(temp_path):
            os.remove(temp_path)

@app.get("/test")
def test_api():
    return {"status": "API operacional!", "version": "1.0"}

@app.get("/")
async def root():
    return {"message": "API funcionando. Acesse /static/index.html para o frontend."}
