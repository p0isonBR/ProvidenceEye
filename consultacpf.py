from requests import get
import re

def ConsultaCPF(message):

    cpf = message.text[8:].replace('-', '').replace('.', '')
    if len(cpf) != 11:
        return '`Documento invalido`'
    elif message.text == '/cpfull@ProvidenceEye_Bot':
        return '`Insira o CPF apos o comando!`'
    else:
        r = get(f'http://191.235.103.105/cpf/api.php?lista={cpf}').text
        if "PESSOAFISICA" in r:
            return f'''
*CPF*: `{re.search('NRCPF="(.*?)"', r).group(1)}`
*Nome*: `{re.search('NOPESSOAFISICA="(.*?)"', r).group(1).title()}`
*Nascimento*: `{re.search('DTNASCIMENTO="(.*?)"', r).group(1)}`
*Nome da Mae*: `{re.search('NOMAE="(.*?)"', r).group(1).title()}`
*Endereco*: `{re.search('NOLOGRADOURO="(.*?)"', r).group(1).title()}, {re.search('NRLOGRADOURO="(.*?)"', r).group(1)}`
*Complemento*: `{re.search('DSCOMPLEMENTO="(.*?)"', r).group(1).title()}`
*Bairro*: `{re.search('NOBAIRRO="(.*?)"', r).group(1).title()}`
*Cidade*: `{re.search('NOMUNICIPIO="(.*?)"', r).group(1).title()}-{re.search('SGUF="(.*?)"', r).group(1)}`
*CEP*: `{re.search('NRCEP="(.*?)"', r).group(1)}`
''')
        else:
            return '`Documento nao encontrado!`'
