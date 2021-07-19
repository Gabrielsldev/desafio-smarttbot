import pytest
from modulos.crypto_functions import *
from  modulos.crypto_setup import *

def test_api_call():
	assert isinstance(APICall(), pd.DataFrame)

onemindata1 = OneMinData()
onemindata2 = OneMinData()

def test_onemindata_datatype():

	assert isinstance(onemindata1[0], datetime.datetime)
	assert isinstance(onemindata1[1], list)
	assert isinstance(onemindata1[2], datetime.datetime)

def test_onemindata_timedelta():

	assert (onemindata1[2].minute - onemindata1[0].minute) == 1
	assert (onemindata2[2].minute - onemindata2[0].minute) == 1
	assert (onemindata2[0].minute - onemindata1[0].minute) == 1 or -1