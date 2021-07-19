from modulos.crypto_functions import *
from  modulos.crypto_setup import *
import plotly.graph_objects as go

# Pega input dos usuários para servirem de parâmetros para as funções
currency, period, duration, user, password, database = GetArgs()

# Variável global que guarda os dados a serem salvos no banco de dados
# e que serão plotados no gráfico
data = pd.DataFrame()

# Conexão com o MySQL.
conn = MySqlConnection(user=user, password=password, database=database)
# Testa conexão com MySQL
conn.connect()

# Cria o gráfico
chart = go.FigureWidget()
chart.update_layout(showlegend=False)
chart.update_layout(xaxis_rangeslider_visible=False)
chart.show()

# Duration é o tempo total que o usuário deseja que o script colete as informações, em minutos.
# Period é qual o período dos Candles, se 1, 5 ou 10 minutos.

if period == 1:

    print(f"Será criada/atualizada tabela 'one_minute' no banco de dados {database}")
    # Garante que o script sempre pegará 1 minuto, e não valores quebrados.
    i = duration//period

    # Enquanto estiver dentro do tempo total estipulado pelo usuário, coletará as informações
    # em candles de 1 minuto.
    print("Início da captura de dados.")
    while i > 0:
        # Apensa o último candle coletado no DataFrame data.
        data = data.append(CandleStickData(data=OneMinData(currency), currency=currency, period=period), ignore_index=True)
        # Salva o último dado coletado na tabela 'one_minute' no banco de dados indicado em 'database'.
        data.iloc[[-1]].to_sql("one_minute", conn, if_exists="append", index=False)
        candle_print = data["Datetime"].iloc[-1]
        print(f"Candle {candle_print} adicionado ao banco de dados com sucesso.")
        # Adiciona o candle no gráfico de CandleStick.
        chart.add_trace(go.Candlestick(ShowChart(data)));
        chart.show()
        i -= 1

elif period == 5:

    print(f"Será criada/atualizada tabela 'five_minutes' no banco de dados {database}")
    # Garante que o script sempre pegará 5 minutos, e não valores quebrados.
    i = duration//period

    # Enquanto estiver dentro do tempo total estipulado pelo usuário, coletará as informações
    # em candles de 1 minuto.
    print("Início da captura de dados.")
    while i > 0:
        # Apensa o último candle coletado no DataFrame data.
        data = data.append(CandleStickData(data=FiveMinData(currency), currency=currency, period=period), ignore_index=True)
        # Salva o último dado coletado na tabela 'one_minute' no banco de dados indicado em 'database'.
        data.iloc[[-1]].to_sql("five_minutes", conn, if_exists="append", index=False)
        candle_print = data["Datetime"].iloc[-1]
        print(f"Candle {candle_print} adicionado ao banco de dados com sucesso.")
        # Adiciona o candle no gráfico de CandleStick.
        chart.add_trace(go.Candlestick(ShowChart(data)));
        chart.show()
        i -= 1

elif period == 10:

    print(f"Será criada/atualizada tabela 'ten_minutes' no banco de dados {database}")
    # Garante que o script sempre pegará 10 minutos, e não valores quebrados.
    i = duration//period

    # Enquanto estiver dentro do tempo total estipulado pelo usuário, coletará as informações
    # em candles de 1 minuto.
    print("Início da captura de dados.")
    while i > 0:
        # Apensa o último candle coletado no DataFrame data.
        data = data.append(CandleStickData(data=TenMinData(currency), currency=currency, period=period), ignore_index=True)
        # Salva o último dado coletado na tabela 'one_minute' no banco de dados indicado em 'database'.
        data.iloc[[-1]].to_sql("ten_minutes", conn, if_exists="append", index=False)
        candle_print = data["Datetime"].iloc[-1]
        print(f"Candle {candle_print} adicionado ao banco de dados com sucesso.")
        # Adiciona o candle no gráfico de CandleStick.
        chart.add_trace(go.Candlestick(ShowChart(data)));
        chart.show()
        i -= 1