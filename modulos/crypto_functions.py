import pandas as pd
import numpy as np
from time import sleep
import datetime

# Função para consumir os dados da API Poloniex
# https://docs.poloniex.com/#returnticker

def APICall():
    '''
    Função para consumir os dados da API Poloniex
    https://docs.poloniex.com/#returnticker
        
    Return:
        Pandas Datafrme com os dados coletados.
    ---
    
    '''
    
    url = 'https://poloniex.com/public?command=returnTicker'
    df = pd.read_json(url)
    
    return df


# Captura os dados da API - 1 minuto.

def OneMinData(currency="USDT_BTC"):
    '''
    Função para capturar os dados da API a cada minuto.
    
    Args:
        currency = moeda definida pelo usuário, conforme link: https://docs.poloniex.com/#currency-pair-ids
        Por padrão, currency busca por USDT_BTC (US Dollar x Bitcoin).
    ---
    
    Return:
        Tuple com datetime do início da coleta de dados, lista com dados, datetime do final da coleta de dados.
    ---
    
    '''

    # Pega hora atual
    now = datetime.datetime.now()
    
    # While Loop garante que os dados do CandleStick serão coletados a partir
    # do primeiro segundo de cada minuto.
    # Evita que os dados sejam coletados no momento em que a função for chamada, o que poderia
    # acarretar no início da coleta de dados em momento diferente do início
    # do período pretendido pelo usuário.
    while now.second != 0:
        now = datetime.datetime.now()
        now = pd.to_datetime(now)
        sleep(1/50)
    
    # Datetime do início da coleta de dados
    begin = datetime.datetime.now()
    begin = pd.to_datetime(begin)
    
    # Cria lista vazia para ser populada com os dados
    one_min_data = []
    # Cria contador para calcular a diferença entre o início da coleta dos dados e o datetime atual.
    counter = datetime.datetime.now()
    timedelta = counter - begin
    
    # Coleta os dados enquando estiver dentro do minuto.
    # Decidiu-se desprezar o último segundo haja vista a API Poloniex pública ser um pouco instável
    # e demorar um pouco mais para responder, o poderia acarretar na perda do minuto seguinte inteiro.
    # Em termos técnicos e estatísticos, essa perda de um segundo não é significativa.
    # A leitura é feita a cada 1/20 segundos e apensada no final da lista.
    while (timedelta.seconds < 59):
        one_min_data.append(APICall()[[currency]].loc["last"][0])
        counter = datetime.datetime.now()
        timedelta = counter - begin
        sleep(1/20)
    
    # Datetime do final da coleta de dados
    finish = datetime.datetime.now()
    finish = pd.to_datetime(finish)
    
    return (begin.round(freq = 'T'), one_min_data, finish.round(freq = 'T'))


# Captura os dados da API - 5 minutos.

def FiveMinData(currency="USDT_BTC"):
    '''
    Função para capturar os dados da API a cada 5 minutos.
    
    Args:
        currency = moeda definida pelo usuário, conforme link: https://docs.poloniex.com/#currency-pair-ids
        Por padrão, currency busca por USDT_BTC (US Dollar x Bitcoin).
    ---
    
    Return:
        Tuple com datetime do início da coleta de dados, lista com dados, datetime do final da coleta de dados.
    ---
    
    '''

    # Pega hora atual
    now = datetime.datetime.now()

    # While Loop garante que os dados do CandleStick serão coletados a partir
    # do primeiro segundo a cada 5 minutos.
    # Evita que os dados sejam coletados no momento em que a função for chamada, o que poderia
    # acarretar no início da coleta de dados em momento diferente do início
    # do período pretendido pelo usuário.
    while now.second != 0:
        now = datetime.datetime.now()
        now = pd.to_datetime(now)
        sleep(1/50)

    # Datetime do início da coleta de dados
    begin = datetime.datetime.now()
    begin = pd.to_datetime(begin)

    # Cria lista vazia para ser populada com os dados
    five_min_data = []
    # Cria contador para calcular a diferença entre o início da coleta dos dados e o datetime atual.
    counter = datetime.datetime.now()
    timedelta = counter - begin

    # Coleta os dados enquando estiver dentro dos 5 minutos.
    # Decidiu-se desprezar o último segundo haja vista a API Poloniex pública ser um pouco instável
    # e demorar um pouco mais para responder, o poderia acarretar na perda do minuto seguinte inteiro.
    # Em termos técnicos e estatísticos, essa perda de um segundo não é significativa.
    # A leitura é feita a cada 1/5 segundos e apensada no final da lista.
    while (timedelta.seconds < 299):
        five_min_data.append(APICall()[[currency]].loc["last"][0])
        counter = datetime.datetime.now()
        timedelta = counter - begin
        sleep(1/5)

    # Datetime do final da coleta de dados
    finish = datetime.datetime.now()
    finish = pd.to_datetime(finish)
    
    return (begin.round(freq = 'T'), five_min_data, finish.round(freq = 'T'))


# Captura os dados da API - 10 minutos.

