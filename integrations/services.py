import requests


def buscar_endereco(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    if response.status_code == 200:
        data = response.json()
        return {
            "cidade": data.get("localidade"),
            "estado": data.get("estado")
        }
    raise ValueError("CEP inválido ou não encontrado.")


def buscar_moeda(pais):
    moeda = buscar_destino(pais)  # ex: "EUR"
    url = f'https://economia.awesomeapi.com.br/last/BRL-{moeda}'

    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        chave = list(dados.keys())[0]  # ex: "BRLEUR"
        return {
            "moeda": moeda,
            "cotacao": dados[chave].get("high"),
            "nome": dados[chave].get("name")
        }

    raise ValueError("Moeda inválida ou não encontrada.")


def buscar_destino(pais):
    response = requests.get('http://127.0.0.1:8000/api/currencies/countries/')
    if response.status_code == 200:
        dados = response.json()

        for item in dados:
            nome_api = item.get("pais", "").strip().lower()
            nome_input = pais.strip().lower()
            if nome_api == nome_input:
                return item.get("codigo_iso")

    raise ValueError("País inválido ou não encontrado.")

