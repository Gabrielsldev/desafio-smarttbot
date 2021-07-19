# **Pessoa Desenvolvedora BackEnd - Plataformas (Python)** | ![SMARTTBOT](https://smarttbot.com/wp-content/uploads/2018/02/sb-1.png)
## Desafio Técnico
###### Desenvolvido por **Gabriel Sobreira Lopes**

### Descrição

O desafio consiste em criar um sistema de agregação de dados de cotações de criptomoedas em tempo real. É necessário construir os candles de 1, 5 e 10 minutos a partir dos dados consumidos via [API Poloniex](https://docs.poloniex.com/#returnticker).

### **Criei meu próprio cliente** a partir das recomendações exigidas:

* Utilização da linguagem **Python**.
* Utilização do **MySQL** para salvar os dados dos candles.
* Uso de ferramentas e componentes open-source, como **Pandas**, **Numpy**, **SQLAlchemy**, dentre outros.
* Testes utilizando a biblioteca **Pytest**.
* Utilização do GIT para controle de versões.

Foram incluídos os seguintes extras:

* Suporte a qualquer moeda disponível na [API](https://docs.poloniex.com/#currency-pair-ids).
* Gráfico de CandleStick plotado em tempo real, de acordo com a coleta dos dados, utilizando a biblioteca **Plotly**.

O programa foi pensado como uma **biblioteca que será utilizada por outras pessoas**. Dessa forma, prezou-se pelas **boas práticas**, **código bem comentado**, além de uma **boa documentação** e **fácil usabilidade**.

**NOTA:** Foi solicitado o uso de Docker e Docker-Compose. Essas ferramentas se apresentam como um desafio para mim. Iniciei um [curso](https://www.udemy.com/course/docker-essentials-for-python-developers/) imediatamente a fim de suprir essa lacuna.

***

## Instruções de uso

* Clone o repositório para o diretório desejado.
* Crie um ambiente virtual e instale os pacotes listados no arquivo [requirements.txt](https://github.com/Gabrielsldev/desafio-smarttbot/blob/main/requirements.txt) por meio do comando `pip install -r requirements.txt`.
* A aplicação foi criada no sistema **Ubuntu 20.04** utilizando **Python 3.8.10**.

## Execução do programa
