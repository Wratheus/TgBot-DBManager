from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from echo.config import *


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет, давай начнем работу!")

def random_text(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Для полного списка команд напишите /help")


def main():
    updater = Updater(token=TG_TOKEN)

    start_handler = CommandHandler('start', start)

    random_handler = MessageHandler(Filters.text & (~Filters.command), random_text)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(random_handler)

    updater.start_polling()
    updater.idle()