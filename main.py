#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# BOT que encaminha mensagens aleatórias de um canal do telegram
"""
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from random import randint
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    update.message.reply_text('Olá! Eu sou o BotFwd e existo unicamente para'
                              ' causar o desconforto nas pessoas!')
    bot.send_message(chat_id=update.message.chat_id, 
                     text="Meus comandos:\n"
                          "Iniciar o bot: /start\n"
                          "Mensagem aleatória: /random\n"
                          "Ajuda: /help")
    

def help(bot, update):
    update.message.reply_text('Sem ajuda malandro!')


def random(bot, update):
# update.message.reply_text('Chat ID: %s' % update.message.chat_id)
# bot.send_message(update.message.chat_id,
# text="Message ID: %s" % update.message.message_id)
    bot.forwardMessage(update.message.chat_id, '@ofwdnovo', 
                       randint(3, 65))
    
def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("390975324:AAG57sa1pBQ9Swk7ry-I4FJijWOc1XZYM5s")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("random", random))

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    print('BOT started')

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
