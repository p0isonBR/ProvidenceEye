import requests

def VirusTotal(message):
    bot_token = ''
    arq = message.json
    arq = arq['reply_to_message']['document']['file_id']
    arq = requests.get(f'https://api.telegram.org/bot{bot_token}/getFile?file_id={arq}').json()
    f = arq['result']['file_path']
    arq = f'https://api.telegram.org/file/bot{bot_token}/' + f
    with open(f.split('/')[1], 'wb') as file:
        file.write(requests.get(arq).content)
        file.close()

    params = {'apikey': 'd1da02ce15b0aea70477b0929a67528e0f4f18f11bcb76bcf43760331bb59699'} #Deixei minha API Key do Virus Total, porem recomendo criar uma propria, pelos limites impostos a APIs Free.
    files = {'file': (f.split('/')[1], open(f.split('/')[1], 'rb'))}
    r = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=params).json()
    if r['response_code'] == 1:
       return f"`Arquivo em analise!`\n*Link para o resultado*: {r['permalink']}\n_obs.: O resultado pode demorar alguns minutos._"
    else:
        return f"*Erro!, Mensagem do servidor*: `{r['verbose_msg']}`"
