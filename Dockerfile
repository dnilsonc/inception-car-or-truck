# Imagem base
FROM python:3.9-slim

# Diretório de trabalho
WORKDIR /app

# Copiar requirements e instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar arquivos necessários (sem barra extra após src)
COPY main.py .
COPY src src/
COPY models/car_or_truck.h5 models/
COPY static static/

# Expor a porta
EXPOSE 8000

# Rodar a API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
