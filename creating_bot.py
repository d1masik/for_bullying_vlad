import telebot

bot = telebot.TeleBot('582709386:AAHtgpKQAIT0jbrfrGLh4aaN_wom6ZkHTBk')


@bot.message_handler(content_types=['text'])
def send_vlad(message):
    mes = message.text.lower()
    if mes.find('влад') != -1 or mes.find('@vladilija') != -1:
        bot.send_sticker(message.chat.id, 'CAADAgADCwADuDxkCK0DhOOwlYB7Ag')


bot.polling(none_stop=True)
