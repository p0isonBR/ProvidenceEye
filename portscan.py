import socket

def scan(message):

    ip = message.text.replace('https://', '').replace('http://', '').replace('/scan ', '')

    portas = {
        21: 'ftp',
        22: 'ssh',
        23: 'telnet',
        25: 'smtp',
        53: 'domain',
        80: 'http',
        110: 'pop3',
        111: 'rpcbind',
        135: 'RPC',
        139: 'netbios',
        143: 'imap',
        443: 'https',
        445: 'microsoft-ds',
        993: 'imaps',
        995: 'pop3s',
        1723: 'pptp',
        3306: 'mysql',
        3389: 'RDP',
        5900: 'vnc',
        8080: 'http-proxy'
        }

    texto = ''

    for key, value in portas.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5)
        code = s.connect_ex((ip, key))
        if code == 0:
            texto = texto + f'*Porta* `{key} {value}` *=>* _Aberta_\n'

    return texto if len(texto) > 1 else '`Nenhuma porta aberta`'