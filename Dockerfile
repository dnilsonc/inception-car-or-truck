FROM python:3.12.3

WORKDIR /app

# Copiar apenas o requirements.txt primeiro para otimizar cache
COPY requirements.txt .

# Instalar dependências, incluindo DVC
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir dvc dvc-s3  # Se precisar usar DVC com AWS S3

# Agora copia o restante do código
COPY . .

CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
