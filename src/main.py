import config
import telebot
from telebot import types
from database import addUserId
from database import getUserBalance
from database import getuserid

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    shop = types.InlineKeyboardButton('Магазин', callback_data= 'magaz')
    profile = types.InlineKeyboardButton('Профиль', callback_data = 'profil')
    supp = types.InlineKeyboardButton('Поддержка', callback_data = 'supp')
    ozivi = types.InlineKeyboardButton('Отзывы', url='https://t.me/shopbotrevs')
    markup.add(shop, profile, supp, ozivi)
    mainmen = open('icons/mainmenu.png', 'rb')
    bot.send_photo(message.chat.id, mainmen, reply_markup=markup)
    addUserId(message)
    
def answerbot(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
    markup.add(backbtn)
    bot.send_message(message.chat.id, '<b>Напишите логин Steam аккаунта, на который хотите пополнить баланс: \n Пополняем аккаунты Steam созданные в странах: Россия, Беларусь, Казахстан, Киргизия (Кыргызстан), Армения,  Таджикистан, Узбекистан, Азербайджан, Молдова, Украина.</b>', parse_mode="html", reply_markup=markup)

def step(message):
    if message.text.isalpha():
        bot.send_message(message.chat.id, 'Введите верное значение')
    if message.text.isdigit():
        answerbot(message)
        


@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.message:
        if call.data == 'magaz':
            markup = types.InlineKeyboardMarkup(row_width=2)
            steam_dep = types.InlineKeyboardButton('Пополнение Steam', callback_data= 'dep')
            spotifypremium = types.InlineKeyboardButton('Spotify Премиум', callback_data = 'spoti')
            netsub = types.InlineKeyboardButton('Подписка на Netflix', callback_data = 'netflix')
            fort = types.InlineKeyboardButton('Fortnite', callback_data = 'fortnite')
            valorant = types.InlineKeyboardButton('Valorant', callback_data = 'valorant')
            ExitLag = types.InlineKeyboardButton('ExitLag', callback_data = 'exit')
            roblox = types.InlineKeyboardButton('Roblox', callback_data = 'Roblox')
            pubg = types.InlineKeyboardButton('PUBG MOBILE', callback_data = 'pubg')
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(steam_dep, spotifypremium, netsub, valorant, fort, ExitLag, roblox, pubg, backbtn)
            mainmen = open('icons/mainmenu.png', 'rb')
            bot.send_photo(call.message.chat.id, mainmen, reply_markup=markup)

        elif call.data == 'supp':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Написать в поддержку', url='https://github.com/kommo124/TarkovMapsBot'))
            markup.add(types.InlineKeyboardButton('FAQ', url='https://telegra.ph/prjct-FAQ-01-04'))
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(backbtn)
            supp = open('icons/support.png', 'rb')
            bot.send_photo(call.message.chat.id, supp, caption='<b>Если у вас есть какие либо вопросы, большинство ответов есть в нашем FAQ (https://telegra.ph/prjct-FAQ-01-04), если вы не нашли ответ на свой вопрос, то используйте кнопки ниже, чтобы найти ответ на ваш вопрос.Если вы не нашли ответ на свой вопрос, то можете обратиться в поддержку.</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'profil':
            markup = types.InlineKeyboardMarkup(row_width=1)
            deposit = types.InlineKeyboardButton('Пополнить баланс', callback_data = 'deposit')
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(deposit, backbtn)
            profile1 = open('icons/mainmenu.png', 'rb')
            bot.send_photo(call.message.chat.id, profile1, caption=getuserid(call.message), reply_markup=markup)

        elif call.data == 'dep':
            markup = types.InlineKeyboardMarkup(row_width=1)
            deposit2 = types.InlineKeyboardButton('Пополнение Steam', callback_data = 'dep2')
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(deposit2, backbtn)
            steamdep2 = open('icons/steam.png', 'rb')
            bot.send_photo(call.message.chat.id, steamdep2, caption='<b>Steam</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'dep2':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(backbtn)
            bot.send_message(call.message.chat.id, '<b>Пожалуйста, введите сумму пополнения (минимальная сумма 100 ₽):</b>', parse_mode="html", reply_markup=markup)
            bot.register_next_step_handler(call.message, step)

        elif call.data =='spoti':
            markup = types.InlineKeyboardMarkup(row_width=1)
            buyprem = types.InlineKeyboardButton('Spotify 1 месяц', callback_data = 'buyprem2')
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(backbtn, buyprem)
            prem22 = open('icons/spoti2.png', 'rb')
            bot.send_photo(call.message.chat.id, prem22, caption='<b>Коды Spotify Premium</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'buyprem2':
            markup = types.InlineKeyboardMarkup(row_width=1)
            buy = types.InlineKeyboardButton('Купить', callback_data = 'buy')
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(backbtn, buy)
            prem22 = open('icons/spoti2.png', 'rb')
            bot.send_photo(call.message.chat.id, prem22, caption='<b>Подписка на ваш аккаунт со входом. \n \nПодписку не продлеваем, можем покупать только на аккаунты, на которых она кончилась. \n \nЦена: 279 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'buy':
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton('Оплатить', url='https://github.com/kommo124/TarkovMapsBot'))
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(backbtn)
            prem22 = open('icons/spoti2.png', 'rb')
            bot.send_photo(call.message.chat.id, prem22, caption='<b>Ссылка на оплату будет действовать 10 минут \n \nЦена: 279 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'fortnite':
            markup = types.InlineKeyboardMarkup(row_width=2)
            vbucks = types.InlineKeyboardButton('В-Баксы', callback_data = 'credits')
            gift = types.InlineKeyboardButton('Подарком', callback_data = 'giftom')
            codes = types.InlineKeyboardButton('Коды', callback_data = 'code')
            region = types.InlineKeyboardButton('Смена региона', callback_data = 'reg')
            crew = types.InlineKeyboardButton('Отряд Fortnite', callback_data = 'crew')
            unlock = types.InlineKeyboardButton('Разблокировка XBOX', callback_data = 'xbox')
            take = types.InlineKeyboardButton('Получить награды', callback_data = 'take')
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(types.InlineKeyboardButton('Подключить аккаунт', url='https://github.com/kommo124/TarkovMapsBot'))
            markup.add(vbucks, gift, codes, region, crew, unlock, take, backbtn)
            main22 = open('icons/mainmenu.png', 'rb')
            bot.send_photo(call.message.chat.id, main22, caption='<b>Делаем покупки на все аккаунты</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'credits':
            markup = types.InlineKeyboardMarkup(row_width=2)
            xboxsom = types.InlineKeyboardButton('XBOX', callback_data = 'xboxson')
            turka = types.InlineKeyboardButton('Epic games Турция', callback_data = 'turciya')
            vbucks1 = types.InlineKeyboardButton('В-Баксы 100%', callback_data = 'vbucks2')
            ua = types.InlineKeyboardButton('Epic games Украина', callback_data = 'ucraine')
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(xboxsom, turka, vbucks1, ua, backbtn)
            vbucks = open('icons/bucks.png', 'rb')
            bot.send_photo(call.message.chat.id, vbucks, caption='<b>Советуем покупать любые предметы из магазина В-Баксами подарком (категория Подарком), так выйдет дешевле, быстрее и не будет никаких ошибок.\n\nЕсли вам нужны В-Баксы на аккаунт то выберите способ выполнения заказа:</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'xboxson':
            markup = types.InlineKeyboardMarkup(row_width=2)
            onek = types.InlineKeyboardButton('1000 В-Баксов | 749₽', callback_data = '1k')
            onek1 = types.InlineKeyboardButton('2800 В-Баксов | 1599₽', callback_data = '2k')
            onek2 = types.InlineKeyboardButton('5000 В-Баксов | 2399₽', callback_data = '5k')
            onek3 = types.InlineKeyboardButton('7800 В-Баксов | 3849₽', callback_data = '7k')
            onek4 = types.InlineKeyboardButton('13500 В-Баксов | 5999₽', callback_data = '13k')
            onek5 = types.InlineKeyboardButton('27000 В-Баксов | 11849₽', callback_data = '11k')
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(onek, onek1, onek2, onek3, onek4, onek5, backbtn)
            vbucks = open('icons/bucks.png', 'rb')
            bot.send_photo(call.message.chat.id, vbucks, caption='<b>Создать XBOX аккаунт можно по инструкции - \nhttps://teletype.in/@funpaykommo124/5GPH7WnVcly\n\nЕсли вы сделаете покупку данным способом выполнения заказа и мы не сможем сделать заказ про причине того, что вы не дочитали все условия, возвращаем деньги только на баланс </b>', parse_mode="html", reply_markup=markup)

        elif call.data == '1k':
            markup = types.InlineKeyboardMarkup(row_width=1)
            buy = types.InlineKeyboardButton('Купить', callback_data = 'buy2')
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(backbtn, buy)
            vbucks = open('icons/bucks.png', 'rb')
            bot.send_photo(call.message.chat.id, vbucks, caption='<b>1000 В-Баксов на ваш аккаунт через XBOX.\n\nЦена: 749 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'buy2':
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton('Оплатить', url='https://github.com/kommo124/TarkovMapsBot'))
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(backbtn)
            bucks22 = open('icons/bucks.png', 'rb')
            bot.send_photo(call.message.chat.id, bucks22, caption='<b>Ссылка на оплату будет действовать 10 минут \n \nЦена: 749 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == '2k':
            markup = types.InlineKeyboardMarkup(row_width=1)
            buy = types.InlineKeyboardButton('Купить', callback_data = 'buy3')
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(backbtn, buy)
            vbucks = open('icons/bucks.png', 'rb')
            bot.send_photo(call.message.chat.id, vbucks, caption='<b>2800 В-Баксов на ваш аккаунт через XBOX.\n\nЦена: 1599 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'buy3':
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton('Оплатить', url='https://github.com/kommo124/TarkovMapsBot'))
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(backbtn)
            bucks22 = open('icons/bucks.png', 'rb')
            bot.send_photo(call.message.chat.id, bucks22, caption='<b>Ссылка на оплату будет действовать 10 минут \n \nЦена: 1599 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == '5k':
            markup = types.InlineKeyboardMarkup(row_width=1)
            buy = types.InlineKeyboardButton('Купить', callback_data = 'buy4')
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(backbtn, buy)
            vbucks = open('icons/bucks.png', 'rb')
            bot.send_photo(call.message.chat.id, vbucks, caption='<b>5000 В-Баксов на ваш аккаунт через XBOX.\n\nЦена: 2399 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'buy4':
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton('Оплатить', url='https://github.com/kommo124/TarkovMapsBot'))
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(backbtn)
            bucks22 = open('icons/bucks.png', 'rb')
            bot.send_photo(call.message.chat.id, bucks22, caption='<b>Ссылка на оплату будет действовать 10 минут \n \nЦена: 2399 ₽</b>', parse_mode="html", reply_markup=markup)


        elif call.data == '7k':
            markup = types.InlineKeyboardMarkup(row_width=1)
            buy = types.InlineKeyboardButton('Купить', callback_data = 'buy5')
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(backbtn, buy)
            vbucks = open('icons/bucks.png', 'rb')
            bot.send_photo(call.message.chat.id, vbucks, caption='<b>7800 В-Баксов на ваш аккаунт через XBOX.\n\nЦена: 3849 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'buy5':
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton('Оплатить', url='https://github.com/kommo124/TarkovMapsBot'))
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(backbtn)
            bucks22 = open('icons/bucks.png', 'rb')
            bot.send_photo(call.message.chat.id, bucks22, caption='<b>Ссылка на оплату будет действовать 10 минут \n \nЦена: 2399 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == '13k':
            markup = types.InlineKeyboardMarkup(row_width=1)
            buy = types.InlineKeyboardButton('Купить', callback_data = 'buy6')
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(backbtn, buy)
            vbucks = open('icons/bucks.png', 'rb')
            bot.send_photo(call.message.chat.id, vbucks, caption='<b>13500 В-Баксов на ваш аккаунт через XBOX.\n\nЦена: 5999 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'buy6':
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton('Оплатить', url='https://github.com/kommo124/TarkovMapsBot'))
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(backbtn)
            bucks22 = open('icons/bucks.png', 'rb')
            bot.send_photo(call.message.chat.id, bucks22, caption='<b>Ссылка на оплату будет действовать 10 минут \n \nЦена: 2399 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == '11k':
            markup = types.InlineKeyboardMarkup(row_width=1)
            buy = types.InlineKeyboardButton('Купить', callback_data = 'buy7')
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(backbtn, buy)
            vbucks = open('icons/bucks.png', 'rb')
            bot.send_photo(call.message.chat.id, vbucks, caption='<b>27000 В-Баксов на ваш аккаунт через XBOX.\n\nЦена: 11849 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'buy7':
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton('Оплатить', url='https://github.com/kommo124/TarkovMapsBot'))
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(backbtn)
            bucks22 = open('icons/bucks.png', 'rb')
            bot.send_photo(call.message.chat.id, bucks22, caption='<b>Ссылка на оплату будет действовать 10 минут \n \nЦена: 11849 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'giftom':
            markup = types.InlineKeyboardMarkup(row_width=2)
            vb1 = types.InlineKeyboardButton('200 В-Баксов | 119₽', callback_data = 'vb')
            vb2 = types.InlineKeyboardButton('300 В-Баксов | 169₽', callback_data = 'vb1')
            vb3 = types.InlineKeyboardButton('400 В-Баксов | 219₽', callback_data = 'vb2')
            vb4 = types.InlineKeyboardButton('500 В-Баксов | 339₽', callback_data = 'vb3')
            vb5 = types.InlineKeyboardButton('600 В-Баксов | 379₽', callback_data = 'vb4')
            vb6 = types.InlineKeyboardButton('700 В-Баксов | 439₽', callback_data = 'vb5')
            vb7 = types.InlineKeyboardButton('800 В-Баксов | 489₽', callback_data = 'vb6')
            vb8 = types.InlineKeyboardButton('900 В-Баксов | 549₽', callback_data = 'vb7')
            vb9 = types.InlineKeyboardButton('1000 В-Баксов | 599₽', callback_data = 'vb8')
            vb10 = types.InlineKeyboardButton('1100 В-Баксов | 649₽', callback_data = 'vb9')
            vb11 = types.InlineKeyboardButton('1200 В-Баксов | 699₽', callback_data = 'vb10')
            vb12 = types.InlineKeyboardButton('1300 В-Баксов | 749₽', callback_data = 'vb11')
            vb13 = types.InlineKeyboardButton('1400 В-Баксов | 799₽', callback_data = 'vb12')
            vb14 = types.InlineKeyboardButton('1500 В-Баксов | 849₽', callback_data = 'vb13')
            vb15 = types.InlineKeyboardButton('1600 В-Баксов | 899₽', callback_data = 'vb14')
            vb16 = types.InlineKeyboardButton('1700 В-Баксов | 849₽', callback_data = 'vb15')
            vb17 = types.InlineKeyboardButton('1800 В-Баксов | 909₽', callback_data = 'vb16')
            vb18 = types.InlineKeyboardButton('1900 В-Баксов | 969₽', callback_data = 'vb17')
            vb19 = types.InlineKeyboardButton('2000 В-Баксов | 1039₽', callback_data = 'vb18')
            vb20 = types.InlineKeyboardButton('2100 В-Баксов | 1099₽', callback_data = 'vb19')
            vb21 = types.InlineKeyboardButton('2200 В-Баксов | 1149₽', callback_data = 'vb20')
            vb22 = types.InlineKeyboardButton('2300 В-Баксов | 1199₽', callback_data = 'vb21')
            vb23 = types.InlineKeyboardButton('2400 В-Баксов | 1249₽', callback_data = 'vb22')
            vb24 = types.InlineKeyboardButton('2500 В-Баксов | 1299₽', callback_data = 'vb23')
            vb25 = types.InlineKeyboardButton('2600 В-Баксов | 1349₽', callback_data = 'vb24')
            vb26 = types.InlineKeyboardButton('2700 В-Баксов | 1399₽', callback_data = 'vb25')
            vb27 = types.InlineKeyboardButton('2800 В-Баксов | 1469₽', callback_data = 'vb26')
            vb28 = types.InlineKeyboardButton('2900 В-Баксов | 1539₽', callback_data = 'vb27')
            vb29 = types.InlineKeyboardButton('3000 В-Баксов | 1799₽', callback_data = 'vb28')
            vb30 = types.InlineKeyboardButton('3500 В-Баксов | 1949₽', callback_data = 'vb29')
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(vb1, vb2, vb3, vb4, vb5, vb6, vb7, vb8, vb9, vb10, vb11, vb12, vb13, vb14, vb15, vb16, vb17, vb18, vb19, vb20, vb21, vb22, vb23, vb24, vb25, vb26, vb27, vb28, vb29, vb30, backbtn)
            vb222 = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vb222, caption='<b>Подарим любой предмет из магазина на выбранное вами количество В-Баксов. \n \nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nПосле оплаты вы должны написать в бота ваш никнейм EPIC и какой предмет вам подарить.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (НЕЛЬЗЯ КУПИТЬ 2800 В-Баксов И ВЫБРАТЬ 2 ПРЕДМЕТА НАПРИМЕР ЗА 800 В-БАКСОВ И 2000)</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vb':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl1')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 119 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vb1':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl2')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 169 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vb2':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl3')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 169 ₽</b>', parse_mode="html", reply_markup=markup)
        elif call.data == 'vb3':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl4')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 219 ₽</b>', parse_mode="html", reply_markup=markup)
        elif call.data == 'vb4':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl5')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 249 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vb5':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl6')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 299 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vb6':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl7')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 349 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vb7':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl8')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 399 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vb8':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl9')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 449 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vb9':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl10')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 549 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vb10':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl11')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 599 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vb11':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl12')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 659 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vb12':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl13')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 699 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vb13':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl14')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 749 ₽</b>', parse_mode="html", reply_markup=markup)
        elif call.data == 'vb14':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl15')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 799 ₽</b>', parse_mode="html", reply_markup=markup)
        elif call.data == 'vb15':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl16')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 849 ₽</b>', parse_mode="html", reply_markup=markup)
        elif call.data == 'vb16':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl17')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 899 ₽</b>', parse_mode="html", reply_markup=markup)
        elif call.data == 'vb17':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl18')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 949 ₽</b>', parse_mode="html", reply_markup=markup)
        elif call.data == 'vb18':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl19')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 999 ₽</b>', parse_mode="html", reply_markup=markup)
        elif call.data == 'vb19':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl20')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 1049 ₽</b>', parse_mode="html", reply_markup=markup)
        elif call.data == 'vb20':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl21')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 1099 ₽</b>', parse_mode="html", reply_markup=markup)
        elif call.data == 'vb21':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl22')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 1149 ₽</b>', parse_mode="html", reply_markup=markup)
        elif call.data == 'vb22':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl23')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 1199 ₽</b>', parse_mode="html", reply_markup=markup)
        elif call.data == 'vb23':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl24')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 1249 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vb24':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl25')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 1299 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vb25':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl26')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 1349 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vb26':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl27')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 1399 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vb27':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl28')
            markup.add(opl,backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 1449 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vb28':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl29')
            markup.add(opl, backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 1499 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vb29':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            opl = types.InlineKeyboardButton('Купить', callback_data = 'opl30')
            markup.add(opl, backbtn)
            vbks = open('icons/gift.png', 'rb')
            bot.send_photo(call.message.chat.id, vbks, caption='<b>Для покупки вы должны добавить в друзья ОБЯЗАТЕЛЬНО ВСЕ НАШИ Аккаунты: \nbucks1\nbucks2\nbucks3 \n\nПодарить подарок сможем после 48 часов после принятия нами вашей заявки в друзья.\n\nВНИМАНИЕ! Мы не дарим В-Баксы, мы дарим предмет за то количество В-Баксов, которое вы купили.\n\n1 ЗАКАЗ - 1 ПОДАРОК. (ПРИМЕР: НЕЛЬЗЯ КУПИТЬ 2800 В-БАКСОВ И ВЫБРАТЬ 2 ПРЕДМЕТА - ОДИН ЗА 800 В-БАКСОВ, ДРУГОЙ ЗА 2000.)Цена: 1549 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'code':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            cod1 = types.InlineKeyboardButton('1000 В-Баксов | 1359₽', callback_data = 'varbaks1')
            cod2 = types.InlineKeyboardButton('2800 В-Баксов | 2859₽', callback_data = 'varbaks2')
            cod3 = types.InlineKeyboardButton('5000 В-Баксов | 4549₽', callback_data = 'varbaks3')
            cod4 = types.InlineKeyboardButton('135000 В-Баксов | 10699₽', callback_data = 'varbaks4')
            markup.add(cod1, cod2, cod4, backbtn)
            codesy = open('icons/codes.png', 'rb')
            bot.send_photo(call.message.chat.id, codesy, caption='<b>Ввести код можно по ссылке - \nhttps://www.fortnite.com/vbuckscard</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'varbaks1':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyvb1k = types.InlineKeyboardButton('Купить', callback_data = 'oplatavb1k')
            markup.add(buyvb1k, backbtn)
            codesy = open('icons/1kvb.png', 'rb')
            bot.send_photo(call.message.chat.id, codesy, caption='<b>1000 В-Баксов кодом на ваш аккаунт.\n\nВвести код можно по ссылке - \nhttps://www.fortnite.com/vbuckscard\n\nЦена: 1359 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'varbaks2':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyvb1k = types.InlineKeyboardButton('Купить', callback_data = 'oplatavb2k')
            markup.add(buyvb1k, backbtn)
            codesy = open('icons/2kvb.png', 'rb')
            bot.send_photo(call.message.chat.id, codesy, caption='<b>1000 В-Баксов кодом на ваш аккаунт.\n\nВвести код можно по ссылке - \nhttps://www.fortnite.com/vbuckscard\n\nЦена: 2859 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'varbaks3':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyvb1k = types.InlineKeyboardButton('Купить', callback_data = 'oplatavb5k')
            markup.add(buyvb1k, backbtn)
            codesy = open('icons/5kvb.png', 'rb')
            bot.send_photo(call.message.chat.id, codesy, caption='<b>1000 В-Баксов кодом на ваш аккаунт.\n\nВвести код можно по ссылке - \nhttps://www.fortnite.com/vbuckscard\n\nЦена: 3549 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'varbaks4':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyvb1k = types.InlineKeyboardButton('Купить', callback_data = 'oplatavb13k')
            markup.add(buyvb1k, backbtn)
            codesy = open('icons/13kvb.png', 'rb')
            bot.send_photo(call.message.chat.id, codesy, caption='<b>13000 В-Баксов кодом на ваш аккаунт.\n\nВвести код можно по ссылке - \nhttps://www.fortnite.com/vbuckscard\n\nЦена: 10699 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'netflix':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            net1month = types.InlineKeyboardButton('1 месяц', callback_data = 'net1m')
            markup.add(net1month, backbtn)
            net = open('icons/netflix3.png', 'rb')
            bot.send_photo(call.message.chat.id, net, caption='<b>Создадим аккаунт Netflix на вашу почту с подпиской которую вы выберете.\n\nЧтобы пользоваться аккаунтом вам обязательно будет нужен Турецкий впн.</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'net1m':
            markup = types.InlineKeyboardMarkup(row_width=2)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            net1month1 = types.InlineKeyboardButton('Standart 720p | 509₽', callback_data = 'net1m1')
            net1month2 = types.InlineKeyboardButton('Premium 1080p | 799₽', callback_data = 'net1m2')
            markup.add(net1month1, net1month2)
            net = open('icons/netflix3.png', 'rb')
            bot.send_photo(call.message.chat.id, net, caption='<b>Создадим аккаунт Netflix на вашу почту с подпиской которую вы выберете.\n\nЧтобы пользоваться аккаунтом вам обязательно будет нужен Турецкий впн.</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'net1m1':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buynet = types.InlineKeyboardButton('Купить', callback_data = 'buynet')
            markup.add(buynet, backbtn)
            net = open('icons/netflix3.png', 'rb')
            bot.send_photo(call.message.chat.id, net, caption='<b>Подписка Standart 720p на месяц.\n\nЧтобы пользоваться аккаунтом вам обязательно будет нужен Турецкий впн.\n\nЦена: 509 ₽</b>', parse_mode="html", reply_markup=markup)


        elif call.data == 'net1m2':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buynet = types.InlineKeyboardButton('Купить', callback_data = 'buynet')
            net = open('icons/netflix3.png', 'rb')
            markup.add(buynet, backbtn)
            bot.send_photo(call.message.chat.id, net, caption='<b>Подписка Premium 1080p на месяц.\n\nЧтобы пользоваться аккаунтом вам обязательно будет нужен Турецкий впн.\n\nЦена: 799 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'valorant':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            valcodes = types.InlineKeyboardButton('Коды Россия и Европа', callback_data = 'valcodes')
            valcodes2 = types.InlineKeyboardButton('Коды Турция', callback_data = 'valcodesTR')
            accs = types.InlineKeyboardButton('Аккаунты', callback_data = 'valaccs')
            markup.add(valcodes, valcodes2, accs)
            valopen = open('icons/valorant.png', 'rb')
            bot.send_photo(call.message.chat.id, valopen, caption='<b>Коды на Valorant Points\n\nВвести коды вы можете сами прямо в игре!\n\nБудьте внимательны, проверяйте свой регион перед покупкой кодов!</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'valcodes':
            markup = types.InlineKeyboardMarkup(row_width=2)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            vp1 = types.InlineKeyboardButton('75 VP | 149₽', callback_data = 'vp1')
            vp2 = types.InlineKeyboardButton('240 VP | 299₽', callback_data = 'vp2')
            vp3 = types.InlineKeyboardButton('475 VP | 495₽', callback_data = 'vp3')
            vp4 = types.InlineKeyboardButton('1000 VP | 1029₽', callback_data = 'vp4')
            vp5 = types.InlineKeyboardButton('1520 VP | 1459₽', callback_data = 'vp5')
            vp6 = types.InlineKeyboardButton('2575 VP | 2529₽', callback_data = 'vp6')
            vp7 = types.InlineKeyboardButton('5350 VP | 5239₽', callback_data = 'vp7')
            vp8 = types.InlineKeyboardButton('8700 VP | 8159₽', callback_data = 'vp8')
            markup.add(vp1, vp2, vp3, vp4, vp5, vp6, vp7, vp8, backbtn)
            valopen = open('icons/valorant.png', 'rb')
            bot.send_photo(call.message.chat.id, valopen, caption='<b>Коды на регионы Россия и Европа\n\nНе работают на любые другие регионы!\n\nВвести код можете сами прямо в игре!</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vp1':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyvp = types.InlineKeyboardButton('Купить', callback_data = 'buyvp')
            markup.add(buyvp, backbtn)
            valopen = open('icons/valorant.png', 'rb')
            bot.send_photo(call.message.chat.id, valopen, caption='<b>75 VP Кодом.\n\nВвести код можно прямо в игре.\n\nАвтовыдача.\n\nЦена: 149 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vp2':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyvp = types.InlineKeyboardButton('Купить', callback_data = 'buyvp')
            markup.add(buyvp, backbtn)
            valopen = open('icons/valorant.png', 'rb')
            bot.send_photo(call.message.chat.id, valopen, caption='<b>240 VP Кодом.\n\nВвести код можно прямо в игре.\n\nАвтовыдача.\n\nЦена: 299 ₽</b>', parse_mode="html", reply_markup=markup)
        
        elif call.data == 'vp3':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyvp = types.InlineKeyboardButton('Купить', callback_data = 'buyvp')
            markup.add(buyvp, backbtn)
            valopen = open('icons/valorant.png', 'rb')
            bot.send_photo(call.message.chat.id, valopen, caption='<b>475 VP Кодом.\n\nВвести код можно прямо в игре.\n\nАвтовыдача.\n\nЦена: 495 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vp4':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyvp = types.InlineKeyboardButton('Купить', callback_data = 'buyvp')
            markup.add(buyvp, backbtn)
            valopen = open('icons/valorant.png', 'rb')
            bot.send_photo(call.message.chat.id, valopen, caption='<b>1000 VP Кодом.\n\nВвести код можно прямо в игре.\n\nАвтовыдача.\n\nЦена: 1029 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vp5':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyvp = types.InlineKeyboardButton('Купить', callback_data = 'buyvp')
            markup.add(buyvp, backbtn)
            valopen = open('icons/valorant.png', 'rb')
            bot.send_photo(call.message.chat.id, valopen, caption='<b>1520 VP Кодом.\n\nВвести код можно прямо в игре.\n\nАвтовыдача.\n\nЦена: 1459 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vp6':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyvp = types.InlineKeyboardButton('Купить', callback_data = 'buyvp')
            markup.add(buyvp, backbtn)
            valopen = open('icons/valorant.png', 'rb')
            bot.send_photo(call.message.chat.id, valopen, caption='<b>2575 VP Кодом.\n\nВвести код можно прямо в игре.\n\nАвтовыдача.\n\nЦена: 2529 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vp7':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyvp = types.InlineKeyboardButton('Купить', callback_data = 'buyvp')
            markup.add(buyvp, backbtn)
            valopen = open('icons/valorant.png', 'rb')
            bot.send_photo(call.message.chat.id, valopen, caption='<b>5350 VP Кодом.\n\nВвести код можно прямо в игре.\n\nАвтовыдача.\n\nЦена: 5239 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vp8':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyvp = types.InlineKeyboardButton('Купить', callback_data = 'buyvp')
            markup.add(buyvp, backbtn)
            valopen = open('icons/valorant.png', 'rb')
            bot.send_photo(call.message.chat.id, valopen, caption='<b>8700 VP Кодом.\n\nВвести код можно прямо в игре.\n\nАвтовыдача.\n\nЦена: 8159 ₽</b>', parse_mode="html", reply_markup=markup)


        elif call.data == 'valcodesTR':
            markup = types.InlineKeyboardMarkup(row_width=2)
            vp11 = types.InlineKeyboardButton('475 VP | 379₽', callback_data = 'vp11')
            vp22 = types.InlineKeyboardButton('1000 VP | 699₽', callback_data = 'vp22')
            vp33 = types.InlineKeyboardButton('2050 VP | 1399₽', callback_data = 'vp33')
            vp44 = types.InlineKeyboardButton('2950 VP | 2149₽', callback_data = 'vp44')
            vp55 = types.InlineKeyboardButton('3650 VP | 2399₽', callback_data = 'vp55')
            vp66 = types.InlineKeyboardButton('5350 VP | 3459₽', callback_data = 'vp66')
            vp77 = types.InlineKeyboardButton('11000 VP | 6899₽', callback_data = 'vp77')
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            markup.add(vp11, vp22, vp33, vp44, vp55, vp66, vp77, backbtn)
            valopen = open('icons/valorant.png', 'rb')
            bot.send_photo(call.message.chat.id, valopen, caption='<b>Коды на регион Турция.\n\nНе работают на любые другие регионы!\n\nВвести код можете сами прямо в игре!</b>', parse_mode="html", reply_markup=markup)
            
        elif call.data == 'vp11':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyvp = types.InlineKeyboardButton('Купить', callback_data = 'buyvp')
            markup.add(buyvp, backbtn)
            valopen = open('icons/valorant.png', 'rb')
            bot.send_photo(call.message.chat.id, valopen, caption='<b>475 VP Кодом.\n\nВвести код можно прямо в игре.\n\nАвтовыдача.\n\nЦена: 379 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vp22':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyvp = types.InlineKeyboardButton('Купить', callback_data = 'buyvp')
            markup.add(buyvp, backbtn)
            valopen = open('icons/valorant.png', 'rb')
            bot.send_photo(call.message.chat.id, valopen, caption='<b>1000 VP Кодом.\n\nВвести код можно прямо в игре.\n\nАвтовыдача.\n\nЦена: 699 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vp33':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyvp = types.InlineKeyboardButton('Купить', callback_data = 'buyvp')
            markup.add(buyvp, backbtn)
            valopen = open('icons/valorant.png', 'rb')
            bot.send_photo(call.message.chat.id, valopen, caption='<b>2050 VP Кодом.\n\nВвести код можно прямо в игре.\n\nАвтовыдача.\n\nЦена: 1399 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vp44':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyvp = types.InlineKeyboardButton('Купить', callback_data = 'buyvp')
            markup.add(buyvp, backbtn)
            valopen = open('icons/valorant.png', 'rb')
            bot.send_photo(call.message.chat.id, valopen, caption='<b>2950 VP Кодом.\n\nВвести код можно прямо в игре.\n\nАвтовыдача.\n\nЦена: 2149 ₽</b>', parse_mode="html", reply_markup=markup)
            
        elif call.data == 'vp55':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyvp = types.InlineKeyboardButton('Купить', callback_data = 'buyvp')
            markup.add(buyvp, backbtn)
            valopen = open('icons/valorant.png', 'rb')
            bot.send_photo(call.message.chat.id, valopen, caption='<b>3650 VP Кодом.\n\nВвести код можно прямо в игре.\n\nАвтовыдача.\n\nЦена: 2399 ₽</b>', parse_mode="html", reply_markup=markup)
            
        elif call.data == 'vp66':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyvp = types.InlineKeyboardButton('Купить', callback_data = 'buyvp')
            markup.add(buyvp, backbtn)
            valopen = open('icons/valorant.png', 'rb')
            bot.send_photo(call.message.chat.id, valopen, caption='<b>5350 VP Кодом.\n\nВвести код можно прямо в игре.\n\nАвтовыдача.\n\nЦена: 3459 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'vp77':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyvp = types.InlineKeyboardButton('Купить', callback_data = 'buyvp')
            markup.add(buyvp, backbtn)
            valopen = open('icons/valorant.png', 'rb')
            bot.send_photo(call.message.chat.id, valopen, caption='<b>11000 VP Кодом.\n\nВвести код можно прямо в игре.\n\nАвтовыдача.\n\nЦена: 6899 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'valaccs':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            TRacc = types.InlineKeyboardButton('Турция', callback_data = 'Tracc')
            markup.add(TRacc, backbtn)
            valopen = open('icons/valorant.png', 'rb')
            bot.send_photo(call.message.chat.id, valopen, caption='<b>Пустой аккаунт с турецким регионом.</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'Tracc':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyacc = types.InlineKeyboardButton('Купить', callback_data = 'buyacc')
            markup.add(buyacc, backbtn)
            valopen = open('icons/valorant.png', 'rb')
            bot.send_photo(call.message.chat.id, valopen, caption='<b>Пустой аккаунт с турецким регионом.\nЦена: 599 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'exit':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            exit = types.InlineKeyboardButton('ExitLag', callback_data = 'buyexit')
            markup.add(exit, backbtn)
            exopen = open('icons/exitlag.png', 'rb')
            bot.send_photo(call.message.chat.id, exopen, caption='<b>ExitLag на ваш аккаунт.</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'buyexit':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            exitcost = types.InlineKeyboardButton('ExitLag 1 месяц | 649₽', callback_data = 'buyexit1')
            markup.add(exitcost, backbtn)
            exopen = open('icons/exitlag.png', 'rb')
            bot.send_photo(call.message.chat.id, exopen, caption='<b>Коды активации ExitLag.\n\nВвести код можете в профиле своего аккаунта по ссылке.\nhttps://www.exitlag.com/prepaidcode/redeem</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'buyexit1':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            exitcostbuy = types.InlineKeyboardButton('Купить', callback_data = 'buyexit2')
            markup.add(exitcostbuy, backbtn)
            exopen = open('icons/exitlag.png', 'rb')
            bot.send_photo(call.message.chat.id, exopen, caption='<b>Коды активации ExitLag с подпиской на 1 месяц.\n\nВвести код можете в профиле своего аккаунта по ссылке.\nhttps://www.exitlag.com/prepaidcode/redeem\nЦена: 649 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'Roblox':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            robloxa = types.InlineKeyboardButton('Robux', callback_data = 'robuxi')
            markup.add(robloxa, backbtn)
            rbopen = open('icons/roblox.png', 'rb')
            bot.send_photo(call.message.chat.id, rbopen, caption='<b>Товары игры Roblox</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'robuxi':
            markup = types.InlineKeyboardMarkup(row_width=2)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            roblox1 = types.InlineKeyboardButton('100 Robux', callback_data = 'robuxi1')
            roblox2 = types.InlineKeyboardButton('500 Robux', callback_data = 'robuxi2')
            roblox3 = types.InlineKeyboardButton('1000 Robux', callback_data = 'robuxi3')
            roblox4 = types.InlineKeyboardButton('1500 Robux', callback_data = 'robuxi4')
            roblox5 = types.InlineKeyboardButton('2000 Robux', callback_data = 'robuxi5')
            markup.add(roblox1, roblox2, roblox3, roblox4, roblox5, backbtn)
            rbopen = open('icons/roblox.png', 'rb')
            bot.send_photo(call.message.chat.id, rbopen, caption='<b>Покупка валюты для игры Roblox</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'robuxi1':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            bloxbuy = types.InlineKeyboardButton('Купить', callback_data = 'robuxi11')
            markup.add(bloxbuy, backbtn)
            rbopen = open('icons/roblox.png', 'rb')
            bot.send_photo(call.message.chat.id, rbopen, caption='<b>Robux - 100 \nЦена: 50₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'robuxi2':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            bloxbuy = types.InlineKeyboardButton('Купить', callback_data = 'robuxi12')
            markup.add(bloxbuy, backbtn)
            rbopen = open('icons/roblox.png', 'rb')
            bot.send_photo(call.message.chat.id, rbopen, caption='<b>Robux - 500 \nЦена: 250₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'robuxi3':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            bloxbuy = types.InlineKeyboardButton('Купить', callback_data = 'robuxi12')
            markup.add(bloxbuy, backbtn)
            rbopen = open('icons/roblox.png', 'rb')
            bot.send_photo(call.message.chat.id, rbopen, caption='<b>Robux - 1000 \nЦена: 500₽</b>', parse_mode="html", reply_markup=markup)


        elif call.data == 'robuxi4':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            bloxbuy = types.InlineKeyboardButton('Купить', callback_data = 'robuxi12')
            markup.add(bloxbuy, backbtn)
            rbopen = open('icons/roblox.png', 'rb')
            bot.send_photo(call.message.chat.id, rbopen, caption='<b>Robux - 1500 \nЦена: 750₽</b>', parse_mode="html", reply_markup=markup)
        
        elif call.data == 'robuxi5':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            bloxbuy = types.InlineKeyboardButton('Купить', callback_data = 'robuxi12')
            markup.add(bloxbuy, backbtn)
            rbopen = open('icons/roblox.png', 'rb')
            bot.send_photo(call.message.chat.id, rbopen, caption='<b>Robux - 2000 \nЦена: 1000₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'pubg':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            uccodes = types.InlineKeyboardButton('UC Коды', callback_data = 'uccodes')
            markup.add(uccodes, backbtn)
            ucopen = open('icons/pubg.png', 'rb')
            bot.send_photo(call.message.chat.id, ucopen, caption='<b>Моментально выдадим вам любой код на UC PUBG Mobile который вы сможете активировать сами!\n\nЛегкая инструкция как активировать код\nhttps://telegra.ph/Aktivaciya-koda-na-UC-PUBG-Mobile-01-06\n\nТолько PUBG MOBILE</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'uccodes':
            markup = types.InlineKeyboardMarkup(row_width=1)
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            uc1 = types.InlineKeyboardButton('60 UC | 109₽', callback_data = 'uc1')
            uc2 = types.InlineKeyboardButton('325 UC | 529₽', callback_data = 'uc2')
            uc3 = types.InlineKeyboardButton('660 UC | 929₽', callback_data = 'uc3')
            uc4 = types.InlineKeyboardButton('1800 UC | 2529₽', callback_data = 'uc4')
            uc5 = types.InlineKeyboardButton('3850 UC | 4599₽', callback_data = 'uc5')
            uc6 = types.InlineKeyboardButton('8100 UC | 9199₽', callback_data = 'uc6')
            markup.add(uc1, uc2, uc3, uc4, uc5, uc6)
            ucopen = open('icons/pubg.png', 'rb')
            bot.send_photo(call.message.chat.id, ucopen, caption='<b>Моментально выдадим вам любой код на UC PUBG Mobile который вы сможете активировать сами!\n\nЛегкая инструкция как активировать код\nhttps://telegra.ph/Aktivaciya-koda-na-UC-PUBG-Mobile-01-06\n\nТолько PUBG MOBILE\nЦена: 109 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'uc1':
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyuc1 = types.InlineKeyboardButton('Купить', callback_data = 'buyuc1')
            markup.add(buyuc1, backbtn)
            ucopen = open('icons/pubg.png', 'rb')
            bot.send_photo(call.message.chat.id, ucopen, caption='<b>Моментально выдадим вам любой код на UC PUBG Mobile который вы сможете активировать сами!\n\nЛегкая инструкция как активировать код\nhttps://telegra.ph/Aktivaciya-koda-na-UC-PUBG-Mobile-01-06\n\nТолько PUBG MOBILE</b>\nЦена: 529 ₽', parse_mode="html", reply_markup=markup)

        elif call.data == 'uc2':
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyuc2 = types.InlineKeyboardButton('Купить', callback_data = 'buyuc2')
            markup.add(buyuc2, backbtn)
            ucopen = open('icons/pubg.png', 'rb')
            bot.send_photo(call.message.chat.id, ucopen, caption='<b>Моментально выдадим вам любой код на UC PUBG Mobile который вы сможете активировать сами!\n\nЛегкая инструкция как активировать код\nhttps://telegra.ph/Aktivaciya-koda-na-UC-PUBG-Mobile-01-06\n\nТолько PUBG MOBILE\nЦена: 929 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'uc3':
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyuc3 = types.InlineKeyboardButton('Купить', callback_data = 'buyuc3')
            markup.add(buyuc3, backbtn)
            ucopen = open('icons/pubg.png', 'rb')
            bot.send_photo(call.message.chat.id, ucopen, caption='<b>Моментально выдадим вам любой код на UC PUBG Mobile который вы сможете активировать сами!\n\nЛегкая инструкция как активировать код\nhttps://telegra.ph/Aktivaciya-koda-na-UC-PUBG-Mobile-01-06\n\nТолько PUBG MOBILE\nЦена: 2529 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'uc4':
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyuc4 = types.InlineKeyboardButton('Купить', callback_data = 'buyuc4')
            markup.add(buyuc1, backbtn)
            ucopen = open('icons/pubg.png', 'rb')
            bot.send_photo(call.message.chat.id, ucopen, caption='<b>Моментально выдадим вам любой код на UC PUBG Mobile который вы сможете активировать сами!\n\nЛегкая инструкция как активировать код\nhttps://telegra.ph/Aktivaciya-koda-na-UC-PUBG-Mobile-01-06\n\nТолько PUBG MOBILE\nЦена: 4599 ₽</b>', parse_mode="html", reply_markup=markup)

        elif call.data == 'uc5':
            backbtn = types.InlineKeyboardButton('Назад', callback_data = 'back')
            buyuc5 = types.InlineKeyboardButton('Купить', callback_data = 'buyuc5')
            markup.add(buyuc5, backbtn)
            ucopen = open('icons/pubg.png', 'rb')
            bot.send_photo(call.message.chat.id, ucopen, caption='<b>Моментально выдадим вам любой код на UC PUBG Mobile который вы сможете активировать сами!\n\nЛегкая инструкция как активировать код\nhttps://telegra.ph/Aktivaciya-koda-na-UC-PUBG-Mobile-01-06\n\nТолько PUBG MOBILE\nЦена: 9199 ₽</b>', parse_mode="html", reply_markup=markup)


        if call.data == 'back':
            markup = types.InlineKeyboardMarkup(row_width=1)
            shop = types.InlineKeyboardButton('Магазин', callback_data= 'magaz')
            profile = types.InlineKeyboardButton('Профиль', callback_data = 'profil')
            supp = types.InlineKeyboardButton('Поддержка', callback_data = 'supp')
            ozivi = types.InlineKeyboardButton('Отзывы', url='https://t.me/shopbotrevs')
            markup.add(shop, profile, supp, ozivi)
            mainmen = open('icons/mainmenu.png', 'rb')
            bot.send_photo(call.message.chat.id, mainmen, reply_markup=markup)

            
            





bot.polling(none_stop=True)


# markup = types.InlineKeyboardMarkup(row_width=2)
#     steam_dep = types.InlineKeyboardButton('Пополнение Steam', callback_data= 'dep')
#     spotifypremium = types.InlineKeyboardButton('Spotify Премиум', callback_data = 'spoti')
#     netsub = types.InlineKeyboardButton('Подписка на Netflix', callback_data = 'netflix')
#     fort = types.InlineKeyboardButton('Fortnite', callback_data = 'fortnite')
#     valorant = types.InlineKeyboardButton('Valorant', callback_data = 'valorant')
#     ExitLag = types.InlineKeyboardButton('ExitLag', callback_data = 'exit')
#     roblox = types.InlineKeyboardButton('Roblox', callback_data = 'Roblox')
    # pubg = types.InlineKeyboardButton('PUBG MOBILE', callback_data = 'pubg')