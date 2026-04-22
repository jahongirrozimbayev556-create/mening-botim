import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8773058966:AAHMOW5PvqslYMHrmsRjAKNRjsnD3HYp3J4"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton("🎱 Billiard Pro ni ochish", url="https://billiard-kappa.vercel.app/")
    markup.add(btn)
    bot.send_message(message.chat.id, "Salom! 👋\nQuyidagi tugmani bosing:", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def javob(message):
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton("🎱 Billiard Pro ni ochish", url="https://billiard-kappa.vercel.app/")
    markup.add(btn)
    bot.send_message(message.chat.id, "Dasturni ochish uchun tugmani bosing:", reply_markup=markup)

print("Bot ishga tushdi...")
bot.infinity_polling()