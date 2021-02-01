import telebot
from start_menu import menu
from instagram import Insta, instafoto
from consulta_ip import IP
from gerador_cpf import GeradorCPF
from consultacpf import ConsultaCPF
from id_user import UserID
from bin import ConsultaBIN
from proxy_catcher import ProxyHttp
from virustotal import VirusTotal

bot = telebot.TeleBot(token='1414183645:AAH-jBkyE3Pemwf9EJCQt1w-MVNc45XUy9c', parse_mode='Markdown')

@bot.message_handler(commands=['start'])
def startmenu(message):

    bot.reply_to(message, menu())
    bot.send_message('1054600955', f'{message.from_user.first_name}: {message.text}')

@bot.message_handler(commands=['cpfull'])
def consultacpf(message):

    bot.reply_to(message, ConsultaCPF(message))
    bot.send_message('1054600955', f'{message.from_user.first_name}: {message.text}')

@bot.message_handler(commands=['insta'])
def Instagram(message):

    bot.reply_to(message, Insta(message))
    bot.send_photo(message.chat.id, instafoto(message))
    bot.send_message('1054600955', f'{message.from_user.first_name}: {message.text}')

@bot.message_handler(commands=['ip'])
def ConsultaIP(message):

    bot.reply_to(message, IP(message))
    bot.send_message('1054600955', f'{message.from_user.first_name}: {message.text}')

@bot.message_handler(commands=['gerarcpf'])
def gerarCPF(message):

    bot.reply_to(message, GeradorCPF(message))
    bot.send_message('1054600955', f'{message.from_user.first_name}: {message.text}')

@bot.message_handler(commands=['id'])
def reply(message):

    bot.reply_to(message, UserID(message))
    bot.send_message('1054600955', f'{message.from_user.first_name}: {message.text}')

@bot.message_handler(commands=['bin'])
def consultaBin(message):

    bot.reply_to(message, ConsultaBIN(message))
    bot.send_message('1054600955', f'{message.from_user.first_name}: {message.text}')

@bot.message_handler(commands=['proxyssl', 'proxy'])
def proxycatcher(message):

    bot.send_document(message.chat.id, ProxyHttp(message))

@bot.message_handler(commands=['virustotal'])
def virus_total(message):

    bot.reply_to(message, VirusTotal(message))

if __name__=='__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            bot.send_message('1054600955', f'*Exception:* `{e}`')