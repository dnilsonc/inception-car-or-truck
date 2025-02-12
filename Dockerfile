FROM python:3.12.3
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
