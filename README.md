# The Convolutional Classifier: Car or Truck

Este projeto implementa um classificador convolucional para distinguir entre imagens de carros e caminhões, inspirado no notebook do Kaggle "The Convolutional Classifier". O objetivo é demonstrar a aplicação de redes neurais convolucionais (CNNs) para reconhecimento de imagens, integrando técnicas modernas de deep learning e deploy de aplicações.

## Visão Geral

O modelo foi desenvolvido para identificar e classificar imagens de veículos em duas categorias: **Car** e **Truck**. Além do treinamento robusto utilizando TensorFlow/Keras, o projeto conta com uma API implementada em FastAPI, permitindo que as predições sejam realizadas de forma simples e prática. A solução é conteinerizada com Docker, o que facilita a implantação e a escalabilidade em diferentes ambientes.

## Tecnologias Utilizadas

- **Python**: Linguagem utilizada para o desenvolvimento do modelo e da aplicação.
- **TensorFlow/Keras**: Frameworks empregados na construção e treinamento da CNN.
- **FastAPI**: Framework para criação da API, possibilitando a integração e a realização de predições em tempo real.
- **Docker**: Garantia de portabilidade e consistência no deploy da aplicação.
- **CI/CD**: Adoção de pipelines de integração e deploy contínuos que automatizam testes e validações, assegurando a qualidade e a agilidade no desenvolvimento.

## Funcionalidades

- **Classificação de Imagens**: O sistema identifica se uma imagem contém um carro ou um caminhão com alta precisão.
- **API para Predições**: Interface RESTful que facilita a integração com outros sistemas e aplicações.
- **Deploy Simplificado**: Uso de Docker para um deploy rápido e confiável em qualquer ambiente.
- **Automação com CI/CD**: Pipelines que garantem testes automatizados e deploy contínuo, promovendo um ciclo de desenvolvimento ágil e seguro.

## Teste Online

Experimente a aplicação diretamente através deste link: [Teste Online](http://3.145.90.115/static/index.html)

## Referências

- [The Convolutional Classifier - Kaggle](https://www.kaggle.com/code/ryanholbrook/the-convolutional-classifier)

## Licença

Distribuído sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

Sinta-se à vontade para contribuir e sugerir melhorias!
