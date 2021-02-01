from requests import get

def GeradorCPF(message):

    cpf = get('http://geradorapp.com/api/v1/cpf/generate?token=f01e0024a26baef3cc53a2ac208dd141').json()['data']['number_formatted']
    return f'*CPF: *`{cpf}`'
