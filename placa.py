from requests import get

def consultaplaca(message):
    
	placa = message.text.replace('/placa ', '').replace('-', '')
	r = get(f'http://api.masterplaca.devplank.com/v2/placa/{placa}/json').json()
	modelo = r["modelo"]
	marca = r["marca"]
	ano = r["ano"]
	anoModelo = r["anoModelo"]
	chassi = r["chassi"]
	cor = r["cor"]
	situacao = r["situacao"]
	cidade = r["municipio"]
	uf = r["uf"]
	return f'''*Placa*: `{placa.upper()}`
*Modelo*: `{modelo.title()}`
*Marca*: `{marca}`
*Ano*: `{ano}/{anoModelo}`
*Cor*: `{cor}`
*Situacao*: `{situacao}`
*Municipio*: `{cidade.title()}-{uf}`
*Chassi*: `{chassi}`'''
