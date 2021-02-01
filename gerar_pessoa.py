from requests import get

def gerarPessoa():

    while True:
        cpf = get('http://geradorapp.com/api/v1/cpf/generate?token=f01e0024a26baef3cc53a2ac208dd141').json()['data']['number']
        r = get(f'http://104.41.5.41:12345/cpf.php?lista={cpf}').json()
        if r['Type'] == "PESSOAFISICA":
            return f'''*CPF*: `{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}`
*Nome*: `{r["Nome"].title()}`
*Nascimento*: `{r["Nacimento"]}`
*Nome da Mae*: `{r["Mae"].title()}`
*Endereco*: `{r["Nologradouro"].title()}, {r["Nrlogradouro"]}`
*Complemento*: `{r["Complemento"].title()}`
*Bairro*: `{r["Bairro"].title()}`
*Cidade*: `{r["Municipio"].title()}-{r["Estado"]}`
*CEP*: `{r["Cep"][:5]}-{r["Cep"][5:]}`'''
