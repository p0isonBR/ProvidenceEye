from requests import get

def Insta(message):
    
    user = message.text.replace('/insta', '').replace(' ', '').replace('@', '') 
    cookies = '' #necessario adicionar cookies para o funcionamento, recomendo criar uma conta apenas para essa finalidade
    h = {
        'Host': 'www.instagram.com',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'cookie': cookies
    }

    i = get(f'https://www.instagram.com/{user}/?__a=1', headers=h).json()
    nome = i['graphql']['user']['full_name']
    bio = i['graphql']['user']['biography']
    seguidores = i['graphql']['user']['edge_followed_by']['count']
    seguindo = i['graphql']['user']['edge_follow']['count']
    privada = i['graphql']['user']['is_private']
    verificada = i['graphql']['user']['is_verified']
    imagem = i['graphql']['user']['profile_pic_url_hd']
    user_id = i['graphql']['user']['id']
    posts = i['graphql']['user']['edge_owner_to_timeline_media']['count']
    url = i['graphql']['user']['external_url']

    return f'''*Username*: `@{user}`
*Nome*: `{nome}`
*Bio*: `{bio}`
*Site*: `{url}`
*Seguidores*: `{'{0:,}'.format(seguidores)}`
*Seguindo*: `{'{0:,}'.format(seguindo)}`
*Posts*: `{'{0:,}'.format(posts)}`
*Privada*: `{'Sim' if privada == True else 'Nao'}`
*Verificada*: `{'Sim' if verificada == True else 'Nao'}`
*User ID*: `{user_id}`
*Imagem do perfil: *'''

def instafoto(message):

    user = message.text.replace('/insta', '').replace(' ', '').replace('@', '') 
    cookies = '' #necessario adicionar cookies para o funcionamento, recomendo criar uma conta apenas para essa finalidade
    h = {
        'Host': 'www.instagram.com',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'cookie': cookies
    }

    i = get(f'https://www.instagram.com/{user}/?__a=1', headers=h).json()
    imagem = i['graphql']['user']['profile_pic_url_hd']
    foto = open('out.jpg', 'wb')
    foto.write(get(imagem).content)
    foto.close()
    foto = open('out.jpg', 'rb')

    return foto
