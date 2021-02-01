from requests import get

def IP(message):

    men = message.text.replace('https://', '').replace('http://', '').replace('/ip ', '')
    if len(men) < 4:
        return '`Formato invalido!`\n`Ex`: *8.8.8.8* `ou` *google.com*.'

    else:
        r = get('http://ip-api.com/json/' + men).json()

        return f'''
*IP*: `{r.get('query')}`
*Pais*: `{r.get('country')}`
*Estado*: `{r.get('regionName')}`
*Cidade*: `{r.get('city')}`
*Provedor*: `{r.get('isp')}`'''