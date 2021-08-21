# **REAL-TIME CRYPTOCURRENCY DATA AGGREGATION SYSTEM**
###### Developed by **Gabriel Sobreira Lopes**

### Description

Real-time cryptocurrency quote data aggregation system. Builds 1, 5 and 10 minute candles from data consumed via [API Poloniex](https://docs.poloniex.com/#returnticker).

### **I created my own client** with the following tools:

* **Python**.
* **Pandas**, **Numpy**, **SQLAlchemy**, among others.
* **MySQL** to save candle stick data.
* **Pytest** to test some of the features.
* **GIT** for version control.

**Features:**

* Support for **any cryptocurrency** provided by the [API](https://docs.poloniex.com/#currency-pair-ids).
* **CandleStick graph** in real time using **Plotly**.

***

# Instructions:

* Clone the repository to the desired directory.
* Create a virtual environment and install the packages listed in the file [requirements.txt](https://github.com/Gabrielsldev/desafio-smarttbot/blob/main/requirements.txt) using `pip install -r requirements.txt`.
* The application was created on **Ubuntu 20.04** with **Python 3.8.10**.

## Execution:

* Run the program `main.py` with `python main.py`.
* The application execution is very intuitive, but the information below must be observed.

**Important notes:**
It is necessary that the **MySQL service is running locally** so that the application can connect to the database. **Before running the program, it is necessary to create a database so that the tables can be saved.** This database will be informed in the execution of the application.

The following data is requested from the user:
* `Moeda (deixe em branco para Bitcoin)`, conforme [moedas disponíveis na API](https://docs.poloniex.com/#currency-pair-ids).
  * `Currency (leave blank for Bitcoin)`, as per [currencies available in the API](https://docs.poloniex.com/#currency-pair-ids).
* `Período do Candle em minutos(1, 5 ou 10)`, informação necessária para definir o período de cada candle.
  * `Candle period in minutes (1, 5 or 10)`, information necessary to define the period of each candle.
* `Por quanto tempo você quer coletar as informações (em minutos)`, define por quanto tempo a aplicação irá rodar.
  * `How long do you want to collect the information (in minutes)`, defines how long the application will run.
* `Usuário MySQL (deixe em branco para root)`, usuário MySQL.
  * `MySQL user (leave blank for root)`, MySQL user.
* `Senha MySQL`, senha MySQL.
  * `MySQL password`, MySQL password.
* `Nome do banco de dados a ser utilizado`, informar o banco de dados criado para salvar as tabelas criadas pela aplicação.
  * `Name of the database to be used`, database created to save the tables created by the application.

It is informed in the terminal whenever the data of each candle is saved in the database. It is noteworthy that candles are only saved after collecting and processing information.

***

## Expected results:

* The program **will consume the API data in real time** and **will save the candles in the informed database** in tables called `one_minute`, `five_minutes` and `ten_minutes`, depending on the desired candle period, as per model below:

| Moeda  |  Periodicidade  |  Datetime  |  Open  |  Low  |  High  |  Close  |
| ------ | --------------- | ---------- | ------ | ----- | ------ | ------- |
|  ---   |      ---        |     ---    |   ---  |  ---  |  ---   |   ---   |
|  ---   |      ---        |     ---    |   ---  |  ---  |  ---   |   ---   |

* **A graph** will be plotted in the browser, in real time, with the collected candles, as shown in the image below:
![ChartOneMin](https://github.com/Gabrielsldev/desafio-smarttbot/blob/main/static/Screenshot%20from%202021-07-19%2017-42-45.png)


***

## Tests:

Tests the application's functions. In the `tests` directory you can find four test files. I decided to split the tests into four files because the tests of the functions that collect the 5 and 10 minute candles take longer. **Pytest** library was used to build the tests.

To run them, just run, in the `tests` directory, the command `py.test` followed by the name of the file with the desired test.

* `testes_candles.py` tests the API call, the correct return of the candles data and if the data is ready to be plotted on the chart.
* `testes_onemin.py`, `testes_fivemin.py` and `testes_tenmin.py` test the API calls, if the data of each of the candles was created correctly and if the collection interval corresponds to the informed period. Files refer to periods of 1, 5 and 10 minutes respectively.

***

## Difficulties, limitations and suggestions for improvements:

Some difficulties and limitations are worth mentioning:

* The public **[API Poloniex](https://docs.poloniex.com/#returnticker)** may suffer a little from instabilities. Thus, despite the best efforts not to lose even one of the candle periods, there may be a loss due to the connection limitation.
 * This limitation can be seen in the chart below:
![ChartOneMinTest](https://github.com/Gabrielsldev/desafio-smarttbot/blob/main/static/Screenshot%20from%202021-07-19%2017-48-28.png)
 * It is possible to run tests to see if the periods are being observed as explained in the previous section.
  * To help overcome this problem, the last second of each period is neglected, which does not prevent it from occurring entirely. Technically and statistically, this last second is not significant for creating candlesticks.
  * It is expected that with the private API and a stable connection, these losses will not occur.
  * Another solution is not to plot the graph, which would save execution time between collecting one period and another.