from django.core.management import BaseCommand
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from Valyuta_kurs.settings import TOKEN
from V_bot.views import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        updater = Updater(TOKEN)

        updater.dispatcher.add_handler(CommandHandler("start", start))
        updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

        updater.start_polling()
        updater.idle()