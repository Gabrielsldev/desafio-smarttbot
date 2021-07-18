import sqlalchemy as sq
import pymysql
import pandas as pd

def GetArgs():
    '''
    Função para pegar os inputs do usuário que servirão de parâmetro para as funções.
    
    Return:
        currency = Moeda desejada (https://docs.poloniex.com/#currency-pair-ids)
        period = Período dos candles (1, 5 ou 10).
        duration = Duração da coleta, em minutos.
        user = Usuário MySQL.
        password = Senha MySQL.
        database = Banco de Dados MySQL a ser utilizado.
    ---
    
    '''
    
    # Pega input dos usuários para servirem de parâmetros para as funções
    currency = input("Moeda (deixe em branco para Bitcoin): ")
    if not currency:
        currency = "USDT_BTC"
    else:
        currencies = pd.read_csv("modulos/PossibleCurrencies.csv")
        currencies = currencies['MOEDA'].tolist()
        while currency not in currencies:
            print("Digite uma moeda válida (https://docs.poloniex.com/#currency-pair-ids)")
            currency = input("Moeda (deixe em branco para Bitcoin): ")
            if not currency:
                currency = "USDT_BTC"

    period = int(input("Período do Candle em minutos(1, 5 ou 10): "))
    while period not in [1, 5, 10]:
        print("Período deve ser 1, 5 ou 10: ")
        period = int(input("Período do Candle em minutos(1, 5 ou 10): "))

    while True:
        try:
            duration = int(input("Por quanto tempo você quer coletar as informações (em minutos): "))
        except ValueError:
            print('Por favor, entre com um número inteiro.')
            continue
        break

    user = input("Usuário MySQL (deixe em branco para root): ")
    if not user:
        user = "root"

    password = input("Senha MySQL: ")
    database = input("Nome do banco de dados a ser utilizado: ")
    
    return currency, period, duration, user, password, database



def MySqlConnection(password, database, user="root"):
    '''
    Cria a conexão com o banco de dados MySQL.
    
    Args:
        user = Usuário do banco de dados.
        Por padrão utiliza 'root'.
    
        password = Senha do banco de dados.
        
        database = Banco de dados criado.
        Deve ser criado no MySQL antes da execução do programa e fornecido como argumento.
    ---
    
    Return:
        Retorna objeto de conexão para ser fornecido na função do Pandas to_sql().
    ---
    
    '''
    
    conn = sq.create_engine("mysql+pymysql://"+user+":"+password+"@localhost/"+database)

    return conn