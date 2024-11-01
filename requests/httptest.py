# Importação das bibliotecas necessárias
import httpx
import respx
from typing import Literal, TypeAlias

# Define a URL para a coleta de dados de cotação das moedas
URL_COTACAO = 'https://economia.awesomeapi.com.br/last/{}'

# Define um type alias para o tipo de moeda, que pode ser 'EUR' ou 'USD'
Moeda: TypeAlias = Literal['EUR', 'USD']

def cotacao(moeda: Moeda):
    # Construindo o código da moeda.
    code = f'{moeda}-BRL'
    
    # Faça uma requisição HTTP GET para buscar os dados de cotações.
    response = httpx.get(URL_COTACAO.format(code))
    
    # Extrai os dados relevantes da resposta JSON.
    data = response.json()[code.replace('-', '')]

    # Retorna a maior valor da cotação como uma string já formatada
    return 'Última Cotação: ' + data["high"]

#printa a cotação desejada: Euro ou Dolar
print(cotacao('EUR'))