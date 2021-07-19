import pytest
from modulos.crypto_functions import *
from  modulos.crypto_setup import *


# Testa se a chamada para a API está funcinando corretamente.
def test_api_call():
	assert isinstance(APICall(), pd.DataFrame)


# Cria as variáveis para sere utilizadas nos testes abaixo com os dados coletados via API.
fivemindata1 = FiveMinData()
fivemindata2 = FiveMinData()


# Testa se da função FiveMinData() retorna os datatypes esperados.
def test_fivemindata_datatype():

	assert isinstance(fivemindata1[0], datetime.datetime)
	assert isinstance(fivemindata1[1], list)
	assert isinstance(fivemindata1[2], datetime.datetime)


# Testa se da função FiveMinData() retorna os os dados com os intervalos esperados.
def test_fivemindata_timedelta():

	assert (fivemindata1[2].minute - fivemindata1[0].minute) == 5
	assert (fivemindata2[2].minute - fivemindata2[0].minute) == 5
	assert (fivemindata2[0].minute - fivemindata1[0].minute) == 5 or -5