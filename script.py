import os
import configs

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello, world!"
    )


def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=update.message.text
    )


def register(update, context):
    message = ' '.join(context.args)

    context.bot.send_message(
        chat_id=os.getenv('TELEGRAM_CHANNEL_ID'),
        text=message
    )

if __name__ == '__main__':
    updater = Updater(
        token=os.getenv('TELEGRAM_BOT_TOKEN'),
        use_context=True
    )

    dispatcher = updater.dispatcher
    handlers = (
        CommandHandler('start', start),
        CommandHandler('register', register),
        MessageHandler(Filters.text, echo)
    )

    for handler in handlers:
        dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()
