# The Convolutional Classifier: Car or Truck

Este repositório implementa um classificador convolucional para distinguir entre imagens de carros e caminhões, baseado no notebook do Kaggle [The Convolutional Classifier](https://www.kaggle.com/code/ryanholbrook/the-convolutional-classifier).

## 📌 Visão Geral
O objetivo deste projeto é criar um modelo de aprendizado profundo capaz de classificar imagens de veículos como carros ou caminhões. Utilizamos uma rede neural convolucional (CNN) treinada com TensorFlow/Keras para realizar essa tarefa.

## 🚀 Tecnologias Utilizadas
- Python
- TensorFlow/Keras
- FastAPI
- Docker

## 📂 Estrutura do Repositório
```
/                         # Diretório raiz
├── data/                 # Arquivos do dataset
├── notebooks/            # Notebooks Jupyter com experimentos
├── models/               # Modelos treinados
├── src/                  # Códigos-fonte do projeto
│   ├── train.py          # Script para treinamento do modelo
│   ├── evaluate.py       # Avaliação do modelo
│   ├── predict.py        # Predições em novas imagens
├── requirements.txt      # Dependências do projeto
└── README.md             # Este arquivo
```

## 📥 Instalação
Clone o repositório e instale as dependências:
```bash
git clone https://github.com/seu-usuario/the-convolutional-classifier.git
cd the-convolutional-classifier
pip install -r requirements.txt
```

## 📊 Treinamento do Modelo
Para treinar o modelo a partir do zero, execute:
```bash
python src/train.py
```
O script carregará os dados, aplicando pré-processamento e treinamento com TensorFlow/Keras.

## 🔍 Avaliação
Para avaliar o desempenho do modelo:
```bash
python src/evaluate.py
```
Isso gerará métricas como acurácia, matriz de confusão e curvas ROC/AUC.

## 🖼️ Testando Predições
Para fazer previsões em novas imagens:
```bash
python src/predict.py --image caminho/para/imagem.jpg
```
O script irá carregar o modelo treinado e prever se a imagem é um carro ou um caminhão.

## 🌐 Teste Online
Você pode testar o projeto online acessando [este link](http://54.175.48.121/static/index.html).

## 📌 Referências
- [The Convolutional Classifier - Kaggle](https://www.kaggle.com/code/ryanholbrook/the-convolutional-classifier)

## 📜 Licença
Este projeto é distribuído sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

---
Sinta-se à vontade para contribuir ou sugerir melhorias! 🚀

