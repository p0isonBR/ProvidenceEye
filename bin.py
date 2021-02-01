from requests import get

def ConsultaBIN(message):

    try:
        r = get('https://lookup.binlist.net/' + message.text.replace('/bin ', '')).json()
        band = r.get('scheme').capitalize()
        tipo = r.get('type').capitalize() + 'o'
        pais = r.get('country')
        paisnome = pais.get('name').capitalize()
        paisemoji = pais.get('emoji')
        banco = r.get('bank')
        nivel = r.get('brand').capitalize()

        return f'''
*Bandeira*: `{band}`
*Tipo*: `{tipo}`
*Nivel*: `{nivel}`
*Pais*: `{paisnome}` {paisemoji}
*Banco*: `{banco.get('name').capitalize()}`'''

    except(ValueError, AttributeError):
        return '`Bin invalido`'
