#!/usr/bin/python3

import time, threading, configparser, data

import telebot
from telebot import types

version = "0.0.1"

config = configparser.ConfigParser()
config.read_file(open("./token.config", mode="r"))
token = config.get("config", "token")

commands = {
    "start": "Begrüßung & Scan",
    "hilfe": "Informationen zur Bedienung",
    "neu": "Neues Gesicht anfordern",
    "stop": "Aktuelle Aktion abbrechen",
    "version": "Zeigt die aktuelle Version des Bots und die Neuerungen an",
}

number_board = types.ReplyKeyboardMarkup(one_time_keyboard=True)
itembtna = types.KeyboardButton("0-2")
itembtnv = types.KeyboardButton("4-6")
itembtnc = types.KeyboardButton("8-12")
itembtnd = types.KeyboardButton("15-20")
itembtne = types.KeyboardButton("25-32")
itembtnf = types.KeyboardButton("38-43")
itembtng = types.KeyboardButton("48-53")
itembtnh = types.KeyboardButton("60-100")
itembtni = types.KeyboardButton("Zufall")
number_board.row(itembtna, itembtnv, itembtnc)
number_board.row(itembtnd, itembtne, itembtnf)
number_board.row(itembtng, itembtnh, itembtni)

text_board = types.ReplyKeyboardMarkup(one_time_keyboard=True)
itembtna = types.KeyboardButton("Männlich")
itembtnv = types.KeyboardButton("Weiblich")
itembtnc = types.KeyboardButton("Zufall")
text_board.row(itembtna, itembtnv, itembtnc)

hideBoard = types.ReplyKeyboardRemove()


def listener(messages):
    for m in messages:
        if m.content_type == "text":
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)


def first_start():
    cids = data.get_all_users()
    for x in cids:
        cid = x[0]
        name = x[1]
        bot.send_message(
            cid,
            f"Hallo {name}, der Bot wurde neu gestartet - Version: {version} - weitere Infos unter /version",
        )


bot = telebot.TeleBot(token)
bot.set_update_listener(listener)


# Start
@bot.message_handler(commands=["start"])
def command_start(m):
    cid = m.chat.id
    first_name = m.from_user.first_name
    last_name = m.from_user.last_name
    username = m.from_user.username
    db_cid = data.get_user(cid)
    if cid != db_cid:
        userStep = 0
        user_data = [(cid, first_name, last_name, username, userStep)]
        data.store_user(user_data)
        bot.send_message(cid, "Hallo " + first_name + ", lass mich dich scannen...")
        bot.send_chat_action(cid, "typing")
        time.sleep(2)
        bot.send_message(cid, "Scan abgeschlossen.")
        command_help(m)
    else:
        bot.send_message(
            cid,
            "Du bist im System unter der Numer " + str(cid) + " bereits registriert.",
        )


# Hilfe
@bot.message_handler(commands=["hilfe"])
def command_help(m):
    cid = m.chat.id
    help_text = "Die folgenden Optionen sind verfügbar: \n"
    for key in commands:
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)


# 1) Neu anfordern
@bot.message_handler(commands=["neu"])
def neu(m):
    cid = m.chat.id
    bot.send_message(cid, "Männlich, Weiblich oder Zufall?", reply_markup=text_board)
    data.store_userStep(cid, 1)


# 2) Alter
@bot.message_handler(func=lambda message: data.get_userstep(message.chat.id) == 1)
def alter(m):
    cid = m.chat.id
    text = m.text

    bot.send_chat_action(cid, "typing")

    if text == "Männlich":
        data.store_userStep(cid, 2)

    elif text == "Weiblich":
        data.store_userStep(cid, 2)

    elif text == "Zufall":
        data.store_userStep(cid, 2)

    elif text == "/stop":
        bot.send_message(cid, "Aktion abgebrochen!")
        data.store_userStep(cid, 0)

    else:
        bot.reply_to(m, "Bitte das Keyboard benutzen.")

    bot.send_message(cid, "Welches Alter?", reply_markup=number_board)


# 3 Ausgabe
@bot.message_handler(func=lambda message: data.get_userstep(message.chat.id) == 2)
def ausgabe(m):
    cid = m.chat.id
    nummer = m.text
    if nummer == "0-2":
        return
    elif nummer == "4-6":
        return
    elif nummer == "8-12":
        return
    elif nummer == "15-20":
        return
    elif nummer == "25-32":
        return
    elif nummer == "38-43":
        return
    elif nummer == "48-53":
        return
    elif nummer == "60-100":
        return
    elif nummer == "Zufall":
        return
    elif nummer == "/stop":
        data.store_userStep(cid, 0)
        return
    else:
        bot.send_message(cid, "Bitte vorgegebenes Keyboard benutzen!")


# Stop
@bot.message_handler(commands=["stop"])
def stop(m):
    cid = m.chat.id
    bot.send_message(cid, "Aktion abgebrochen!")
    data.store_userStep(cid, 0)


# Version
@bot.message_handler(commands=["version"])
def version_info(m):
    cid = m.chat.id
    bot.send_message(cid, f"Version: {version}\nAktuelle Neuerungen: \n")


# Standard Handler
@bot.message_handler(func=lambda message: True, content_types=["text"])
def command_default(m):
    bot.send_message(
        m.chat.id,
        'Ich verstehe "'
        + m.text
        + '"nicht. Bitte einmal /start ausführen und dann /hilfe eingeben.',
    )


if __name__ == "__main__":
    threading.Thread(
        target=bot.infinity_polling, name="bot_infinity_polling", daemon=True
    ).start()
    first_start()
    while True:
        time.sleep(100)
        
"""To be added: 
    if gender == '':
        db_output = ImageRecord.query.filter(ImageRecord.age >= minimum_age, ImageRecord.age <= maximum_age).order_by(func.random()).first_or_404()

    if gender != '':
        db_output = ImageRecord.query.filter(ImageRecord.gender == gender, ImageRecord.age >= minimum_age, ImageRecord.age <= maximum_age).order_by(func.random()).first_or_404()

    db_output.last_served = datetime.utcnow()
    db.session.commit()
"""
