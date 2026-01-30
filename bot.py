import telebot
import os

BOT_TOKEN = os.getenv("967946148")

bot = telebot.TeleBot(8206535171:AAHusE-vfyzbzmgSG6O2MoM9ypboAY5rZ2Y)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "هلا بيك 👋 البوت شغّال ✅")

@bot.message_handler(func=lambda m: True)
def forward(message):
    bot.forward_message(
        chat_id=7967946148,
        from_chat_id=message.chat.id,
        message_id=message.message_id
    )

bot.infinity_polling()
