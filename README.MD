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
* Utilização do **GIT** para controle de versões.

**Foram incluídos os seguintes extras:**

* Suporte a **qualquer moeda** disponível na [API](https://docs.poloniex.com/#currency-pair-ids).
* **Gráfico de CandleStick** plotado em tempo real, de acordo com a coleta dos dados, utilizando a biblioteca **Plotly**.

O programa foi pensado como uma **biblioteca que será utilizada por outras pessoas**. Dessa forma, prezou-se pelas **boas práticas**, **código bem comentado**, além de uma **boa documentação** e **fácil usabilidade**.

**NOTA:** Foi solicitado o uso de Docker e Docker-Compose. Essas ferramentas se apresentam como um desafio para mim. Iniciei um [curso](https://www.udemy.com/course/docker-essentials-for-python-developers/) imediatamente a fim de suprir essa lacuna.

***

## Instruções de uso

* Clone o repositório para o diretório desejado.
* Crie um ambiente virtual e instale os pacotes listados no arquivo [requirements.txt](https://github.com/Gabrielsldev/desafio-smarttbot/blob/main/requirements.txt) por meio do comando `pip install -r requirements.txt`.
* A aplicação foi criada no sistema **Ubuntu 20.04** utilizando **Python 3.8.10**.

## Execução do programa

* Execute o programa `main.py` através do comando `python main.py`.
* A execução da aplicação é bem intuitiva, mas devem ser observadas as informações abaixo.

**Observações importantes:**
Para fins de entrega deste desafio, a fim de deixar a execução da aplicação mais intuitiva, ao invés de argumentos em linhas de comando, optou-se por solicitar do usuário, via `input()`, a entrada dos dados usados como argumentos das funções.
Dependendo do uso, se necessário, é possível fazer os devidos ajustes para incluir esses dados como argumentos em linha de comando ou via Docker-Compose.

**NOTA:** É necessário que o serviço **MySQL** esteja rodando para que a aplicação possa se conectar com o banco de dados. **Antes da execução do programa, é necessário a criação de um banco de dados para que as tabelas sejam salvas.** Esse banco de dados será informado na execução da aplicação.

Os seguintes dados são solicitados do usuário:
* `Moeda (deixe em branco para Bitcoin)`, conforme [moedas disponíveis na API](https://docs.poloniex.com/#currency-pair-ids).
* `Período do Candle em minutos(1, 5 ou 10)`, informação necessária para definir o período de cada candle.
* `Por quanto tempo você quer coletar as informações (em minutos)`, define por quanto tempo a aplicação irá rodar.
* `Usuário MySQL (deixe em branco para root)`, usuário MySQL. 
* `Senha MySQL`, senha MySQL.
* `Nome do banco de dados a ser utilizado`, informar o banco de dados criado para salvar as tabelas criadas pela aplicação.

É informado no terminal sempre que for salvo os dados de cada candle no banco de dados. Vale ressaltar que os candles só são salvos após a coleta e o processamento das informações.

***

## Resultados esperados

* O programa **consumirá os dados da API em tempo real** e **salvará os candles no banco de dados informado** em tabelas chamadas `one_minute`, `five_minutes` e `ten_minutes`, dependendo do período de candle desejado, conforme modelo abaixo:

| Moeda  |  Periodicidade  |  Datetime  |  Open  |  Low  |  High  |  Close  |
| ------ | --------------- | ---------- | ------ | ----- | ------ | ------- |
|  ---   |      ---        |     ---    |   ---  |  ---  |  ---   |   ---   |
|  ---   |      ---        |     ---    |   ---  |  ---  |  ---   |   ---   |

* Será **plotado um gráfico** no navegador, em tempo real, com os candles coletados, conforme imagem abaixo:
![ChartOneMin](https://github.com/Gabrielsldev/desafio-smarttbot/blob/main/static/Screenshot%20from%202021-07-19%2017-42-45.png)


***

## Testes

Foram criados testes para testar as funções da aplicação. No diretório `testes` é possível encontrar quatro arquivos de teste. Decidi dividir os testes em quatro arquivos pois os testes das funções que coletam os candles de 5 e de 10 minutos demoram mais. Foi utilizada a biblioteca **Pytest** para a construção dos testes.

Para executá-los, basta executar, no diretório `testes`, o comando `py.test` seguido do nome do arquivo com o teste desejado.

* `testes_candles.py` testa a chamada da API, o retorno correto dos dados dos candles e se os dados estão prontos para serem plotados no grádico.
* `testes_onemin.py`, `testes_fivemin.py` e `testes_tenmin.py` testam as chamadas da API, se os dados de cada um dos candles foram criados corretamente e se o intervalo de coleta corresponde ao período informado. Os arquivos referem-se aos períodos de 1, 5 e 10 minutos respectivamente.


***

## Dificuldades encontradas, limitações e sugestões de melhorias

Algumas dificuldades e limitações merecem destaque:

* A **[API Poloniex](https://docs.poloniex.com/#returnticker) pública** pode sofrer um pouco com instabilidades. Dessa forma, apesar dos melhores esforços para não se perder nem um dos períodos dos candles, pode haver perda por conta da limitação de conexão.
  * Essa limitação pode ser vista no gráfico abaixo:
![ChartOneMinTest](https://github.com/Gabrielsldev/desafio-smarttbot/blob/main/static/Screenshot%20from%202021-07-19%2017-48-28.png)
  * É possível fazer os testes para saber se os períodos estão sendo observados conforme explicado na seção anterior.
  * Para ajudar a contornar esse problema, é desprezado o último segundo de cada período, o que não impede que ocorra totalmente. Tecnicamente e estatisticamente, esse último segundo não é significativo para a criação dos candles.
  * Espera-se que com a API privada e uma conexão estável, essas perdas não ocorram.
  * Uma outra solução é não plotar o gráfico, o que economizaria tempo de execução entre a coleta de um período e outro.

* Implementação com Docker e Docker-Compose. Como já ressaltado, são ferramentas que ainda se apresentam como um desafio para mim, mas já iniciei um [curso](https://www.udemy.com/course/docker-essentials-for-python-developers/) para sanar essa lacuna.