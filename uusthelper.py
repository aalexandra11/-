import telebot
from telebot import types


bot=telebot.TeleBot('')
@bot.message_handler(content_types=['photo'])
def getphotomess(message):
    bot.reply_to(message,'Классное фото, но зачем🧐')
@bot.message_handler(content_types=['voice'])
def getaudioomess(message):
    bot.reply_to(message,'не хочу слушать, эммм')
@bot.message_handler(commands=['start','привет','Привет'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('👩‍💻 Открыть ИСУ/Open ISU 👩‍💻','https://isu.uust.ru/')
    btn2 = types.InlineKeyboardButton('📅 Расписание/Schedule 📅', callback_data='schedule')
    btn3 = types.InlineKeyboardButton('🅿️ Парковки/Parking place 🅿️',callback_data='parking')
    btn4 = types.InlineKeyboardButton('🗺️ Карта Университета/University map 🗺️', callback_data='map')
    btn5 = types.InlineKeyboardButton('🪩 Скорые мероприятия/Upcomming events 🪩',callback_data='events')
    btn6 = types.InlineKeyboardButton('🍱 Где покушать/Where can go to eat 🍱',callback_data='eat')
    btn7 = types.InlineKeyboardButton('🔎 Быстрый поисковик Yandex 🔍','https://dzen.ru/?clid=2233626&yredirect=true')
    btn8 = types.InlineKeyboardButton('🍽️ Доставка еды 🍽️', callback_data='food')
    btn9 = types.InlineKeyboardButton('🚗 Такси 🚗', callback_data='tax')
    btn10 = types.InlineKeyboardButton('🚨 Аптеки 🚨', callback_data='apt')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn4)
    markup.row(btn6)
    markup.row(btn5)
    markup.row(btn3)
    markup.row(btn7)
    markup.row(btn8)
    markup.row(btn9)
    markup.row(btn10)
    bot.send_message(message.chat.id,'Привет!', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):

    if call.data == 'schedule':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1️⃣', callback_data='gr1')
        btn2 = types.InlineKeyboardButton('2️⃣', callback_data='gr2')
        btn3 = types.InlineKeyboardButton('3️⃣', callback_data='gr3')
        btn4 = types.InlineKeyboardButton('4️⃣', callback_data='gr4')
        markup.row(btn1, btn2)
        markup.row(btn3,btn4)
        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Выберите номер курса',
            reply_markup=markup
        )
    elif call.data == 'food':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('delivery club', 'https://market-delivery.yandex.ru/moscow?shippingType=delivery')
        btn2 = types.InlineKeyboardButton('Самокат', 'https://samokat.ru/?ysclid=mfwi1bbyfa848881559')
        btn3 = types.InlineKeyboardButton('Яндекс еда', 'https://eda.yandex.ru/moscow?shippingType=delivery')
        btn4 = types.InlineKeyboardButton('Купер', 'https://kuper.ru/?utm_referrer=https%3a%2f%2fyandex.ru%2f')
        markup.row(btn1, btn2)
        markup.row(btn3,btn4)
        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Выберите заведение, в котором хотите покушать',
            reply_markup=markup
        )
    elif call.data == 'tax':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('🚕 Yandex GO 🚕',
                                          'https://taxi.yandex.ru/?ysclid=mfwiar5t6q617677941')
        btn2 = types.InlineKeyboardButton('🚕 Максим 🚕', 'https://ufa.taximaxim.ru/?ysclid=mfwiboxfgy828446211')
        btn3 = types.InlineKeyboardButton('🚕 Везет 🚕', 'https://vezet.ru/ufa?ysclid=mfwical2c3975498416')
        btn4 = types.InlineKeyboardButton('🚕 Поехали 🚕', 'https://ufa.taxipoehali.ru/client/?intl=ru-RU&ysclid=mfwides7rk369543506')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Выберите заведение, в котором хотите покушать',
            reply_markup=markup
        )

    elif call.data == 'eat':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('☕️ Кафе ☕️', 'https://yandex.ru/maps/172/ufa/search/%D0%9A%D0%BE%D1%84%D0%B5%D0%B9%D0%BD%D0%B8/?ll=55.946478%2C54.726154&sll=55.946478%2C54.725194&source=serp_navig&sspn=0.024166%2C0.009491&z=15.58')
        btn2 = types.InlineKeyboardButton('🦪 Рестораны 🦪', 'https://yandex.ru/maps/172/ufa/category/restaurant/184106394/?ll=55.952356%2C54.728077&sll=55.952356%2C54.728077&source=serp_navig&sspn=0.065115%2C0.025572&z=14.41')
        btn3 = types.InlineKeyboardButton('🍲 Столовые 🍲', 'https://yandex.ru/maps/172/ufa/category/canteen/184106396/?ll=55.952356%2C54.728077&sll=55.946478%2C54.726154&source=serp_navig&sspn=0.028938%2C0.011365&z=14.41')
        markup.row(btn1, btn2)
        markup.row(btn3)
        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Выберите заведение, в котором хотите покушать',
            reply_markup=markup
        )

    elif call.data == 'parking':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('🅿️🆓 Бесплатная парковка 🆓🅿️', callback_data='free')
        btn2 = types.InlineKeyboardButton('🅿️💰 Платная парковка 💰🅿️', 'https://yandex.ru/maps/172/ufa/search/%D0%9F%D0%BB%D0%B0%D1%82%D0%BD%D1%8B%D0%B5%20%D0%BF%D0%B0%D1%80%D0%BA%D0%BE%D0%B2%D0%BA%D0%B8/?l=carparks&ll=55.946850%2C54.724038&sll=55.952356%2C54.728077&source=serp_navig&sspn=0.065115%2C0.025572&z=16.21')
        markup.row(btn1, btn2)

        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Информация о парковке',
            reply_markup = markup
        )

    elif call.data == 'apt':
        markup = types.InlineKeyboardMarkup()

        btn2 = types.InlineKeyboardButton('🚨 Аптеки 🚨',
                                          'https://yandex.ru/maps/172/ufa/category/pharmacy/184105932/?ll=55.942396%2C54.722807&sll=55.940708%2C54.722886&source=serp_navig&sspn=0.013500%2C0.005303&z=15.85')
        markup.row(btn2)

        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='ближайшие аптеки',
            reply_markup=markup
        )

    elif call.data == 'free':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='тут должно быть фото и какой-то текст'
        )

    elif call.data == 'map':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1️⃣', callback_data='k1')
        btn2 = types.InlineKeyboardButton('2️⃣', callback_data='k2')
        btn3 = types.InlineKeyboardButton('3️⃣', callback_data='k3')
        btn4 = types.InlineKeyboardButton('4️⃣', callback_data='k4')
        btn5 = types.InlineKeyboardButton('5️⃣', callback_data='k5')
        btn6 = types.InlineKeyboardButton('6️⃣', callback_data='k6')
        btn7 = types.InlineKeyboardButton('7️⃣', callback_data='k7')
        btn8 = types.InlineKeyboardButton('8️⃣', callback_data='k8')
        btn9 = types.InlineKeyboardButton('9️⃣', callback_data='k9')
        markup.row(btn1, btn2,btn3 ,btn4)
        markup.row(btn5,btn6,btn7,btn8,btn9)

        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)

        # Удаляем старое сообщение с текстовым меню
        bot.delete_message(call.message.chat.id, call.message.message_id)

        # Отправляем фото по ссылке + текст + кнопки
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo='https://uust.ru/media/uploads/ckeditor/2023/06/26/image-20230626151216-1.jpeg',  # Ваша ссылка на карту
            caption='🗺️ Карта Университета\n\nЗдесь вы можете увидеть расположение всех корпусов университета. Выберите номер корпуса для получения подробной информации:',
            reply_markup=markup
        )

    elif call.data == 'k1':
        markup = types.InlineKeyboardMarkup()
        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(
            chat_id=call.message.chat.id,
            text='1 этаж\nКоворкинг\nКофе\nГардероб\nМужской туалет\n\n2 этаж\nКоворкинг зона\nАвиатрон\nЖенский туалет\nБеспроводные рабочие зарядки\nЗона отдыха (диваны)\n\n3 этаж\nЖенский туалет\nЗона отдыха (диваны)\n\n4 этаж\nДеканат\nЖенский туалет\nЗона для отдыха\n\n5 этаж\nМужской туалет\nЗона для отдыха',
            reply_markup = markup
        )

    elif call.data == 'k2':
        markup = types.InlineKeyboardMarkup()
        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(
            chat_id=call.message.chat.id,
            text='тут должна быть инфа о 2 корпусе',
            reply_markup = markup
        )

    elif call.data == 'k3':
        markup = types.InlineKeyboardMarkup()
        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(
            chat_id=call.message.chat.id,
            text='тут должна быть инфа о 3 корпусе',
            reply_markup=markup
        )

    elif call.data == 'k4':
        markup = types.InlineKeyboardMarkup()
        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(
            chat_id=call.message.chat.id,
            text='тут должна быть инфа о 4 корпусе',
            reply_markup=markup
        )

    elif call.data == 'k5':
        markup = types.InlineKeyboardMarkup()
        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(
            chat_id=call.message.chat.id,
            text='тут должна быть инфа о 5 корпусе',
            reply_markup=markup
        )

    elif call.data == 'k6':
        markup = types.InlineKeyboardMarkup()
        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo='https://downloader.disk.yandex.ru/preview/6e959a64e00fda35caed0d20d6ef8e45b98c2c545ebe42ff3393d6b02a0e0ee1/68d432b2/S4rcOjQKVYIPa-QOdtvKAax8LXzoYIjWrfoQ416n3p78oYdZ4ISbt57rTpqzB_u7OWDPdgszlRXM_rXoG8OyGw%3D%3D?uid=0&filename=%D0%9A%D0%B0%D1%80%D1%82%D0%B0_1_%D0%AD%D1%82%D0%B0%D0%B6.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v3&size=2048x2048',
            caption='🗺\n\n1 этаж\nКоворкинг\nКофе\nГардероб\nМужской туалет\n\n2 этаж\nКоворкинг зона\nАвиатрон\nЖенский туалет\nБеспроводные рабочие зарядки\nЗона отдыха (диваны)\n\n3 этаж\nЖенский туалет\nЗона отдыха (диваны)\n\n4 этаж\nДеканат\nЖенский туалет\nЗона для отдыха\n\n5 этаж\nМужской туалет\nЗона для отдыха',
            reply_markup=markup
        )

    elif call.data == 'k7':
        markup = types.InlineKeyboardMarkup()
        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(
            chat_id=call.message.chat.id,
            text='тут должна быть инфа о 7 корпусе',
            reply_markup=markup
        )

    elif call.data == 'k8':
        markup = types.InlineKeyboardMarkup()
        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(
            chat_id=call.message.chat.id,
            text='тут должна быть инфа о 8 корпусе',
            reply_markup=markup
        )

    elif call.data == 'k9':
        markup = types.InlineKeyboardMarkup()
        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)
        bot.send_message(
            chat_id=call.message.chat.id,
            text='тут должна быть инфа о 9 корпусе',
            reply_markup=markup
        )

    elif call.data == 'events':
        markup = types.InlineKeyboardMarkup()
        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Предстоящие события: https://vk.com/wall-216069379_2920 ',
            reply_markup = markup
        )

    elif call.data == 'gr1':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('ТОП-101Б 1️⃣', callback_data='top1')
        btn2 = types.InlineKeyboardButton('ТОП-102И 2️⃣', callback_data='top2')
        btn3 = types.InlineKeyboardButton('💖 ТОП-103Б 💖', callback_data='top3')
        btn4 = types.InlineKeyboardButton('ТОП-104Б4️⃣', callback_data='top4')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Выберите группу',
            reply_markup = markup
        )

    elif call.data == 'top3':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('эта неделя', 'https://isu.uust.ru/schedule_2024/')
        btn2 = types.InlineKeyboardButton('следущая неделя', 'https://isu.uust.ru/schedule_2024/')
        markup.row(btn1, btn2)
        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Выберите неделю',
            reply_markup = markup
        )

    elif call.data == 'top1':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Расписание на сегодня:\n\n9:00 - Математика (ауд. 101)\n11:00 - Физика (ауд. 205)\n14:00 - Программирование (ауд. 310)'
        )

    elif call.data == 'top2':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Расписание на сегодня:\n\n9:00 - Математика (ауд. 101)\n11:00 - Физика (ауд. 205)\n14:00 - Программирование (ауд. 310)'
        )

    elif call.data == 'top4':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Расписание на сегодня:\n\n9:00 - Математика (ауд. 101)\n11:00 - Физика (ауд. 205)\n14:00 - Программирование (ауд. 310)'
        )

    elif call.data == 'gr2':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Расписание на сегодня:\n\n9:00 - Математика (ауд. 101)\n11:00 - Физика (ауд. 205)\n14:00 - Программирование (ауд. 310)'
        )
    elif call.data == 'gr3':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Расписание на сегодня:\n\n9:00 - Математика (ауд. 101)\n11:00 - Физика (ауд. 205)\n14:00 - Программирование (ауд. 310)'
        )
    elif call.data == 'gr4':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Расписание на сегодня:\n\n9:00 - Математика (ауд. 101)\n11:00 - Физика (ауд. 205)\n14:00 - Программирование (ауд. 310)'
        )

    elif call.data == 'back_main':
        # Возврат к главному меню
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('👩‍💻 ИСУ Личный кабинет/ISU Personal account 👩‍💻', url='http://isu.uust.ru/')
        btn2 = types.InlineKeyboardButton('📅 Расписание/Schedule 📅', callback_data='schedule')
        btn3 = types.InlineKeyboardButton('🅿️ Парковка/Parking place 🅿️', callback_data='parking')
        btn4 = types.InlineKeyboardButton('🗺️ Карта университета/University map 🗺️', callback_data='map')
        btn5 = types.InlineKeyboardButton('🪩 Предстоящие события/Upcomming events 🪩', callback_data='events')
        btn6 = types.InlineKeyboardButton('🍱 Где покушать/Where can go to eat 🍱',callback_data='eat')
        btn7 = types.InlineKeyboardButton('🔎 Быстрый поисковик Yandex 🔍',
                                          'https://dzen.ru/?clid=2233626&yredirect=true')
        btn8 = types.InlineKeyboardButton('🍽️ Доставка еды 🍽️', callback_data='food')
        btn9 = types.InlineKeyboardButton('🚗 Такси 🚗', callback_data='tax')
        btn10 = types.InlineKeyboardButton('🚨 Аптеки 🚨', callback_data='apt')
        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn4)
        markup.row(btn6)
        markup.row(btn5)
        markup.row(btn3)
        markup.row(btn7)
        markup.row(btn8)
        markup.row(btn9)
        markup.row(btn10)

        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(
            chat_id=call.message.chat.id,
            text='Главное меню:',
            reply_markup=markup
        )

bot.polling(none_stop=True)
