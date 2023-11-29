import telebot
from telebot import types
bot = telebot.TeleBot('6678823538:AAFdoXOV8rQFF2r7O3IsVaOhPhmPhbcHoRw')


@bot.message_handler(commands=['start'])
def main_function(message):
    user = bot.send_message(message.chat.id,
                            text='Привіт, чим можу допомогти?',
                            reply_markup=keyboard())
    bot.register_next_step_handler(user, check_user_do)


def check_user_do(message):
    if message.text == 'Інформація ℹ':
        bot.send_message(message.chat.id,
                         text=f'Бот працює в тестовому режимі.'
                         )

    elif message.text == 'Розказати анекдот':
        foto = open('ne_mogy.jpeg', 'rb')
        bot.send_photo(message.chat.id, foto)
        bot.send_message(message.chat.id,
                         text=f'😶')


def keyboard():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    info_button = types.KeyboardButton(text='Інформація ℹ')

    last_step = types.KeyboardButton(text='Розказати анекдот')
    buttons.add(info_button, last_step)
    return buttons


if __name__ == '__main__':
    bot.polling(non_stop=True)
