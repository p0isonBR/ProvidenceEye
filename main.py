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
from portscan import scan
from placa import consultaplaca
from gerar_pessoa import gerarPessoa

bot = telebot.TeleBot(token='', parse_mode='Markdown')


@bot.message_handler(commands=['start'])
def startmenu(message):
    bot.reply_to(message, menu())


@bot.message_handler(commands=['cpfull'])
def consultacpf(message):
    bot.reply_to(message, ConsultaCPF(message))


@bot.message_handler(commands=['insta'])
def Instagram(message):
    bot.reply_to(message, Insta(message))
    bot.send_photo(message.chat.id, instafoto(message))


@bot.message_handler(commands=['ip'])
def ConsultaIP(message):
    bot.reply_to(message, IP(message))


@bot.message_handler(commands=['gerarpessoa'])
def GeradorPessoa(message):
    bot.reply_to(message, gerarPessoa())


@bot.message_handler(commands=['gerarcpf'])
def gerarCPF(message):
    bot.reply_to(message, GeradorCPF(message))


@bot.message_handler(commands=['id'])
def reply(message):
    bot.reply_to(message, UserID(message))


@bot.message_handler(commands=['bin'])
def consultaBin(message):
    bot.reply_to(message, ConsultaBIN(message))


@bot.message_handler(commands=['proxyssl', 'proxy'])
def proxycatcher(message):
    bot.send_document(message.chat.id, ProxyHttp(message))


@bot.message_handler(commands=['virustotal'])
def virus_total(message):
    bot.reply_to(message, VirusTotal(message))


@bot.message_handler(commands=['scan'])
def scanports(message):
    bot.reply_to(message, scan(message))


@bot.message_handler(commands=['placa'])
def consulta_placa(message):
    bot.reply_to(message, consultaplaca(message))


if __name__=='__main__':
    feedback_chat = '' #Insira um Chat ID pra receber os "excepts" do bot, e monitora-lo. pode ser seu proprio, ou de um grupo.
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            bot.send_message(feedback_chat, f'*Exception:* `{e}`')
