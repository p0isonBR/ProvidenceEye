from requests import get
import os

def GeradorCPF(message):

    cpf = get('https://gerador.app/api/cpf/generate', headers={"Accept": "application/json", "Authorization": "Bearer " + os.getenv("cpf_token")}).json()['number_formatted']
    return f'*CPF: *`{cpf}`'
