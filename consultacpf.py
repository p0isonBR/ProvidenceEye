from requests import get

def ConsultaCPF(message):

    cpf = message.text[8:].replace('-', '').replace('.', '')
    if len(cpf) != 11:
        return '`Documento invalido`'
    elif message.text == '/cpfull@ProvidenceEye_Bot':
        return '`Insira o CPF apos o comando!`'
    else:
        r = get(f'http://104.41.5.41:12345/cpf.php?lista={cpf}').json()
        if r['Type'] == "PESSOAFISICA":
            return f'''
*CPF*: `{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}`
*Nome*: `{r["Nome"].title()}`
*Nascimento*: `{r["Nacimento"]}`
*Nome da Mae*: `{r["Mae"].title()}`
*Endereco*: `{r["Nologradouro"].title()}, {r["Nrlogradouro"]}`
*Complemento*: `{r["Complemento"].title()}`
*Bairro*: `{r["Bairro"].title()}`
*Cidade*: `{r["Municipio"].title()}-{r["Estado"]}`
*CEP*: `{r["Cep"][:5]}-{r["Cep"][5:]}`'''
        else:
            return '`Documento nao encontrado!`'
