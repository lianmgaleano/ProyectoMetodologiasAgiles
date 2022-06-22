from config import bot
import config
from time import sleep
import re
import logic
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