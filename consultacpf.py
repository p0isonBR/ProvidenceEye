from requests import get
import re


def ConsultaCPF(message):
    cpf = message.text[8:].replace('-', '').replace('.', '')
    if len(cpf) != 11:
        return '`Documento invalido`'

    elif message.text == '/cpfull@ProvidenceEye_Bot':
        return '`Insira o CPF apos o comando!`'

    else:
        r = get(f'https://sherlockconsulta.herokuapp.com/cpf/{cpf}').json()
        if r["status"]:
            return f'''
*CPF*: `{cpf}`
*Nome*: `{r["result"]["nome_da_pf"].title()}`
*Nascimento*: `{r["result"]["data_nascimento"]}`
*Situacao Cadastral*: `{r["result"]["situacao_cadastral"].title()}`
''')

        else:
            return '`Documento nao encontrado banco de dados ou invalido!`'
