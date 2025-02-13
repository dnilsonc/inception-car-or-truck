from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.predict import predict  # Ajuste a importação de acordo com a estrutura do seu projeto

app = FastAPI()

@app.get("/predict/")
def get_prediction():
    # Caminho fixo da imagem para teste
    img_path = "data/valid/Car/05118.jpeg"  # Ou qualquer outro caminho que você queira usar
    result = predict(img_path)
    return JSONResponse(content=result)

@app.get("/test/")
def test():
    return {"Testando API... OK!"}
