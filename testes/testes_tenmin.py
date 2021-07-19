import pytest
from modulos.crypto_functions import *
from  modulos.crypto_setup import *

def test_api_call():
	assert isinstance(APICall(), pd.DataFrame)

tenmindata1 = TenMinData()
tenmindata2 = TenMinData()

def test_tenmindata_datatype():

	assert isinstance(tenmindata1[0], datetime.datetime)
	assert isinstance(tenmindata1[1], list)
	assert isinstance(tenmindata1[2], datetime.datetime)

def test_tenmindata_timedelta():

	assert (tenmindata1[2].minute - tenmindata1[0].minute) == 10
	assert (tenmindata2[2].minute - tenmindata2[0].minute) == 10
	assert (tenmindata2[0].minute - tenmindata1[0].minute) == 10 or -10