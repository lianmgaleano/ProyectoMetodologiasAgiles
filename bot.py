from config import bot
import config
from time import sleep
import re
import logica.logic as logic
from logica.logicaPersona import LogicaPersona
import basedatos.bd as bd

#########################################################

if __name__ == '__main__':
     bd.Base.metadata.create_all( bd.engine)

#########################################################

#START
@bot.message_handler(commands=['start'])
def on_command_start(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)

    bot.send_message(
        message.chat.id,
        logic.get_welcome_message(bot.get_me()),
        parse_mode="Markdown")

    bot.send_message(
        message.chat.id,
        logic.get_help_message(),
        parse_mode="Markdown")

    #logic.register_account(message.from_user.id)

#########################################################

#Registrar Mecánico
@bot.message_handler(regexp=r"^(registrar mecánico|registrar mecanico|rm) ([a-zA-Z0-9]{6,15}), ([a-zA-Z0-9Á-Ü,\s]{3,100})$")
def on_registrar_mecanico(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)

    parts = re.match(
        r"^(registrar mecánico|registrar mecanico|rm) ([a-zA-Z0-9]{6,15}), ([a-zA-Z0-9Á-Ü,\s]{3,100})$",
        message.text,
        flags=re.IGNORECASE)

    documento = parts[2]
    nombre = parts[3]

    control = LogicaPersona.registrar_persona (documento, nombre, "2")
    bot.reply_to(message,f"\U0001F527 ¡Mecánico registrado!" 
                    if control == True 
                    else "\U000026A0 El mecánico ya se encuentra registrado, ejecuta /start y vuelve a intentarlo" )  


#########################################################

#Registrar Dueño
@bot.message_handler(regexp=r"^(registrar dueño|rd) ([a-zA-Z0-9]{6,15}), ([a-zA-Z0-9Á-Ü,\s]{3,100})$")
def on_registrar_dueno(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)

    parts = re.match(
        r"^(registrar dueño|rd) ([a-zA-Z0-9]{6,15}), ([a-zA-Z0-9Á-Ü,\s]{3,100})$",
        message.text,
        flags=re.IGNORECASE)

    documento = parts[2]
    nombre = parts[3]

    control = LogicaPersona.registrar_persona (documento, nombre, "1")
    bot.reply_to(message,f"\U0001F9D4 ¡Dueño registrado!" 
                    if control == True 
                    else "\U000026A0 El dueño ya se encuentra registrado, ejecuta /start y vuelve a intentarlo" )

#########################################################

#HELP
@bot.message_handler(commands=['help'])
def on_command_help(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)

    bot.send_message(
        message.chat.id,
        logic.get_help_message(),
        parse_mode="Markdown") 

#########################################################

#ABOUT
@bot.message_handler(commands=['about'])
def on_command_about(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)

    bot.send_message(
        message.chat.id,
        logic.get_about_this(config.VERSION),
        parse_mode="Markdown")

#########################################################
#FALLBACK
@bot.message_handler(func=lambda message: True)
def on_fallback(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)

    response = logic.get_fallback_message(message.text)
    bot.reply_to(message, response)

#########################################################

if __name__ == '__main__':
    bot.polling(timeout=20)

#########################################################