def TenMinData(currency="USDT_BTC"):
    '''
    Função para capturar os dados da API a cada 10 minutos.
    
    Args:
        currency = moeda definida pelo usuário, conforme link: https://docs.poloniex.com/#currency-pair-ids
        Por padrão, currency busca por USDT_BTC (US Dollar x Bitcoin).
    ---
    
    Return:
        Tuple com datetime do início da coleta de dados, lista com dados, datetime do final da coleta de dados.
    ---
    
    '''

    # Pega hora atual
    now = datetime.datetime.now()

    # While Loop garante que os dados do CandleStick serão coletados a partir
    # do primeiro segundo a cada 10 minutos.
    # Evita que os dados sejam coletados no momento em que a função for chamada, o que poderia
    # acarretar no início da coleta de dados em momento diferente do início
    # do período pretendido pelo usuário.
    while now.second != 0:
        now = datetime.datetime.now()
        now = pd.to_datetime(now)
        sleep(1/50)

    # Datetime do início da coleta de dados
    begin = datetime.datetime.now()
    begin = pd.to_datetime(begin)

    # Cria lista vazia para ser populada com os dados
    ten_min_data = []
    # Cria contador para calcular a diferença entre o início da coleta dos dados e o datetime atual.
    counter = datetime.datetime.now()
    timedelta = counter - begin

    # Coleta os dados enquando estiver dentro dos 10 minutos.
    # Decidiu-se desprezar o último segundo haja vista a API Poloniex pública ser um pouco instável
    # e demorar um pouco mais para responder, o poderia acarretar na perda do minuto seguinte inteiro.
    # Em termos técnicos e estatísticos, essa perda de um segundo não é significativa.
    # A leitura é feita a cada 1/5 segundos e apensada no final da lista.
    while (timedelta.seconds < 599):
        ten_min_data.append(APICall()[[currency]].loc["last"][0])
        counter = datetime.datetime.now()
        timedelta = counter - begin
        sleep(1/5)

    # Datetime do final da coleta de dados
    finish = datetime.datetime.now()
    finish = pd.to_datetime(finish)
    
    return (begin.round(freq = 'T'), ten_min_data, finish.round(freq = 'T'))


# Pega os dados de capturados da API e transforma em um dataframe para a formação dos candles
# com os dados de periodicidade, datetime, open, low, high e close.
# Cria um Dataframe somente com uma linha com os dados coletados no período indicado.

def CandleStickData(data, period, currency="USDT_BTC"):
    '''
    Função para pegar os dados capturados da API e transformar em um dataframe 
    com os dados de periodicidade, datetime, open, low, hihgh e close.
    
    Cria um Dataframe somente com uma linha com os dados coletados no período indicado.
    Para se criar uma tabela completa a ser salva no banco de dados, é necessário apensar
    cada uma das linhas criadas por quanto tempo se desejar.
    
    Args:
        data = Tuple retornado por uma das funções OneMinData(), FiveMinData() ou TenMinData().
    
        currency = moeda definida pelo usuário, conforme link: https://docs.poloniex.com/#currency-pair-ids
        Por padrão, currency busca por USDT_BTC (US Dollar x Bitcoin).
        
        period = qual o período escolhido, se 1, 5 ou 10 minutos.
    ---
    
    Return:
        DataFrame com uma linha com os dados Periodicidade, Datetime, Open, Low, High e Close
        para o período desejado pelo usuário (1, 5 ou 10 minutos).
    ---
    
    '''
    
    # Dataframe será criado com as colunas Periodicidade, Datetime, Open, Low, High e Close.
    Moeda = currency
    Periodicidade = period
    Open = data[1][0]
    Low = min(data[1])
    High = max(data[1])
    Close = data[1][-1]
    
    # Dicionário para ser passado como argunto em pd.DataFrame() para criação do DataFrame.
    df_data = {
        'Moeda':[Moeda],
        'Periodicidade':[Periodicidade],
        'Datetime':[data[0]],
        'Open':[Open],
        'Low': [Low],
        'High': [High],
        'Close': [Close]}
    
    # Cria do DataFrame a partir do dicionário fornecido.
    df_model = pd.DataFrame(data=df_data)
    
    return df_model


# Função para passar os dados coletados pela API e já transformados em um DataFrame
# a fim de criar um gráfico de CandleStick em tempo real.

def ShowChart(data_chart, currency="USDT_BTC"):
    '''
    Função para passar os dados coletados pela API e já transformados em um DataFrame
    a fim de criar um gráfico de CandleStick em tempo real.
    
    Retorna os dados de acordo com o esperado pelo Plotly para a criação de um único candle em um
    gráfico de CandleSticks.
    
    Args:
        data_chart = DataFrame retornado pela função CandleStickData().
    
        currency = moeda definida pelo usuário, conforme link: https://docs.poloniex.com/#currency-pair-ids
        Por padrão, currency busca por USDT_BTC (US Dollar x Bitcoin).
    ---
    
    Return:
        Dicionário com os dados esperados pelo Plotly para a criação de um
        único candle em um gráfico de CandleStick.
    ---
    
    '''
    
    candles_grafico = {
        "x": data_chart["Datetime"],
        "open": data_chart["Open"],
        "close": data_chart["Close"],
        "high": data_chart["High"],
        "low": data_chart["Low"],
        "type": 'candlestick',
        "name": currency,
    }

    dados_grafico = [candles_grafico]
    
    return candles_grafico