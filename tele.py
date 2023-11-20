from telegram import *
from telegram.ext import *

bot = Bot("6842276666:AAFCCo0QcVH0PqFMlteQApxF5_avDDgsrw4")
#print(bot.get_me())
updater = Updater("DealsLoooterHub_bot", use_context=True)

dispatcher= updater.dispatcher


def test_func(update:Update, context:CallbackContext):
    bot.send_message(hi
        chat_id = update.effective_chat.id,
        text ="tutorial link : https://youtu.be/Tm5u97I7OrM",
    )
start_value = CommandHandler('motion_detection',test_func)

dispatcher.add_handler(start_value)

updater.start_polling()
