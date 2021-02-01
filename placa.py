from requests import get

def consusltaplaca(message):

    proxys = get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=yes&anonymity=all&simplified=true').text
    proxys = proxys.splitlines()
    placa = message.text.replace('/placa ', '').replace('-', '')

    for x in range(len(proxys)):
        try:
            p = {
                'http': proxys[x]
            }
            r = get(f'https://apicarros.com/v1/consulta/{placa}/json', verify=False, proxies=p).json()
            modelo = r["modelo"]
            marca = r["marca"]
            ano = r["ano"]
            anoModelo = r["anoModelo"]
            chassi = r["chassi"]
            cor = r["cor"]
            situacao = r["situacao"]
            cidade = r["municipio"]
            uf = r["uf"]
            furto = r["dataAtualizacaoRouboFurto"]
            return f'*Placa*: `{placa.upper()}`\n*Modelo*: `{modelo.title()}`\n*Marca*: `{marca}`\n*Ano*: `{ano}/{anoModelo}`\n*Cor*: `{cor}`\n*Situacao*: `{situacao}`\n*Municipio*: `{cidade.title()}-{uf}`\n*Chassi*: `{chassi}`\n*Data da atualizacao*: `{furto}`'
        except Exception as e:
            print(e)
