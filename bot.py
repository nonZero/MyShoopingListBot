import logging

from telegram import Update
from telegram.ext import (
    CommandHandler,
    CallbackContext,
    MessageHandler,
    Filters,
    Updater,
)

import bot_settings
from dict_storage import DictStorage

WELCOME_TEXT = "Enter your shopping items and I will save them for you. "

logging.basicConfig(
    format="[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

storage = DictStorage()


def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    logger.info(f"> Start chat #{chat_id}")
    context.bot.send_message(chat_id=chat_id, text=WELCOME_TEXT)


def list_items(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    logger.info(f"> Getting list for chat #{chat_id}")
    items = storage.list_items_for_chat(chat_id)
    if not items:
        msg = "No items."
    else:
        msg = ''.join(f"* {x}\n" for x in items)
        msg = f"Your items:\n{msg}"
    context.bot.send_message(chat_id=chat_id, text=msg)


def respond(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    text = update.message.text
    logger.info(f"= Got on chat #{chat_id}: {text!r}")
    storage.add_item_for_chat(chat_id, text)
    response = f"Added item: {text}."
    context.bot.send_message(chat_id=update.message.chat_id, text=response)


my_bot = Updater(token=bot_settings.BOT_TOKEN, use_context=True)
my_bot.dispatcher.add_handler(CommandHandler("start", start))
my_bot.dispatcher.add_handler(CommandHandler("list", list_items))
my_bot.dispatcher.add_handler(MessageHandler(Filters.text, respond))

logger.info("* Start polling...")
my_bot.start_polling()  # Starts polling in a background thread.
my_bot.idle()  # Wait until Ctrl+C is pressed
logger.info("* Bye!")
