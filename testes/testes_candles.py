import pytest
from modulos.crypto_functions import *
from  modulos.crypto_setup import *


# Testa se a chamada para a API está funcinando corretamente.
def test_api_call():
	assert isinstance(APICall(), pd.DataFrame)


# Cria variável para ser utilizada nos testes abaixo com os dados coletados via API. 
onemindata = OneMinData()
candledata = CandleStickData(data=onemindata, period=1, currency="USDT_BTC")


# Verifica se o DataFrame criado pela função OneMinData() contém as colunas desejadas
# e se os dados estão corretos.
def test_candlestickdata():

	assert isinstance(candledata["Moeda"][0],str)
	assert isinstance(candledata["Periodicidade"][0],np.integer)
	assert isinstance(candledata["Datetime"][0],datetime.datetime)
	assert isinstance(candledata["Open"][0],float)
	assert isinstance(candledata["Low"][0],float)
	assert isinstance(candledata["High"][0],float)
	assert isinstance(candledata["Close"][0],float)


# Verifica se a função ShowChart() cria o dict esperada pelo Plotly para plotar o gráfico.
def test_showchart():

	datachart = ShowChart(candledata, currency="USDT_BTC")

	assert isinstance(datachart,dict)