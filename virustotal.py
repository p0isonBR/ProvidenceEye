import requests

def VirusTotal(message):
    arq = message.json
    arq = arq['reply_to_message']['document']['file_id']
    arq = requests.get(f'https://api.telegram.org/bot1414183645:AAH-jBkyE3Pemwf9EJCQt1w-MVNc45XUy9c/getFile?file_id={arq}').json()
    f = arq['result']['file_path']
    arq = 'https://api.telegram.org/file/bot1414183645:AAH-jBkyE3Pemwf9EJCQt1w-MVNc45XUy9c/' + f
    with open(f.split('/')[1], 'wb') as file:
        file.write(requests.get(arq).content)
        file.close()

    params = {'apikey': 'd1da02ce15b0aea70477b0929a67528e0f4f18f11bcb76bcf43760331bb59699'}
    files = {'file': (f.split('/')[1], open(f.split('/')[1], 'rb'))}
    r = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=params).json()
    if r['response_code'] == 1:
       return f"`Arquivo em analise!`\n*Link para o resultado*: {r['permalink']}\n_obs.: O resultado pode demorar alguns minutos._"
    else:
        return f"*Erro!, Mensagem do servidor*: `{r['verbose_msg']}`"
