import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# 1. Simulando 1 ano (365 dias) de vendas diárias de um e-commerce
np.random.seed(42)
datas = pd.date_range(start='2025-01-01', periods=365, freq='D')

# Tendência de crescimento ao longo do ano + Sazonalidade semanal (pico nos finais de semana) + Ruído
tendencia = np.linspace(1000, 3000, 365)
sazonalidade = np.sin(np.arange(365) * (2 * np.pi / 7)) * 400
ruido = np.random.normal(0, 100, 365)
vendas = tendencia + sazonalidade + ruido

df = pd.DataFrame({'data': datas, 'vendas': vendas})
df.set_index('data', inplace=True)

print(f"📅 Histórico de dados: {df.index.min().strftime('%d/%m/%Y')} até {df.index.max().strftime('%d/%m/%Y')}")
print(f"💰 Média de vendas diárias: R$ {df['vendas'].mean():.2f}\n")

# 2. Treinando o Modelo Holt-Winters
# seasonal_periods=7 indica ciclo semanal (sazonalidade de 7 dias)
modelo = ExponentialSmoothing(
    df['vendas'], 
    trend='add', 
    seasonal='add', 
    seasonal_periods=7
)
modelo_ajustado = modelo.fit()

# 3. Prevendo os próximos 7 dias no futuro
dias_previsao = 7
previsao = modelo_ajustado.forecast(dias_previsao)

print("📈 --- PREVISÃO DE VENDAS PARA A PRÓXIMA SEMANA ---")
for data, valor in previsao.items():
    print(f"🗓️  {data.strftime('%d/%m/%Y (%A)')}: R$ {valor:.2f}")