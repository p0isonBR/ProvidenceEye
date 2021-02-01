from requests import get

def ProxyHttp(message):
    if ('proxyssl') in message.text:
        proxy = get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=yes&anonymity=all&simplified=true').content
        txt = open('ProxySSL.txt', 'wb')
        txt.write(proxy)
        txt.close()
        txt = open('ProxySSL.txt', 'r')
        return txt

    else:
        proxy = get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=no&anonymity=all&simplified=true').content
        txt = open('ProxyHTTP.txt', 'wb')
        txt.write(proxy)
        txt.close()
        txt = open('ProxyHTTP.txt', 'r')
        return txt